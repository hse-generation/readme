from django.shortcuts import render, redirect
from analytics.models import Analytics
from genres.models import Genres
from authors.models import Authors
import matplotlib.pyplot as plt
import seaborn as sns

def index(request):
    data = {}
    data['favoriteAuthor'] = Authors.get_favorite_author(request.session['user_id'])
    data['favoriteGenre'] = Genres.get_favorite_genre(request.session['user_id'])
    data['totalMoneySpent'] = Analytics.get_total_money_spend(request.session['user_id'])
    data['booksInProgressCount'] = Analytics.get_books_in_progress_count(request.session['user_id'])
    data['futureBooksCount'] = Analytics.get_future_books_count(request.session['user_id'])
    data['totalPagesReadPerMonth'] = Analytics.get_total_pages_read_per_month(request.session['user_id'])
    data['genreStatistics'] = Analytics.get_genre_statistics(request.session['user_id'])
    data['genre_names'] = []
    data['book_counts'] = []
    for genre in data['genreStatistics'][:3]:
        data['genre_names'].append(genre.genre_name)
        data['book_counts'].append(genre.book_count)

    data['reviewsCount'] = Analytics.get_reviews_count(request.session['user_id'])
    data['completedBooks'] = Analytics.get_completed_books_count(request.session['user_id'])
    data['minReviewScore'] = Analytics.get_min_score(request.session['user_id'])
    data['maxReviewScore'] = Analytics.get_max_score(request.session['user_id'])
    data['medReviewScore'] = Analytics.get_med_score(request.session['user_id'])
    return render(request, 'analytics/index.html', data)

