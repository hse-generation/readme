from django.db import models
from account.models import Users
from books.models import Books


class ReadBooks(models.Model):

    days = models.IntegerField("Количество дней")
    account = models.ForeignKey(Users, on_delete=models.CASCADE)
    book = models.ForeignKey(Books, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.account)

    @classmethod
    def create_new_read_book(cls, account_id, book_id, days):
        new_read_book = cls(account_id=account_id, book_id=book_id, days=days)
        new_read_book.save()


    class Meta:
        verbose_name = "Прочитанная книга"
        verbose_name_plural = "Прочитанные книги"
        db_table = "read_books"
