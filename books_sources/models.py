import random

from django.db import models
from books.models import Books
from sources.models import Sources


class BooksSources(models.Model):
    book = models.ForeignKey(Books, on_delete=models.CASCADE)
    source = models.ForeignKey(Sources, on_delete=models.CASCADE)
    pic_link = models.URLField("Ссылка на картинку", max_length=10000, null=True)
    book_link = models.URLField("Ссылка на книгу", max_length=10000, null=True)
    price = models.IntegerField("Цена", default=random.choice(range(300, 800)))

    def __str__(self):
        return str(self.books_id)

    class Meta:
        verbose_name = "Источник книг"
        verbose_name_plural = "Источники книг"
        db_table = "books_sources"
