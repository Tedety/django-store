from django.shortcuts import render
from products.models import Product, ProductCategory


def index(requset):
    return render(requset, 'products/index.html')


def products(requset):
    context = {
        'products': Product.objects.all(),
        'categories': ProductCategory.objects.all(),
    }
    return render(requset, 'products/products.html', context)
