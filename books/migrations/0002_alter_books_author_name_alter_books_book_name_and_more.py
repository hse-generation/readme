# Generated by Django 4.1.3 on 2022-12-13 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("books", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="books",
            name="author_name",
            field=models.CharField(max_length=20, null=True, verbose_name="Автор"),
        ),
        migrations.AlterField(
            model_name="books",
            name="book_name",
            field=models.CharField(
                max_length=20, null=True, verbose_name="Название книги"
            ),
        ),
        migrations.AlterField(
            model_name="books",
            name="genre",
            field=models.CharField(max_length=20, null=True, verbose_name="Жанр"),
        ),
        migrations.AlterField(
            model_name="books",
            name="pages_count",
            field=models.IntegerField(
                blank=True, null=True, verbose_name="Количество страниц"
            ),
        ),
    ]
