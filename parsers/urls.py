from django.urls import path

from . import views

urlpatterns = [

    path('', views.index, name='parsers'),
    path('add_genres_from_file/', views.add_genres_from_file, name='add_genres_from_file'),
    path('add_authors_from_file/', views.add_authors_from_file, name='add_authors_from_file'),
    path('add_books_from_file/', views.add_books_from_file, name='add_books_from_file'),
    path('generate_users/', views.generate_users, name='generate_users'),
    path('transfer_data_to_books_sources/', views.transfer_data_to_books_sources, name='transfer_data_to_books_sources'),
]