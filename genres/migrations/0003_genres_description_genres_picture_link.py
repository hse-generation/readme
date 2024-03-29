# Generated by Django 4.1.4 on 2022-12-14 19:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('genres', '0002_alter_genres_genre_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='genres',
            name='description',
            field=models.TextField(null=True, verbose_name='Описание'),
        ),
        migrations.AddField(
            model_name='genres',
            name='picture_link',
            field=models.TextField(max_length=200, null=True, verbose_name='Ссылка на картину'),
        ),
    ]
