from django.db import models

# Create your models here.
class City(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, blank=True)

