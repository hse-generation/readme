import os

from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse_lazy, reverse
from books.models import Books
from accounts_books_statuses.models import AccountsBooksStatuses
from books_authors.models import Books_authors
from books_genres.models import Books_genres
from account.models import Users
from genres.models import Genres
from favorite_genres.models import FavoritesGenres


def index(request):
    data = {}

    if 'status-edit' in request.POST:
        status_number, book_id = request.POST['status-edit'].split(',')
        accountBookStatus = AccountsBooksStatuses.objects.filter(account_id=request.session['user_id'],
                                                                 book_id=book_id).first()
        if accountBookStatus:
            accountBookStatus.status = status_number
            accountBookStatus.save()
        else:
            newAccountBookStatus = AccountsBooksStatuses(status=status_number,
                                                         account_id=request.session['user_id'],
                                                         book_id=book_id)
            newAccountBookStatus.save()

    if 'user_id' in request.session:
        account = Users.objects.filter(id=request.session['user_id']).first()
        if not account.is_onboarding_passed:
            return redirect('popup_genres')

    data['books'] = Books.objects.all()[7:13]
    for book in data['books']:
        book_authors = Books_authors.objects.filter(books_id_id=book.id)
        authors = [(author.author_id.id, author.author_id.author_name) for author in book_authors]
        book.authors = authors

    if 'user_id' in request.session:  # если пользователь авторизован
        for book in data['books']:
            status = AccountsBooksStatuses.objects.filter(book=book, account=request.session['user_id']).first()
            if status:
                book.status_number = status.status
                book.status = AccountsBooksStatuses.ACCOUNTS_BOOKS_STATUSES.get(status.status)
                book.status_button = AccountsBooksStatuses.STATUSES_BUTTON.get(status.status)
            else:
                book.status_number = None
                book.status = None
                book.status_button = None

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
