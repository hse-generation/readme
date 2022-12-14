from django.db import models

# Create your models here.

class Genres(models.Model):
    genre_name = models.CharField("Имя", max_length=100000, null=True)
    creat_date = models.DateField("Дата добавления", null=True)
    # github_link = models.CharField("Ccылка на github", max_length=200, null=True)
    # telegram = models.CharField("Ник в телеграм", max_length=200, null=True)
    # phone_number = models.CharField("Номер телефона", max_length=15, null=True)
    # specialization = models.CharField("Специализация", max_length=200, null=True)


    def __str__(self):
        return self.genre_name


    class Meta:
        verbose_name = "Жанр"
        verbose_name_plural = "Жанры"
        db_table = "genres"