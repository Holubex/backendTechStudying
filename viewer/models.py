from django.db import models
from django.db.models import Model
# Create your models here.


class Genre(Model):
    name = models.CharField(max_length=20)