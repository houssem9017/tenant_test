from django.shortcuts import render, redirect
from .models import Product


def product_list(request):
    products = Product.objects.all()
    return render(request, 'product_list.html', {'products': products})


def create_product(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        price = request.POST.get('price')
        Product.objects.create(name=name, price=price)
        return redirect('product_list')
    return render(request, 'create_product.html')
