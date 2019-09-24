from django.shortcuts import render
from .models import Product


# Create your views here.
def home(request):
    context = {
        'products': Product.objects.all()
    }
    return render(request, 'home/home.html', context)


def products(request, id):
    product = Product.objects.get(id=id)
    context = {
        'title': 'Product Details',
        'product': product
    }
    return render(request, 'home/product.html', context)
