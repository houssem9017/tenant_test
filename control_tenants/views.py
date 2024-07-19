import os

from django.shortcuts import render, redirect
from django_tenants.utils import schema_context

from control_tenants.models import Client, TenantForm, Domain
from dotenv import load_dotenv
load_dotenv()


def tenant_list(request):
    tenants = Client.objects.all().prefetch_related('domains')
    return render(request, 'tenant_list.html', {'tenants': tenants})


def create_tenant(request):
    if request.method == 'POST':
        form = TenantForm(request.POST)
        if form.is_valid():
            with schema_context('public'):
                # the domain should be unique, so we can use it to check if the tenant already exists
                domain = form.cleaned_data['domain']
                if Domain.objects.filter(domain=domain).exists():
                    form.add_error('domain', 'A tenant with this domain already exists.')
                    return render(request, 'create_tenant.html', {'form': form})
                # add .localhost to the domain to make it a valid domain
                form.cleaned_data['domain'] += '.'+os.getenv('DOMAIN_URL')
                print(os.getenv('DOMAIN_URL'))
                form.save()
            return redirect('tenant_list')
    else:
        form = TenantForm()
    return render(request, 'create_tenant.html', {'form': form})
