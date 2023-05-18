import os

from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse_lazy, reverse
from books.models import Books
from accounts_books_statuses.models import AccountsBooksStatuses
from books_authors.models import Books_authors
from books_genres.models import Books_genres

def index(request):
    data = {}
    data['books'] = Books.objects.all()[7:13]
    for book in data['books']:
        book_authors = Books_authors.objects.filter(books_id_id=book.id)
        authors = [(author.author_id.id, author.author_id.author_name) for author in book_authors]
        book.authors = authors

    if 'user_id' in request.session:  # если пользователь авторизован
        for book in data['books']:
            status = AccountsBooksStatuses.objects.filter(book=book, account=request.session['user_id']).first()
            if status:
                book.status = AccountsBooksStatuses.ACCOUNTS_BOOKS_STATUSES.get(status.status)
                book.status_button = AccountsBooksStatuses.STATUSES_BUTTON.get(status.status)
            else:
                book.status = None
                book.status_button = None



    return render(request, 'home/index.html', data)

