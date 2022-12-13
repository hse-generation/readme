# Generated by Django 4.1.3 on 2022-12-13 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Books",
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
                    "book_name",
                    models.CharField(max_length=20, null=True, verbose_name="Имя"),
                ),
                (
                    "author_name",
                    models.CharField(max_length=20, null=True, verbose_name="Фамилия"),
                ),
                (
                    "genre",
                    models.CharField(max_length=20, null=True, verbose_name="Фамилия"),
                ),
                (
                    "score",
                    models.IntegerField(blank=True, null=True, verbose_name="Оценка"),
                ),
                (
                    "pages_count",
                    models.IntegerField(
                        blank=True, null=True, verbose_name="Колическтво страниц"
                    ),
                ),
                (
                    "description",
                    models.CharField(
                        max_length=1000, null=True, verbose_name="Описание"
                    ),
                ),
                (
                    "pic_link",
                    models.URLField(null=True, verbose_name="Ссылка на картинку"),
                ),
                (
                    "book_link",
                    models.URLField(null=True, verbose_name="Ссылка на книгу"),
                ),
            ],
            options={
                "verbose_name": "Книга",
                "verbose_name_plural": "Книги",
                "db_table": "books",
            },
        ),
    ]