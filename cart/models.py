from django.db import models

# Create your models here.
from home.models import Product
from users.models import CustomUser


class OrderItem(models.Model):
    product = models.OneToOneField(Product, on_delete=models.SET_NULL, null=True)
    date_added = models.DateTimeField(auto_now=True)
    date_ordered = models.DateTimeField(null=True)
    quantity=models.IntegerField(null=False,default=1)
    #totalPrice = models.IntegerField()

    def __str__(self):
        return self.product.name


class Order(models.Model):
    ref_code = models.CharField(max_length=15)
    owner = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True)
    is_ordered = models.BooleanField(default=False)
    items = models.ManyToManyField(OrderItem)
    date_ordered = models.DateTimeField(auto_now=True)

    def get_cart_items(self):
        return self.items.all()

    def get_cart_total(self):
        return sum([item.product.price*item.quantity for item in self.items.all()])

    def __str__(self):
        return '{0} - {1}'.format(self.owner, self.ref_code)
