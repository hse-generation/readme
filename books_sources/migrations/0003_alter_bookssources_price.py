# Generated by Django 4.1.4 on 2023-05-23 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books_sources', '0002_bookssources_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookssources',
            name='price',
            field=models.IntegerField(default=362, verbose_name='Цена'),
        ),
    ]
