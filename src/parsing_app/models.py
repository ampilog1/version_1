from django.db import models

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
    adress = models.CharField(max_length=250, verbose_name='Адрес')
    salary = models.CharField(max_length=250, verbose_name='Зарплата')


    class Meta:
        verbose_name = 'Вакансия'
        verbose_name_plural = 'Вакансии'

    def __str__(self):
        return self.name

