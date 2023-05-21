from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('popup-genres/', views.popup_genres, name='popup_genres'),
]