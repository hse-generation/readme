from django.db import models
from django.db.models import Count


# Create your models here.
class Authors(models.Model):
    author_name = models.CharField("Имя", max_length=10000, null=True)
    author_pic = models.URLField("Ссылка на фото автора", max_length=10000, null=True)
    author_description = models.TextField("Коротко об авторе", null=True)

    @classmethod
    def get_favorite_author(cls, user_id):
        # Get the count of books read by each author for the given user
        author_counts = cls.objects.filter(author_books__books_id__readbooks__account_id=user_id).annotate(
            book_count=Count('author_books__books_id')
        )

        # Sort the authors by the book count in descending order
        sorted_authors = author_counts.order_by('-book_count')

        # Get the favorite author (author with the highest book count)
        favorite_author = sorted_authors.first()

        return favorite_author


    def __str__(self):
        return self.author_name

    class Meta:
        verbose_name = "Автор"
        verbose_name_plural = "Авторы"
        db_table = "authors"
