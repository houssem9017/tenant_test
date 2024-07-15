from django.urls import path
from .views import product_list, create_product

urlpatterns = [
    path('products/', product_list, name='product_list'),
    path('products/create/', create_product, name='create_product')
]
