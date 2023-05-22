# Generated by Django 4.1.4 on 2023-05-21 15:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('sections', '0001_initial'),
        ('books', '0003_remove_books_author_id_remove_books_genre_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='SectionsBooks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('books', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='books.books')),
                ('section', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sections.sections')),
            ],
            options={
                'verbose_name': 'Книга vs секция',
                'verbose_name_plural': 'Книги vs секции',
                'db_table': 'sections_books',
            },
        ),
    ]