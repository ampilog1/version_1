from django.db import models


# Create your models here.
class Vacancy(models.Model):
    name = models.CharField(max_length=250)
    link = models.URLField(unique=True)
    address = models.CharField(max_length=250)
    salary = models.CharField(max_length=250)

    def __str__(self):
        return self.name
