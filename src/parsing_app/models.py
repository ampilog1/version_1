from django.db import models

# Create your models here.
class City(models.Model):
    name = models.CharField(max_length=50, verbose_name='город')
    slug = models.SlugField(max_length=50, blank=True)

    class Meta:
        verbose_name = 'город'
        verbose_name_plural = 'города'

    def __str__(self):
        return self.name

