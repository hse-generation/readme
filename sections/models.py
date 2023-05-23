from django.db import models
from sklearn.neighbors import NearestNeighbors
import numpy as np
from account.models import Users
from authors.models import Authors
from books.models import Books
from books_authors.models import Books_authors
from books_genres.models import Books_genres
from favorite_genres.models import FavoritesGenres
from genres.models import Genres
from read_books.models import ReadBooks
from reviews.models import Reviews
from accounts_books_statuses.models import AccountsBooksStatuses

class Sections(models.Model):
    name = models.CharField("Название подборки", max_length=10000, null=True)
    status = models.IntegerField("Статус активности", null=False, default=1)

    def __str__(self):
        return self.name

    @classmethod
    def get_book_recommendations(cls, user_id):
        # Get the user's read books.
        read_books = ReadBooks.objects.filter(account_id=user_id)

        # If the user does not have any read books, return all books sorted by rating.
        if not read_books:
            return Books.objects.all()[:300]
        else:
            # Get the user's favorite genres.
            favorite_genres = FavoritesGenres.get_favorite_genres_by_account(user_id)

            # Get all books.
            books = Books.objects.all()

            # Get the book IDs of the user's read books.
            read_book_ids = ReadBooks.objects.filter(account_id=user_id).values_list('book_id', flat=True)

            # Filter the books to exclude the ones that the user has already read.
            filtered_books = books.exclude(id__in=read_book_ids)

            # Create a numerical representation for book features.
            book_features = []
            book_ids = []
            for book in filtered_books:
                feature = [
                    book.pages_count,
                    len(book.books_genres_set.all()),
                    len(book.book_authors.all()),
                    book.score,
                ]
                book_features.append(feature)
                book_ids.append(book.id)

            # Create a machine learning model to recommend books.
            model = NearestNeighbors()
            model.fit(np.array(book_features))

            # Get the nearest neighbors to the user's read books.
            user_read_books_features = []
            for read_book in read_books:
                feature = [
                    read_book.book.pages_count,
                    len(read_book.book.books_genres_set.all()),
                    len(read_book.book.book_authors.all()),
                    read_book.book.score,
                ]
                user_read_books_features.append(feature)
            nearest_neighbors = model.kneighbors(np.array(user_read_books_features), n_neighbors=5,
                                                 return_distance=False)

            # Get the book IDs of the nearest neighbors.
            nearest_book_ids = [book_ids[neighbor] for neighbor in nearest_neighbors.flatten()]

            # Get the books that are recommended to the user.
            recommended_books = books.filter(id__in=nearest_book_ids)[:300]

            # Sort the recommended books by score.
            # recommended_books = sorted(recommended_books, key=lambda book: book.score, reverse=True)

            return recommended_books

    class Meta:
        verbose_name = "Подборка"
        verbose_name_plural = "Подборки"
        db_table = "sections"
