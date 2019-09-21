from django.shortcuts import render
from .models import Product
# Create your views here.
products = [
    {
        'name': 'RTX 2060 Super',
        'type': 'Graphic Card',
        'price': '37000',
    },
    {
        'name': 'RTX 2060',
        'type': 'Graphic Card',
        'price': '32000',
    },
    {
        'name': 'Samsung Evo 970 512GB NvMe SSD',
        'type': 'SSD',
        'price': '9000',
    }
]


def home(request):
    context = {
        'products': Product.objects.all()
    }
    return render(request, 'home/home.html', context)
