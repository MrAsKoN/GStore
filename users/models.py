from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class CustomUser(models.Model):
    firstname = models.CharField(max_length=100,null=True)
    lastname = models.CharField(max_length=100,null=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(default='default.jpg', upload_to='profile-pics')
    address = models.TextField(max_length=300, null=True, blank=True)
    phoneno = models.IntegerField(null=True, blank=True)
    REQUIRED_FIELDS = ['user']
