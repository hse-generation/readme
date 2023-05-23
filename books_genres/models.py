from django.db import models
from books.models import Books
from genres.models import Genres


# Create your models here.

class Books_genres(models.Model):
    books_id = models.ForeignKey(Books, on_delete=models.CASCADE)
    genre_id = models.ForeignKey(Genres, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.books_id)

    class Meta:
        verbose_name = "Жанры книг"
        verbose_name_plural = "Жанры книг"
        db_table = "books_genres"
