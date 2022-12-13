from django.db import models

# Create your models here.
class Authors(models.Model):
    name = models.CharField("Имя", max_length=20, null=True)
    last_name = models.CharField("Фамилия", max_length=20, null=True)
    profile_picture = models.ImageField(upload_to='images', null=True, blank=True)


    def __str__(self):
        return self.name


    class Meta:
        verbose_name = "Автор"
        verbose_name_plural = "Авторы"
        db_table = "authors"