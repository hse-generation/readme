import os
import random

from django.db import models
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse_lazy, reverse
from books.models import Books
from account.models import Users
from genres.models import Genres
from books_sources.models import BooksSources
from authors.models import Authors
from books_genres.models import Books_genres
from books_authors.models import Books_authors
import pandas as pd
from django.contrib.staticfiles.storage import staticfiles_storage
import logging
from django.db import models
from django.db.models import Count
from reviews.models import Reviews


def index(request):
    # df = pd.read_csv('/files/chitai_gorod.csv')
    # print(df)
    data = {}
    return render(request, 'parsers/index.html', data)


def add_genres_from_file(request):
    file = staticfiles_storage.path('parsers/chitai_gorod.csv')
    df = pd.read_csv(file)
    df.columns = ['book_url', 'name', 'author_name', 'genres', 'score', 'pages', 'description', 'cover_link']
    data = {}
    for index, row in df.iterrows():
        genres = row['genres'].split('.')
        for genre in genres:
            genre_name = genre.strip()
            if not Genres.objects.filter(genre_name=genre_name).exists():
                genre_obj = Genres(genre_name=genre_name)
                genre_obj.save()

    data['info'] = 1
    return render(request, 'parsers/index.html', data)


def add_authors_from_file(request):
    file = staticfiles_storage.path('parsers/chitai_gorod.csv')
    df = pd.read_csv(file)
    df.columns = ['book_url', 'name', 'author_name', 'genres', 'score', 'pages', 'description', 'cover_link']
    data = {}
    for index, row in df.iterrows():
        authors = row['author_name'].split(', ')
        for author in authors:
            author_name = author.strip()
            if not Authors.objects.filter(author_name=author_name).exists():
                author_obj = Authors(author_name=author_name)
                author_obj.save()

    data['info'] = 1
    return render(request, 'parsers/index.html', data)


def add_books_from_file(request):
    file = staticfiles_storage.path('parsers/book24.csv')
    df = pd.read_csv(file)
    df.columns = ['book_link', 'book_name', 'author_name', 'genres', 'score', 'pages_count', 'price', 'description',
                  'pic_link', 'review']
    data = {}
    users = Users.objects.all()
    res = 0
    for index, row in df.iterrows():
        # if not Books.objects.filter(book_name=row['book_name']).exists():
        #     if row['score'] is None or row['score'] == 0:
        #         row['score'] = random.randint(3, 5)
        #
        #     if not isinstance(row['pages_count'], (int, float)):
        #         continue
        #     if row['pages_count'] is None or row['pages_count'] == 0:
        #         row['pages_count'] = random.randint(320, 500)
        #
        #     row['score'] = row['score'].replace(',', '.')  # Replace comma with period
        #     row['score'] = float(row['score'])  # Convert the corrected value to a float
        #
        #     books_obj = Books(score=row['score'],
        #                       pages_count=row['pages_count'],
        #                       description=row['description'],
        #                       book_name=row['book_name'])
        #     books_obj.save()
        #
        #     authors = row['author_name'].split(', ')
        #     for author in authors:
        #         author_name = author.strip()
        #         author_instance = Authors.objects.filter(author_name=author_name).first()
        #
        #         if author_instance:
        #             books_authors_obj = Books_authors(author_id_id=author_instance.id, books_id_id=books_obj.id)
        #             books_authors_obj.save()
        #
        #     genres = row['genres'].split('.')
        #     for genre in genres:
        #         genre_name = genre.strip()
        #         genre_instance = Genres.objects.filter(genre_name=genre_name).first()
        #         if genre_instance:
        #             books_genres_obj = Books_genres(genre_id_id=genre_instance.id, books_id_id=books_obj.id)
        #             books_genres_obj.save()
        # else:
        #     res += 1

        # if row['pic_link'][0:2] == '//':
        #     row['pic_link'] = row['pic_link'][2:]

        books_obj = Books.objects.filter(book_name=row['book_name']).first()
        genres = row['genres'].split('.')
        if books_obj:
            for genre in genres:
                genre_name = genre.strip()
                genre_instance = Genres.objects.filter(genre_name=genre_name).first()
                if genre_instance:
                    books_genres_obj = Books_genres(genre_id_id=genre_instance.id, books_id_id=books_obj.id)
                    books_genres_obj.save()

        # books_sources = BooksSources(pic_link=row['pic_link'],
        #                              book_link=row['book_link'],
        #                              book_id=books_obj.id,
        #                              source_id=3,
        #                              price=row['price'])
        #
        # books_sources.save()
        # if row['review'] is not None and str(row['review']).strip() != '':
        #     reviews = str(row['review']).split(' , ')
        #     for review in reviews:
        #         if review.strip() != '':
        #             random_user = random.choice(users)
        #             random_user_id = random_user.id
        #             Reviews.create_new_review(random_user_id, books_obj.id, review, random.randint(3, 5),
        #                                       random.randint(20, 50))

    data['info'] = res
    return render(request, 'parsers/index.html', data)


def transfer_data_to_books_sources(request):
    books = Books.objects.filter(id__gte=1072)
    data = {}
    for book in books:
        books_sources = BooksSources(pic_link=book.pic_link,
                                     book_link=book.book_link,
                                     book_id=book.id,
                                     source_id=2,
                                     price=book.price)

        books_sources.save()

    data['info'] = 1
    return render(request, 'parsers/index.html', data)


def set_score(request):
    books_with_null_score = Books.objects.all()
    for book in books_with_null_score:
        book.score = round(book.score, 2)
        book.save()

    data = {}
    data['info'] = 1
    return render(request, 'parsers/index.html', data)


def delete_nan_reviews(request):
    Reviews.objects.filter(text="nan").delete()


def delete_uplicate(request):
    # Get the list of duplicate records based on your criteria
    duplicate_records = (
        Books_authors.objects.values('books_id_id', 'author_id_id')
        .annotate(count=Count('id'))
        .filter(count__gt=1)
    )

    # Iterate over the duplicate records and delete all except the first one
    for duplicate in duplicate_records:
        duplicate_instances = (
            Books_genres.objects
            .filter(books_id_id=duplicate['books_id_id'], genre_id_id=duplicate['author_id_id'])
            .order_by('id')
        )

        # Keep the first instance
        first_instance = duplicate_instances.first()

        # Delete the remaining instances
        duplicate_instances.exclude(pk=first_instance.pk).delete()

    data = {}
    return render(request, 'parsers/index.html', data)

def generate_users(request):
    names = ["Александр", "Алексей", "Анатолий", "Андрей", "Антон", "Артем", "Борис", "Вадим", "Валентин", "Валерий",
             "Василий", "Виктор", "Виталий", "Владимир", "Владислав", "Вячеслав", "Геннадий", "Георгий", "Григорий",
             "Даниил", "Денис", "Дмитрий", "Евгений", "Егор", "Иван", "Игорь", "Илья", "Кирилл", "Константин", "Леонид",
             "Максим", "Марк", "Матвей", "Михаил", "Никита", "Николай", "Олег", "Павел", "Петр", "Роман", "Руслан",
             "Семен", "Сергей", "Станислав", "Степан", "Тимофей", "Федор", "Юрий", "Ярослав", "Александра",
             "Александрина", "Алена", "Алина", "Алла", "Анастасия", "Ангелина", "Анжела", "Анжелика", "Анна",
             "Антонина", "Валентина", "Валерия", "Варвара", "Василиса", "Вера", "Вероника", "Виктория", "Галина",
             "Дарья", "Евгения", "Екатерина", "Елена", "Елизавета", "Жанна", "Зинаида", "Инна", "Ирина", "Карина",
             "Кира", "Кристина", "Лариса", "Лидия", "Любовь", "Маргарита", "Марина", "Мария", "Надежда", "Наталья",
             "Оксана", "Ольга", "Полина", "Светлана", "София", "Татьяна", "Ульяна", "Юлия", "Яна"]
    last_names = ["Иванов", "Смирнов", "Кузнецов", "Попов", "Соколов", "Лебедев", "Козлов", "Новиков", "Морозов",
                  "Петров", "Волков", "Соловьев", "Васильев", "Зайцев", "Павлов", "Семенов", "Голубев", "Виноградов",
                  "Богданов", "Воробьев", "Федоров", "Михайлов", "Беляев", "Тарасов", "Белов", "Комаров", "Орлов",
                  "Киселев", "Макаров", "Андреев", "Ковалев", "Ильин", "Гусев", "Титов", "Кузьмин", "Кудрявцев",
                  "Баранов", "Куликов", "Алексеев", "Степанов", "Яковлев", "Сорокин", "Сергеев", "Романов", "Захаров",
                  "Борисов", "Королев", "Герасимов", "Пономарев", "Григорьев", "Лазарев", "Медведев", "Ершов",
                  "Никитин", "Соболев", "Рябов", "Поляков", "Цветков", "Данилов", "Жуков", "Фролов", "Журавлев",
                  "Николаев", "Крылов", "Максимов", "Сидоров", "Осипов", "Белоусов", "Федотов", "Дорофеев", "Егоров",
                  "Матвеев", "Бобров", "Дмитриев", "Калинин", "Анисимов", "Петухов", "Антонов", "Тимофеев", "Никифоров",
                  "Веселов", "Филиппов", "Марков", "Большаков", "Суханов", "Миронов", "Ширяев", "Александров",
                  "Коновалов", "Шестаков", "Казаков", "Ефимов", "Денисов", "Громов", "Фомин", "Давыдов"]

    for i in range(len(names)):
        new_acc = Users(name=random.choice(names),
                        last_name=random.choice(last_names),
                        birthdate=random.randint(1990, 2010),
                        status=1,
                        pages_per_day=random.randint(20, 100),
                        )
        new_acc.save()

    data = {}
    return render(request, 'parsers/index.html', data)
