from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('products/<int:id>/', views.products, name='product'),
    path('search/', views.search, name='search'),
    path('addProducts/', views.addProducts, name='addproducts'),
    path('about/', views.about, name='about')
]
