from django.db import models
from books.models import Books
from genres.models import Genres
from account.models import Users


class FavoritesGenres(models.Model):
    account_id = models.ForeignKey(Users, on_delete=models.CASCADE)
    genre_id = models.ForeignKey(Genres, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.account_id)

    @classmethod
    def get_favorite_genres_by_account(cls, account_id):
        return Genres.objects.filter(favoritesgenres__account_id=account_id)

    class Meta:
        verbose_name = "Избранный жанр для пользователя"
        verbose_name_plural = "Избранные жанры для пользователя"
        db_table = "favorites_genres"
