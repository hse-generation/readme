from django.shortcuts import render, redirect
from authors.models import Authors
from books.models import Books


def index(request):
    data = {}
    data['authors'] = Authors.objects.all()
    return render(request, 'authors/index.html', data)


def get_author_books(request, author_id):
    data = {}
    data['books'] = Books.objects.filter(author_id__id=author_id).values()
    data['author'] = Authors.objects.filter(id=author_id).values()[0]['author_name']
    return render(request, 'authors/author-books.html', data)
