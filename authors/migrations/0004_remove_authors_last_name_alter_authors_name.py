# Generated by Django 4.1.3 on 2022-12-13 18:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        (
            "authors",
            "0003_remove_authors_about_author_remove_authors_birthdate_and_more",
        ),
    ]

    operations = [
        migrations.RemoveField(model_name="authors", name="last_name",),
        migrations.AlterField(
            model_name="authors",
            name="name",
            field=models.CharField(max_length=100, null=True, verbose_name="Имя"),
        ),
    ]