from django.db import models
from authors.models import Authors
from books.models import Books
from account.models import Users


class AccountsBooksStatuses(models.Model):
    READING = 1
    TO_READ = 2
    COMPLETED = 3

    ACCOUNTS_BOOKS_STATUSES = {
        READING: 'Читаю',
        TO_READ: 'Буду читать',
        COMPLETED: 'Завершенные'
    }

    STATUSES_BUTTON = {
        READING: 'primary',
        TO_READ: 'info',
        COMPLETED: 'success'
    }

    book = models.ForeignKey(Books, on_delete=models.CASCADE)
    account = models.ForeignKey(Users, on_delete=models.CASCADE)
    status = models.IntegerField('Cтатус')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.book)

    class Meta:
        verbose_name = "Статус книги для пользователя"
        verbose_name_plural = "Статусы книг для пользователей"
        db_table = "accounts_books_statuses"
