from django.db import models
from books.models import Books
from sections.models import Sections


class SectionsBooks(models.Model):
    books = models.ForeignKey(Books, on_delete=models.CASCADE)
    section = models.ForeignKey(Sections, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.books_id)

    @classmethod
    def get_books_by_section(cls, section_id):
        return cls.objects.filter(section_id=section_id).values_list('books', flat=True)

    class Meta:
        verbose_name = "Книга vs секция"
        verbose_name_plural = "Книги vs секции"
        db_table = "sections_books"
