from django.db import models

# Create your models here.
class Authors(models.Model):
    author_name = models.CharField("Имя", null=True)
    author_pic = models.URLField("Ссылка на фото автора",  null=True)


    def __str__(self):
        return self.name


    class Meta:
        verbose_name = "Автор"
        verbose_name_plural = "Авторы"
        db_table = "authors"