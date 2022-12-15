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

