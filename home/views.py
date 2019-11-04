from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import Product
from django.contrib import messages


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


def searchMatch(query, product):
    query = query.lower()
    if query in product.description.lower() or query in product.name.lower() or query in product.type.lower():
        return True
    return False


def search(request):
    query = request.GET.get('search')
    allProducts = Product.objects.all()
    context = {
        'products': allProducts,
        'noofproducts': 0,
        'totalnoofproducts': len(allProducts)
    }
    if query:
        searchedproducts = [product for product in allProducts if searchMatch(query, product)]
        n = len(searchedproducts)
        context = {
            'products': searchedproducts,
            'noofproducts': n,
            'totalnoofproducts': len(allProducts)
        }
    else:
        messages.info(request, "No matching results found.", )
    return render(request, 'home/search.html', context)
