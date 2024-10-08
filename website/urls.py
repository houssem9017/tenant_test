from django.urls import path
from .views import *

urlpatterns = [
    path("", home, name="home"),
    path('products/', product_list, name='product_list'),
    path('products/create/', create_product, name='create_product')
]
