from django.db import models

# Create your models here.

class Product(models.Model):
    title = models.CharField(max_length=280)
    images = models.CharField(max_length=280)
    likes = models.PositiveBigIntegerField(default=0)


class User(models.Model):
    pass