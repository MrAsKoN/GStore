from django.contrib import admin
from .models import Product, Entry, Cart
# Register your models here.


admin.site.register(Product)
admin.site.register(Cart)
admin.site.register(Entry)
