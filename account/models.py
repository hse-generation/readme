from django.db import models

class Users(models.Model):
    name = models.CharField("Имя", max_length=10000, null=True, default="Книгоман")
    last_name = models.CharField("Фамилия",max_length=10000, null=True)
    birthdate = models.IntegerField("Год рождения", null=True)
    status = models.IntegerField("Статус активности", null=True, default=1)
    password = models.CharField("Пароль",max_length=10000, null=True)
    about = models.TextField("О себе",max_length=10000, null=True)
    email = models.EmailField("Почта", max_length=10000, null=True)
    profile_picture = models.ImageField(upload_to='avatars', null=True, blank=True, default="avatars/avatar.jpg")

    # github_link = models.CharField("Ccылка на github", max_length=200, null=True)
    # telegram = models.CharField("Ник в телеграм", max_length=200, null=True)
    # phone_number = models.CharField("Номер телефона", max_length=15, null=True)
    # specialization = models.CharField("Специализация", max_length=200, null=True)


    def __str__(self):
        return self.name


    class Meta:
        verbose_name = "Аккаунт"
        verbose_name_plural = "Аккаунты"
        db_table = "accounts"
