from django.db import models
from authors.models import Authors
from books.models import Books
from account.models import Users


class AccountsBooksStatuses(models.Model):
    TO_READ = 1
    READING = 2
    COMPLETED = 3

    ACCOUNTS_BOOKS_STATUSES = {
        TO_READ: 'Буду читать',
        READING: 'Читаю',
        COMPLETED: 'Завершенные'
    }

    ACCOUNTS_BOOKS_STATUSES_TEXT = {
        'TO_READ': ACCOUNTS_BOOKS_STATUSES[TO_READ],
        'READING': ACCOUNTS_BOOKS_STATUSES[READING],
        'COMPLETED': ACCOUNTS_BOOKS_STATUSES[COMPLETED],
    }

    ACCOUNTS_BOOKS_STATUSES_TEXT_TO_NUMBER = {
        'TO_READ': TO_READ,
        'READING': READING,
        'COMPLETED': COMPLETED,
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

    @classmethod
    def save_or_update_status(cls, account_id, book_id, status_number):
        accountBookStatus = cls.objects.filter(account_id=account_id, book_id=book_id).first()

        # Add or update the status if it exists
        if accountBookStatus:
            accountBookStatus.status = status_number
            accountBookStatus.save()
        else:
            newAccountBookStatus = cls(status=status_number, account_id=account_id, book_id=book_id)
            newAccountBookStatus.save()

    @classmethod
    def get_books_by_status(cls, account_id, status_id):
        return Books.objects.filter(accountsbooksstatuses__account_id=account_id,
                                    accountsbooksstatuses__status=status_id)

    class Meta:
        verbose_name = "Статус книги для пользователя"
        verbose_name_plural = "Статусы книг для пользователей"
        db_table = "accounts_books_statuses"
