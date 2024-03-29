# Generated by Django 4.1.4 on 2023-05-15 21:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('genres', '0004_remove_genres_creat_date')
    ]

    operations = [
        migrations.CreateModel(
            name='Books_genres',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('books_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='books.books')),
                ('genre_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='genres.genres')),
            ],
            options={
                'verbose_name': 'Жанры книг',
                'verbose_name_plural': 'Жанры книг',
                'db_table': 'books_genres',
            },
        ),
    ]
