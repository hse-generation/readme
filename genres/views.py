# import os
#
# from django.shortcuts import render, redirect
# from django.http import HttpResponse, HttpResponseRedirect
# from django.urls import reverse_lazy, reverse
#
#
#
# def index(request):
#     # return render(request, 'users/register.html', data)
#     return render(request, 'genres/index.html')
#


import os

from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse_lazy, reverse
from books.models import Books
from genres.models import Genres


def index(request):
    data = {}
    data['genres'] = Genres.objects.all()[:10]
    return render(request, 'genres/index.html', data)

def get_genre_books(request, genre_id):
    data = {}
    data['books'] = Books.objects.filter(genre_id__id=genre_id).values()
    data['genre'] = Genres.objects.filter(id=genre_id).values()[0]['genre_name']
    return render(request, 'genres/genre-books.html', data)

