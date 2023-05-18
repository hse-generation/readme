# Generated by Django 4.1.4 on 2023-05-18 10:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('account', '0017_users_is_onboarding_passed'),
        ('books', '0003_remove_books_author_id_remove_books_genre_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='AccountsBooksStatuses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.IntegerField(verbose_name='Cтатус')),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.users')),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='books.books')),
            ],
            options={
                'verbose_name': 'Статус книги для пользователя',
                'verbose_name_plural': 'Статусы книг для пользователей',
                'db_table': 'accounts_books_statuses',
            },
        ),
    ]