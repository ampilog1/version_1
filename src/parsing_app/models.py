from django.db import models
from accouts.models import DearUser

# Create your models here.
class City(models.Model):
    name = models.CharField(max_length=50, verbose_name='город', unique=True)

    class Meta:
        verbose_name = 'город'
        verbose_name_plural = 'города'

    def __str__(self):
        return self.name


class Language(models.Model):
    name = models.CharField(max_length=50, verbose_name='Язык програмирования', unique=True)

    class Meta:
        verbose_name = 'Язык програмирования'
        verbose_name_plural = 'Языки програмирования'

    def __str__(self):
        return self.name


class Vacancy(models.Model):
    name = models.CharField(max_length=250, verbose_name='Наименование вакансии')
    link = models.URLField(unique=True, verbose_name='Описание вакансии')
    address = models.CharField(max_length=250, verbose_name='Адрес')
    salary = models.CharField(max_length=250, verbose_name='Зарплата')
    user = models.ForeignKey(DearUser, on_delete=models.CASCADE)


    class Meta:
        verbose_name = 'Вакансия'
        verbose_name_plural = 'Вакансии'

    def __str__(self):
        return self.name

