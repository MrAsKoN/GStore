from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from .models import Product
from django.contrib import messages
from .forms import AddProductForm, UpdateProductForm
from .models import CustomUser


# Create your views here.
def home(request):
    context = {
        'products': Product.objects.all(),
    }
    return render(request, 'home/home.html', context)


def about(request):
    return render(request, 'home/about.html')


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


def addProducts(request):
    if request.method == "POST":
        productForm = AddProductForm(request.POST)
        productData = productForm.data
        productid = productData['productid']
        productname = productData['productname']
        price = productData['price']
        stock = productData['stock']
        productType = productData['producttype']
        description = productData['description']
        avgrating = productData['rating']
        image = "default.jpg"
        if len(Product.objects.filter(pk=productid)) > 0:
            messages.warning(request, "Product ID already exists")
            return redirect('adminhome')
        if 'productimg' in request.FILES:
            print("present")
            image = request.FILES['productimg']
            print(request.FILES['productimg'])

        product = Product.create(id=productid, name=productname, price=price, stock=stock, type=productType,
                                 description=description, avg_rating=avgrating, image=image)
        product.save()
        messages.info(request, "Product added successfully")
    return render(request, 'home/addProducts.html', {})


def updateProducts(request):
    if request.method == "POST":
        print("post")
        productForm = UpdateProductForm(request.POST)
        productData = productForm.data
        productid = productData['productid']
        product = get_object_or_404(Product, pk=productid)
        productname = productData['productname']
        price = productData['price']
        stock = productData['stock']
        productType = productData['producttype']
        description = productData['description']
        avgrating = productData['rating']
        image = "default.jpg"
        if len(Product.objects.filter(pk=productid)) > 0:
            if 'productimg' in request.FILES:
                print("present")
                image = request.FILES['productimg']
                print(request.FILES['productimg'])
                Product.objects.filter(pk=productid).update(name=productname, price=price, stock=stock,
                                                            type=productType,
                                                            description=description, avg_rating=avgrating,
                                                            image=image)
                context = {
                    'product': product
                }
                return render(request, 'users/adminhome.html', context)
        else:
            messages.warning(request, "No such Product found!")
    return redirect('updateproducts')
