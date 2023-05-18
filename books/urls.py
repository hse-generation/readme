from django.urls import path

from . import views

urlpatterns = [
    path('view_book/<int:book_id>', views.view_book, name='view_book'),
]