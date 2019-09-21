from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.FloatField(max_length=10)
    stock = models.IntegerField(max_length=10)
    date_added = models.DateTimeField(default=timezone.now)
    description = models.TextField()
