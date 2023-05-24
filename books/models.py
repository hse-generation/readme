from django.db import models
from authors.models import Authors
from genres.models import Genres

class Books(models.Model):
    book_name = models.CharField("Название книги",max_length=10000, null=True)
    score = models.FloatField("Оценка", blank=True, null=True)
    pages_count = models.IntegerField("Количество страниц", blank=True, null=True)
    description = models.TextField("Описание",max_length=10000, null=True)
    price = models.IntegerField("Цена", blank=True, null=True)

    def __str__(self):
        return self.book_name

    @classmethod
    def search(cls, query):
        books = Books.objects.filter(book_name__icontains=query).values('book_name')
        authors = Authors.objects.filter(author_name__icontains=query).values('author_name')
        author_books = Books.objects.filter(book_authors__author_id__author_name__icontains=query).values('book_name')
        genres = Genres.objects.filter(genre_name__icontains=query).values('genre_name')

        # Фильтруем книги по жанру
        genre_books = Books.objects.filter(books_genres__genre_id__genre_name__icontains=query).values('book_name')

        # Если найдены книги по жанру, добавляем их в список books
        if genre_books.exists():
            books = books.union(genre_books)

        ans = list(books) + list(author_books) + list(genre_books)
        return ans


    class Meta:
        verbose_name = "Книга"
        verbose_name_plural = "Книги"
        db_table = "books"
