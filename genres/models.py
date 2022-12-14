from django.db import models

# Create your models here.

class Genres(models.Model):
    genre_name = models.CharField("Имя", max_length=100000, null=True)
    creat_date = models.DateField("Дата добавления", null=True)
    description = models.TextField("Описание", null=True)
    picture_link = models.TextField("Ссылка на картину", max_length=200, null=True)

    def __str__(self):
        return self.genre_name


    class Meta:
        verbose_name = "Жанр"
        verbose_name_plural = "Жанры"
        db_table = "genres"