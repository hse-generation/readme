import os

from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse_lazy, reverse



def index(request):
    # return render(request, 'users/register.html', data)
    return render(request, 'home/index.html')

