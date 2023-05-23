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

    class Meta:
        verbose_name = "Книга"
        verbose_name_plural = "Книги"
        db_table = "books"
