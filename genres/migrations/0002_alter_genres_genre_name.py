# Generated by Django 4.1.4 on 2022-12-14 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('genres', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='genres',
            name='genre_name',
            field=models.CharField(max_length=100000, null=True, verbose_name='Имя'),
        ),
    ]
