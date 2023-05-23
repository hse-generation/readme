from django.shortcuts import render, redirect
from books.models import Books
from accounts_books_statuses.models import AccountsBooksStatuses
from books_authors.models import Books_authors
from account.models import Users
from genres.models import Genres
from favorite_genres.models import FavoritesGenres
from read_books.models import ReadBooks
from sections.models import Sections
from math import ceil
from sections_books.models import SectionsBooks


def index(request):
    data = {}

    if 'status-edit' in request.POST:
        status_number, book_id = request.POST['status-edit'].split(',')
        AccountsBooksStatuses.save_or_update_status(request.session['user_id'], book_id, status_number)

        # cохраняем книгу в прочитанных, если статус 'Завершен'
        if int(status_number.strip()) == AccountsBooksStatuses.ACCOUNTS_BOOKS_STATUSES_TEXT_TO_NUMBER['COMPLETED']:
            account = Users.objects.filter(id=request.session['user_id']).first()
            book = Books.objects.filter(id=book_id).first()
            days = ceil(book.pages_count / account.pages_per_day)
            ReadBooks.create_new_read_book(request.session['user_id'], book_id, days)

    if 'user_id' in request.session:
        account = Users.objects.filter(id=request.session['user_id']).first()
        if not account.is_onboarding_passed:
            return redirect('popup_genres')

    if 'user_id' in request.session:  # если пользователь авторизован
        data['recommendations'] = Sections.get_book_recommendations(request.session['user_id'])
        for book in data['recommendations']:
            book_authors = Books_authors.objects.filter(books_id_id=book.id)
            authors = [(author.author_id.id, author.author_id.author_name) for author in book_authors]
            book.authors = authors

            status = AccountsBooksStatuses.objects.filter(book=book, account=request.session['user_id']).first()
            if status:
                book.status_number = status.status
                book.status = AccountsBooksStatuses.ACCOUNTS_BOOKS_STATUSES.get(status.status)
                book.status_button = AccountsBooksStatuses.STATUSES_BUTTON.get(status.status)

    sections = Sections.objects.all()
    data['sections'] = []
    for section in sections:
        book_ids = SectionsBooks.get_books_by_section(section.id)
        books = Books.objects.filter(id__in=book_ids)

        for book in books:
            book_authors = Books_authors.objects.filter(books_id_id=book.id)
            authors = [(author.author_id.id, author.author_id.author_name) for author in book_authors]
            book.authors = authors

        if 'user_id' in request.session:  # если пользователь авторизован
            for book in books:
                status = AccountsBooksStatuses.objects.filter(book=book, account=request.session['user_id']).first()
                if status:
                    book.status_number = status.status
                    book.status = AccountsBooksStatuses.ACCOUNTS_BOOKS_STATUSES.get(status.status)
                    book.status_button = AccountsBooksStatuses.STATUSES_BUTTON.get(status.status)

        data['sections'].append((section.name, books))


    data['accountsBooksStatuses'] = AccountsBooksStatuses.ACCOUNTS_BOOKS_STATUSES
    data['accountsBooksStatusesText'] = AccountsBooksStatuses.ACCOUNTS_BOOKS_STATUSES_TEXT

    return render(request, 'home/index.html', data)


def popup_genres(request):
    if 'non_chosen_genres' in request.POST:
        account = Users.objects.filter(id=request.session['user_id'])
        account.update(is_onboarding_passed=1)
        return redirect('home')

    if 'save_genres' in request.POST:
        for key in request.POST:
            if key.startswith('genre_'):
                genre_id = key.split('_')[1]
                new_fav_gen = FavoritesGenres(account_id_id=request.session['user_id'], genre_id_id=genre_id)
                new_fav_gen.save()
        account = Users.objects.filter(id=request.session['user_id'])
        account.update(is_onboarding_passed=1)
        return redirect('home')

    data = {}
    if 'user_id' not in request.session:
        return redirect('home')

    account = Users.objects.filter(id=request.session['user_id']).first()
    if account.is_onboarding_passed:
        return redirect('home')

    data['genres'] = Genres.objects.all()
    return render(request, 'home/pop-up.html', data)
