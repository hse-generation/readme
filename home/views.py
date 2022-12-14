import os

from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse_lazy, reverse
from books.models import Books


def index(request):
    data = {}
    data['books'] = Books.objects.all()[:10]
    return render(request, 'home/index.html', data)

