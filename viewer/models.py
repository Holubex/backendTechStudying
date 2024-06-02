from django.db import models
from django.db.models import Model, DO_NOTHING


# Create your models here.


class Genre(Model):
    name = models.CharField(max_length=20)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

class Country(Model):
    name = models.CharField(max_length=50)

    class Meta:
        ordering = ['name']
        verbose_name_plural = 'Countries'

    def __str__(self):
        return self.name


class Creator(Model):
    name = models.CharField(max_length=100)
    birth_date = models.DateField()
    death_date = models.DateField(null=True, blank=True)
    biography = models.TextField()

    class Meta:
        ordering = ['name']
        verbose_name_plural = 'Actors'

    def __str__(self):
        return self.name


class Movie(Model):
    title = models.CharField(max_length=64)
    # genre = models.ForeignKey(Genre, on_delete=DO_NOTHING)
    genre = models.ManyToManyField(Genre, blank=True, related_name='movies')
    country = models.ManyToManyField(Country, blank=True, related_name='movies')
    actors = models.ManyToManyField(Creator, blank=True, related_name='movies')
    directors = models.ManyToManyField(Creator, blank=True, related_name='movie')
    rating = models.IntegerField()
    released = models.DateField()
    description = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['title', 'released']

    def __str__(self):
        return f'{self.title} ({self.released.year})'

