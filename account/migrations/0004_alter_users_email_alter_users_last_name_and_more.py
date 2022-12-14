# Generated by Django 4.1.3 on 2022-12-13 18:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("account", "0003_rename_profile_pic_users_profile_picture_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="users",
            name="email",
            field=models.EmailField(max_length=100, null=True, verbose_name="Почта"),
        ),
        migrations.AlterField(
            model_name="users",
            name="last_name",
            field=models.CharField(max_length=100, null=True, verbose_name="Фамилия"),
        ),
        migrations.AlterField(
            model_name="users",
            name="login",
            field=models.CharField(max_length=100, null=True, verbose_name="Логин"),
        ),
        migrations.AlterField(
            model_name="users",
            name="name",
            field=models.CharField(max_length=100, null=True, verbose_name="Имя"),
        ),
    ]