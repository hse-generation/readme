import os

from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse_lazy, reverse
from books.models import Books
from genres.models import Genres
from authors.models import Authors
from books_genres.models import Books_genres
import pandas as pd
from django.contrib.staticfiles.storage import staticfiles_storage
import logging


def index(request):
    # df = pd.read_csv('/files/chitai_gorod.csv')
    # print(df)
    data = {}
    return render(request, 'parsers/index.html', data)


def add_genres_from_file(request):
    file = staticfiles_storage.path('parsers/chitai_gorod.csv')
    df = pd.read_csv(file)
    df.columns = ['book_url', 'name', 'author_name', 'genres', 'score', 'pages', 'description', 'cover_link']
    data = {}
    for index, row in df.iterrows():
        genres = row['genres'].split('.')
        for genre in genres:
            genre_name = genre.strip()
            if not Genres.objects.filter(genre_name=genre_name).exists():
                genre_obj = Genres(genre_name=genre_name)
                genre_obj.save()

    data['info'] = 1
    return render(request, 'parsers/index.html', data)



def add_authors_from_file(request):
    file = staticfiles_storage.path('parsers/chitai_gorod.csv')
    df = pd.read_csv(file)
    df.columns = ['book_url', 'name', 'author_name', 'genres', 'score', 'pages', 'description', 'cover_link']
    data = {}
    for index, row in df.iterrows():
        authors = row['author_name'].split(', ')
        for author in authors:
            author_name = author.strip()
            if not Authors.objects.filter(author_name=author_name).exists():
                author_obj = Authors(author_name=author_name)
                author_obj.save()

    data['info'] = 1
    return render(request, 'parsers/index.html', data)

def add_books_from_file(request):
    file = staticfiles_storage.path('parsers/chitai_gorod.csv')
    df = pd.read_csv(file)
    df.columns = ['book_link', 'book_name', 'author_name', 'genres', 'score', 'pages_count', 'description', 'pic_link']
    data = {}
    for index, row in df.iterrows():
        if not Books.objects.filter(book_name=row['book_name']).exists():
            books_obj = Books(book_link=row['book_link'],
                           score=row['score'],
                           pages_count=row['pages_count'],
                           description=row['description'],
                           pic_link=row['pic_link'],
                           book_name=row['book_name'],
                        )
            books_obj.save()
            authors = row['author_name'].split(', ')
            for author in authors:
                author_name = author.strip()
                author_id = Authors.objects.filter(author_name=author_name).values_list('id', flat=True).first()



    data['info'] = 1
    return render(request, 'parsers/index.html', data)





