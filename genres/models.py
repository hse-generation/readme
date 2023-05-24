from django.db import models
from django.db.models import Count


# Create your models here.

class Genres(models.Model):
    genre_name = models.CharField("Имя", max_length=100000, null=True)
    description = models.TextField("Описание", null=True)
    picture_link = models.TextField("Ссылка на картину", max_length=200, null=True)

    def __str__(self):
        return self.genre_name


    @classmethod
    def get_favorite_genre(cls, user_id):
        # Get the count of books in each genre read by the given user
        genre_counts = cls.objects.filter(books_genres__books_id__readbooks__account_id=user_id).annotate(
            book_count=Count('books_genres__books_id')
        )

        # Sort the genres by the book count in descending order
        sorted_genres = genre_counts.order_by('-book_count')

        # Get the favorite genre (genre with the highest book count)
        favorite_genre = sorted_genres.first()

        return favorite_genre


    class Meta:
        verbose_name = "Жанр"
        verbose_name_plural = "Жанры"
        db_table = "genres"