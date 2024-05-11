from django.db import models
from django.db.models import Model, DO_NOTHING


# Create your models here.


class Genre(Model):
    name = models.CharField(max_length=20)

class Movie(Model):
    title = models.CharField(max_length=64)
    genre = models.ForeignKey(Genre, on_delete=DO_NOTHING, null=True)
    rating = models.IntegerField()
    released = models.DateField()
    description = models.TextField()
    created = models.DateTimeField(auto_now_add=True)