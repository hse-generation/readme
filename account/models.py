from django.db import models


class Users(models.Model):
    name = models.CharField("Имя", max_length=10000, null=True, default="Книгоман")
    last_name = models.CharField("Фамилия", max_length=10000, null=True)
    birthdate = models.IntegerField("Год рождения", null=True)
    status = models.IntegerField("Статус активности", null=True, default=1)
    pages_per_day = models.IntegerField("Количество страниц в день", null=True, default=10)
    password = models.CharField("Пароль", max_length=10000, null=True)
    about = models.TextField("О себе", max_length=10000, null=True)
    email = models.EmailField("Почта", max_length=10000, null=True)
    profile_picture = models.ImageField(upload_to='avatars', null=True, blank=True, default="avatars/avatar.jpg")
    is_onboarding_passed = models.IntegerField("Онбординг пройден?", default=0)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Аккаунт"
        verbose_name_plural = "Аккаунты"
        db_table = "accounts"
