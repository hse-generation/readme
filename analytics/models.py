from django.db import models
from django.db.models import Count, Min, Max, Avg
from django.utils import timezone

from accounts_books_statuses.models import AccountsBooksStatuses
from authors.models import Authors
from books.models import Books
from books_sources.models import BooksSources
from genres.models import Genres
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from django.db import models

from reviews.models import Reviews


class Analytics(models.Model):
    @classmethod
    def get_total_money_spend(cls, user_id):
        total_money_spend = \
            BooksSources.objects.filter(book__readbooks__account_id=user_id).aggregate(total=models.Sum('price'))[
                'total']
        return total_money_spend if total_money_spend else 0

    @classmethod
    def get_completed_books_count(cls, user_id):
        completed_books_count = AccountsBooksStatuses.objects.filter(account_id=user_id,
                                                                     status=AccountsBooksStatuses.COMPLETED).count()
        return completed_books_count

    @classmethod
    def get_books_in_progress_count(cls, user_id):
        books_in_progress_count = AccountsBooksStatuses.objects.filter(account_id=user_id,
                                                                       status=AccountsBooksStatuses.READING).count()
        return books_in_progress_count

    @classmethod
    def get_future_books_count(cls, user_id):
        future_books_count = AccountsBooksStatuses.objects.filter(account_id=user_id,
                                                                  status=AccountsBooksStatuses.TO_READ).count()
        return future_books_count

    @classmethod
    def get_total_pages_read_per_month(cls, user_id):
        current_month = timezone.now().month
        current_year = timezone.now().year

        total_pages_read = Books.objects.filter(
            accountsbooksstatuses__account_id=user_id,
            accountsbooksstatuses__status=AccountsBooksStatuses.COMPLETED,
            accountsbooksstatuses__updated_at__month=current_month,
            accountsbooksstatuses__updated_at__year=current_year
        ).aggregate(total=models.Sum('pages_count'))['total']

        return total_pages_read if total_pages_read else 0

    @classmethod
    def get_genre_statistics(cls, user_id):
        genre_statistics = Genres.objects.filter(books_genres__books_id__accountsbooksstatuses__account_id=user_id,
                                              books_genres__books_id__accountsbooksstatuses__status=AccountsBooksStatuses.COMPLETED).annotate(
            book_count=Count('books_genres__books_id')
        ).order_by('-book_count')

        return genre_statistics

    @classmethod
    def get_reviews_count(cls, user_id):
        return Reviews.objects.filter(account_id=user_id).count()

    @classmethod
    def get_min_score(cls, user_id):
        min_score = Reviews.objects.filter(account_id=user_id).aggregate(min_score=Min('score'))['min_score']
        return min_score

    @classmethod
    def get_max_score(cls, user_id):
        min_score = Reviews.objects.filter(account_id=user_id).aggregate(max_score=Max('score'))['max_score']
        return min_score

    @classmethod
    def get_med_score(cls, user_id):
        avg_score = Reviews.objects.filter(account_id=user_id).aggregate(avg_score=Avg('score'))['avg_score']
        return round(avg_score, 2)

