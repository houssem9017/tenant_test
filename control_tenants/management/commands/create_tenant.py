from django.core.management.base import BaseCommand
from control_tenants.models import Client, Domain


class Command(BaseCommand):
    help = 'Create a new tenant'

    def add_arguments(self, parser):
        parser.add_argument('schema_name', type=str)
        parser.add_argument('name', type=str)
        parser.add_argument('domain', type=str)

    def handle(self, *args, **options):
        schema_name = options['schema_name']
        name = options['name']
        domain = options['domain']

        tenant = Client(schema_name=schema_name, name=name)
        tenant.save()

        domain = Domain()
        domain.domain = domain
        domain.tenant = tenant
        domain.is_primary = True
        domain.save()

        self.stdout.write(self.style.SUCCESS(f'Successfully created tenant "{name}" with domain "{domain}"'))
