from django.db import models


# Create your models here.

class Books(models.Model):
    book_name = models.CharField("Название книги", null=True)
    author_name = models.CharField("Автор", null=True)
    genre = models.CharField("Жанр", null=True)
    score = models.IntegerField("Оценка", blank=True, null=True)
    pages_count = models.IntegerField("Количество страниц", blank=True, null=True)
    description = models.CharField("Описание", null=True)
    pic_link = models.URLField("Ссылка на картинку", null=True)
    book_link = models.URLField("Ссылка на книгу", null=True)

    def __str__(self):
        return self.book_name

    class Meta:
        verbose_name = "Книга"
        verbose_name_plural = "Книги"
        db_table = "books"
