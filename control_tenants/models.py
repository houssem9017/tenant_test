from django.db import models
from django.utils.text import slugify
from django_tenants.models import TenantMixin, DomainMixin
from django import forms


class Client(TenantMixin):
    name = models.CharField(max_length=100)
    paid_until = models.DateField(default='2099-12-05')
    on_trial = models.BooleanField(default=True)
    created_on = models.DateField(auto_now_add=True)

    # default true, schema will be automatically created and synced when it is saved
    auto_create_schema = True


class Domain(DomainMixin):
    tenant = models.ForeignKey(Client, related_name='domains', on_delete=models.CASCADE)


class TenantForm(forms.ModelForm):
    domain = forms.CharField(max_length=255, help_text="Domain for your website")

    class Meta:
        model = Client
        fields = ['name']

    def save(self, commit=True):
        tenant = super().save(commit=False)
        tenant.schema_name = slugify(tenant.name)
        if commit:
            tenant.save()
            Domain.objects.create(tenant=tenant, domain=self.cleaned_data['domain'], is_primary=True)
        return tenant
