from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from users.models import CustomUser
# import base64


# Create your models here.
class Product(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=200)
    price = models.FloatField(max_length=10)
    stock = models.IntegerField()
    type = models.CharField(max_length=50, default="Hardware")
    description = models.TextField()
    avg_rating = models.FloatField(max_length=10, default=0.0)
    image = models.ImageField(default="default.jpg", upload_to="product-pics")
    # @classmethod
    # def create(cls,id,name,price,stock,type,description,avg_rating,image):
    #     product = cls(id=id,name=name,price=price,stock=stock,type=type,description=description,avg_rating=avg_rating,image=image)
    #     return product
    #
    # class Meta:
    #     db_table='home_product'

    # def encoded_id(self):
    #     return base64.b64encode(str(self.id))
    #
    # def decoded_id(self):
    #     return base64.b64decode(str(self.id))

# class Cart(models.Model):
#     user = models.ForeignKey(CustomUser, blank=True, on_delete='CASCADE')
#     count = models.PositiveIntegerField(default=0)
#     total = models.DecimalField(default=0, max_digits=10, decimal_places=2)
#
#     def __str__(self):
#         return "User: {} has {} items in their cart. Their total is ${}".format(self.user, self.count, self.total)
#
#
# class Entry(models.Model):
#     product = models.ForeignKey(Product, null=True, on_delete='CASCADE')
#     cart = models.ForeignKey(Cart, null=True, on_delete='CASCADE')
#
#     def __str__(self):
#         return "This entry contains {} {}(s).".format(self.quantity, self.product.name)
