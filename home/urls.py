from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('products/<int:id>/', views.products, name='product'),
    path('search/', views.search, name='search'),
    path('addProducts/', views.addProducts, name='addproducts'),
    path('updateproducts/<item_id>', views.updateProducts, name='updateproducts'),
    path('updatedone/<item_id>', views.updatedone, name='updatedone'),
    path('showProducts/', views.showProduct, name='showProduct'),
    path('deleteProduct/<item_id>',views.deleteProduct,name='deleteProduct'),
    path('showdeleteProduct/', views.showdeleteProduct, name='showdeleteProduct'),
    path('confDelete/<item_id>',views.confDelete,name= 'confDelete'),
    path('about/', views.about, name='about')
]
