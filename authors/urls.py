from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='authors'),
    path('<int:author_id>', views.get_author_books, name='author_books'),
]