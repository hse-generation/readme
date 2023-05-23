from django.db import models
from account.models import Users
from books.models import Books


class Reviews(models.Model):
    account = models.ForeignKey(Users, on_delete=models.CASCADE)
    book = models.ForeignKey(Books, on_delete=models.CASCADE)
    score = models.IntegerField('Оценка', null=True)
    text = models.TextField("Отзыв", max_length=10000, null=True)
    days = models.IntegerField('Время прочтения в днях', null=True)

    def __str__(self):
        return str(self.account)

    @classmethod
    def create_new_review(cls, account_id, book_id, text, score, days):
        new_review = Reviews(account_id=account_id,
                             book_id=book_id,
                             text=text,
                             score=score,
                             days=days)
        new_review.save()

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'
        db_table = 'reviews'
