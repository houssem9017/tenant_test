from django.urls import path
from .views import *

urlpatterns = [
    path('tenants/', tenant_list, name='tenant_list'),
    path('create-tenant/', create_tenant, name='create_tenant'),
]
