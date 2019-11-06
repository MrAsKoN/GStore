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


def updateProducts(request, item_id):
    context = {
        'product': Product.objects.get(pk=item_id)
    }
    return render(request, 'home/updateproduct.html', context)


def updatedone(request, item_id):
    if request.method == "POST":
        print("inside")
        prodForm = UpdateProductForm(request.POST)
        prd = get_object_or_404(Product, pk=item_id)
        productData = prodForm.data
        price = productData['price']
        stock = productData['stock']
        image = prd.image
        print(image)
        print(request.FILES)
        if 'productpic' in request.FILES:
            image = request.FILES['productpic']
        Product.objects.filter(pk=item_id).update(price=price, stock=stock, image=image)
    return render(request, 'users/adminhome.html')


def showProduct(request):
    context = {
        'products': Product.objects.all(),
    }
    return render(request, 'home/showProducts.html', context)


def deleteProduct(request, item_id):
    print(request.method)
    prpduct = get_object_or_404(Product,pk = item_id)
    context = {
        'product':prpduct
    }
    return render(request, 'home/deleteproduct.html',context)


def confDelete(request,item_id):
    if request.method=="POST":
        Product.objects.filter(pk=item_id).delete()
        messages.info(request,"Product deleted successfully")
    return render(request,"users/adminhome.html")
def showdeleteProduct(request):
    context = {
        'products': Product.objects.all(),
    }
    return render(request, 'home/viewProducts.html', context)