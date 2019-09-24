from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.FloatField(max_length=10)
    stock = models.IntegerField()
    type = models.CharField(max_length=50, default="Hardware")
    description = models.TextField()
    avg_rating = models.FloatField(max_length=10, default=0.0)
    image = models.ImageField(default="default.jpg", upload_to="product-pics")
