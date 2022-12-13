# Generated by Django 4.1.3 on 2022-12-13 12:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Users",
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
                    "genre_name",
                    models.CharField(max_length=20, null=True, verbose_name="Имя"),
                ),
                (
                    "adding_date",
                    models.DateField(null=True, verbose_name="Дата добавления"),
                ),
            ],
            options={
                "verbose_name": "Жанр",
                "verbose_name_plural": "Жанры",
                "db_table": "genres",
            },
        ),
    ]
