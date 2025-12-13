from django.db import models

# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=50)
    release = models.DateField()
    completion = models.DateField()
    start = models.DateField()

class Game(models.Model):
    name = models.CharField(max_length=200)
    hours_played = models.IntegerField(default=0)
    release = models.DateField()
    completion = models.DateField()
    start = models.DateField()