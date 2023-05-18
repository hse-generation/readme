from django.db import models
from account.models import Users
from books.models import Books


class Reviews(models.Model):
    account = models.ForeignKey(Users, on_delete=models.CASCADE)
    book = models.ForeignKey(Books, on_delete=models.CASCADE)
    score = models.IntegerField('Оценка', null=True)

    def __str__(self):
        return str(self.account)

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'
        db_table = 'reviews'
