from django.shortcuts import render
from .models import Product
# Create your views here.
def home(request):
    context = {
        'products': Product.objects.all()
    }
    return render(request, 'home/home.html', context)
