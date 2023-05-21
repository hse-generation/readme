import os

from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse_lazy, reverse
from books.models import Books
from books_authors.models import Books_authors
from books_genres.models import Books_genres
from reviews.models import Reviews


def index(request):
    data = {}
    data['books'] = Books.objects.all()[7:13]
    return render(request, 'home/index1.html', data)


def view_book(request, book_id):
    data = {}

    if 'save-review' in request.POST:
        review = Reviews(days=request.POST['days'],
                         text=request.POST['text'],
                         score=request.POST['rating'],
                         account_id=request.session['user_id'],
                         book_id=book_id)
        review.save()

    data['book'] = Books.objects.filter(id=book_id).values().first()
    if data['book']:
        book_authors = Books_authors.objects.filter(books_id_id=data['book']['id'])
        authors = [(author.author_id.id, author.author_id.author_name) for author in book_authors]
        data['book']['authors'] = authors

        book_genres = Books_genres.objects.filter(books_id_id=data['book']['id'])
        genres = [(genres.genre_id.id, genres.genre_id.genre_name) for genres in book_genres]
        data['book']['genres'] = genres

        data['book']['reviews'] = Reviews.objects.filter(book_id=data['book']['id'])

        if 'user_id' in request.session and not data['book']['reviews'].filter(account_id=request.session['user_id']).exists():
            data['book']['canReview'] = 1

    return render(request, 'books/view_book.html', data)
