from django.db import models
from accounts.models import DearUser


class Vacancy(models.Model):
    name = models.CharField(max_length=250, null=True, blank=True)
    link = models.URLField(unique=False, null=True, blank=True)
    address = models.CharField(max_length=250, null=True, blank=True)
    salary = models.CharField(max_length=250, null=True, blank=True)

    def __str__(self):
        return self.name
