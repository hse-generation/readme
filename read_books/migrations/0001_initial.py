# Generated by Django 4.1.4 on 2023-05-21 12:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('books', '0003_remove_books_author_id_remove_books_genre_id'),
        ('account', '0017_users_is_onboarding_passed'),
    ]

    operations = [
        migrations.CreateModel(
            name='ReadBooks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('days', models.IntegerField(verbose_name='Количество дней')),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.users')),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='books.books')),
            ],
            options={
                'verbose_name': 'Прочитанная книга',
                'verbose_name_plural': 'Прочитанные книги',
                'db_table': 'read_books',
            },
        ),
    ]