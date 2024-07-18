from django.shortcuts import render, redirect
from .models import Product


home = lambda request: redirect('product_list')


product_list = lambda request: render(request, 'product_list.html', {'products': Product.objects.all()})


def create_product(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        price = request.POST.get('price')
        Product.objects.create(name=name, price=price)
        return redirect('product_list')
    return render(request, 'create_product.html')
