# Generated by Django 4.1.4 on 2023-05-23 15:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0004_books_price'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='books',
            name='book_link',
        ),
        migrations.RemoveField(
            model_name='books',
            name='pic_link',
        ),
    ]
