from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt

from .forms import AccountForm
from .models import Users
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from accounts_books_statuses.models import AccountsBooksStatuses
from books_authors.models import Books_authors
from account.models import Users
from read_books.models import ReadBooks
from books.models import Books
from math import ceil
from favorite_genres.models import FavoritesGenres
from genres.models import Genres


@csrf_exempt
def index(request):
    if 'user_id' not in request.session:  # если пользователь не авторизован, отправляем на страницу входа
        return redirect('login')
    else:
        user = Users.objects.filter(id=request.session['user_id']).values()
        if len(user) == 0 or user[0]['status'] == 0:
            return redirect('logout')

    data = {}  # дата (данные), которая отправляется в view

    if request.method == 'POST':
        if 'genre_id' in request.POST and 'action' in request.POST:
            genre_id = request.POST['genre_id']
            action = request.POST['action']
            user_id = request.session.get('user_id')

            if action == 'add':
                FavoritesGenres.objects.get_or_create(account_id_id=user_id, genre_id_id=genre_id)
            elif action == 'remove':
                FavoritesGenres.objects.filter(account_id_id=user_id, genre_id_id=genre_id).delete()

            return JsonResponse({'status': 'success'})


    if 'deactivate-account' in request.POST:
        Users.objects.filter(id=request.session['user_id']).update(status=0)
        return redirect("account")
    if 'save_account_info' in request.POST:  # проверяем была ли нажата кнопочка с name = save_account_info в post запросе
        info = request.POST
        info_pic = AccountForm(request.POST, request.FILES)
        Users.objects.filter(id=request.session['user_id']).update(name=info['name'],
                                                                   last_name=info['last_name'],
                                                                   about=info['about'],
                                                                   birthdate=info['birthdate'],
                                                                   email=info['email'],
                                                                   pages_per_day=info['pages_per_day'])
        request.session['name'] = info['name']
        if info_pic.is_valid() and len(request.FILES) > 0:
            info_pic.save()
            profile_picture = Users.objects.latest('id').profile_picture
            Users.objects.latest('id').delete()
            Users.objects.filter(id=request.session['user_id']).update(profile_picture=profile_picture)
            request.session['avatar'] = Users.objects.filter(id=request.session['user_id']).values()[0][
                'profile_picture']

        return redirect("account")

    user = Users.objects.filter(
        id=request.session['user_id']).values()  # берем из accounts вссех юзеров с id равный id пользака из сессии
    form = AccountForm(data=user[0])  # указываем в data значение из базы, чтобы автоматом выставлялись в поля
    data['form'] = form
    data['chosenGenres'] = data['chosenGenres'] = list(
        FavoritesGenres.get_favorite_genres_by_account(request.session['user_id'])
        .values_list('id', flat=True))
    data['genres'] = Genres.objects.all()

    data['profile_picture'] = user[0]['profile_picture']
    return render(request, 'account/index.html', data)


def shelf(request, status_id):
    data = {}

    data['books'] = AccountsBooksStatuses.get_books_by_status(request.session['user_id'], status_id)

    if 'status-edit' in request.POST:
        status_number, book_id = request.POST['status-edit'].split(',')
        AccountsBooksStatuses.save_or_update_status(request.session['user_id'], book_id, status_number)

        # cохраняем книгу в прочитанных, если статус 'Завершен'
        if status_number == AccountsBooksStatuses.ACCOUNTS_BOOKS_STATUSES_TEXT_TO_NUMBER['COMPLETED']:
            account = Users.objects.filter(id=request.session['user_id']).first()
            book = Books.objects.filter(id=book_id).first()
            days = ceil(book.pages_count / account.pages_per_day)
            ReadBooks.create_new_read_book(request.session['user_id'], book_id, days)

    for book in data['books']:
        book_authors = Books_authors.objects.filter(books_id_id=book.id)
        authors = [(author.author_id.id, author.author_id.author_name) for author in book_authors]
        book.authors = authors

        status = AccountsBooksStatuses.objects.filter(book_id=book.id, account=request.session['user_id']).first()
        if status:
            book.status_number = status.status
            book.status = AccountsBooksStatuses.ACCOUNTS_BOOKS_STATUSES.get(status.status)
            book.status_button = AccountsBooksStatuses.STATUSES_BUTTON.get(status.status)

    data['accountsBooksStatuses'] = AccountsBooksStatuses.ACCOUNTS_BOOKS_STATUSES
    data['accountsBooksStatusesText'] = AccountsBooksStatuses.ACCOUNTS_BOOKS_STATUSES_TEXT
    return render(request, 'account/shelf.html', data)


def logout(request):
    if 'user_id' in request.session.keys():
        del request.session['user_id']
    return redirect('home')
