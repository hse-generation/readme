import os

from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse_lazy, reverse
from books.models import Books
from books_authors.models import Books_authors
from books_genres.models import Books_genres


def index(request):
    data = {}
    data['books'] = Books.objects.all()[7:13]
    return render(request, 'home/index1.html', data)


def view_book(request, book_id):
    data = {}
    data['book'] = Books.objects.filter(id=book_id).values().first()
    if data['book']:
        book_authors = Books_authors.objects.filter(books_id_id=data['book']['id'])
        authors = [(author.author_id.id, author.author_id.author_name) for author in book_authors]
        data['book']['authors'] = authors

        book_genres = Books_genres.objects.filter(books_id_id=data['book']['id'])
        genres = [(genres.genre_id.id, genres.genre_id.genre_name) for genres in book_genres]
        data['book']['genres'] = genres

    return render(request, 'books/view_book.html', data)
