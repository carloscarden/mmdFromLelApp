from django.db import models

class Animal(models.Model):
    nombre = models.CharField(max_length=100)
    edad = models.IntegerField()
