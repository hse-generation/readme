from django.db import models
from authors.models import Authors
from genres.models import Genres

class Books(models.Model):
    book_name = models.CharField("Название книги",max_length=10000, null=True)
    score = models.FloatField("Оценка", blank=True, null=True)
    pages_count = models.IntegerField("Количество страниц", blank=True, null=True)
    description = models.TextField("Описание",max_length=10000, null=True)
    pic_link = models.URLField("Ссылка на картинку", max_length=10000, null=True)
    book_link = models.URLField("Ссылка на книгу", max_length=10000, null=True)
    # author_id = models.ForeignKey(Authors, on_delete=models.CASCADE, null=True)
    # genre_id = models.ForeignKey(Genres, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.book_name

    class Meta:
        verbose_name = "Книга"
        verbose_name_plural = "Книги"
        db_table = "books"
