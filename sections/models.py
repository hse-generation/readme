from django.db import models


class Sections(models.Model):
    name = models.CharField("Название подборки", max_length=10000, null=True)
    status = models.IntegerField("Статус активности", null=False, default=1)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Подборка"
        verbose_name_plural = "Подборки"
        db_table = "sections"
