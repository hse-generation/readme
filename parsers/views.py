import os
import random

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
    file = staticfiles_storage.path('parsers/gorod.csv')
    df = pd.read_csv(file)
    df.columns = ['book_link', 'book_name', 'author_name', 'genres', 'score', 'pages_count', 'price', 'description',
                  'pic_link', 'review']
    data = {}
    users = Users.objects.all()
    for index, row in df.iterrows():
        if not Books.objects.filter(book_name=row['book_name']).exists():
            books_obj = Books(book_link=row['book_link'],
                              score=row['score'],
                              pages_count=row['pages_count'],
                              description=row['description'],
                              pic_link=row['pic_link'],
                              book_name=row['book_name'],
                              price=row['price'],
                              )
            books_obj.save()
            authors = row['author_name'].split(',')
            for author in authors:
                author_name = author.strip()
                author_instance = Authors.objects.filter(author_name=author_name).first()

                if author_instance:
                    books_authors_obj = Books_authors(author_id_id=author_instance.id, books_id_id=books_obj.id)
                    books_authors_obj.save()

            genres = row['genres'].split('.')
            for genre in genres:
                genre_name = genre.strip()
                genre_instance = Genres.objects.filter(genre_name=genre_name).first()
                if genre_instance:
                    books_genres_obj = Books_genres(genre_id_id=genre_instance.id, books_id_id=books_obj.id)
                    books_genres_obj.save()

            if row['review']:
                random_user = random.choice(users)
                random_user_id = random_user.id
                Reviews.create_new_review(random_user_id, books_obj.id, row['review'], random.randint(3, 5),
                                          random.randint(20, 50))

    data['info'] = 1
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
