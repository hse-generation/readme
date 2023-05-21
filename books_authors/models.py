from django.db import models
from books.models import Books
from genres.models import Genres
from authors.models import Authors


class Books_authors(models.Model):
    books_id = models.ForeignKey(Books, on_delete=models.CASCADE, related_name='book_authors')
    author_id = models.ForeignKey(Authors, on_delete=models.CASCADE, related_name='author_books')

    def __str__(self):
        return str(self.books_id)

    class Meta:
        verbose_name = "Авторы книг"
        verbose_name_plural = "Авторы книг"
        db_table = "books_authors"
