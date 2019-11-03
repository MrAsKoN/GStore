from django.urls import path
from . import views

appname = 'cart'

urlpatterns = [
    path('displaycart', views.displaycart, name='displaycart'),
    path('addtocart/<item_id>', views.add_to_cart, name='addtocart'),
    path('deletefromcart/<item_id>', views.delete_from_cart, name='deletefromcart'),
]
