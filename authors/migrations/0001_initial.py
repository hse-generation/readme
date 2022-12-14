# Generated by Django 4.1.3 on 2022-12-13 12:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Authors",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(max_length=20, null=True, verbose_name="Имя"),
                ),
                (
                    "last_name",
                    models.CharField(max_length=20, null=True, verbose_name="Фамилия"),
                ),
                (
                    "birthdate",
                    models.DateField(null=True, verbose_name="Дата рождения"),
                ),
                ("about_author", models.TextField(null=True, verbose_name="О себе")),
                (
                    "popular_books",
                    models.TextField(null=True, verbose_name="Популярные книги"),
                ),
                (
                    "profile_picture",
                    models.ImageField(blank=True, null=True, upload_to="images"),
                ),
            ],
            options={
                "verbose_name": "Автор",
                "verbose_name_plural": "Авторы",
                "db_table": "authors",
            },
        ),
    ]
