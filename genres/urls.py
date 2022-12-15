from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='genres'),
    path('<int:genre_id>', views.get_genre_books, name='genre_books'),

]