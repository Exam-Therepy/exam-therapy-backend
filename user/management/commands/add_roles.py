from django.core.management.base import BaseCommand
from django.db.utils import IntegrityError
from user.models import Role


class Command(BaseCommand):
    help = 'Creates a specified role in the database'

    def add_arguments(self, parser):
        # Optional argument to pass a role name directly from the command line
        parser.add_argument('-n', '--name', type=str, help='Name of the role to create')

    def handle(self, *args, **options):
        role_name = options['name']
        if not role_name:
            # If no role name is provided through command line arguments, ask for it
            role_name = input('Please enter the role name to create: ').strip()

        if not role_name:
            self.stderr.write(self.style.ERROR('No role name provided. Exiting.'))
            return

        try:
            role, created = Role.objects.get_or_create(name=role_name)
            if created:
                self.stdout.write(self.style.SUCCESS(f'Successfully created the "{role_name}" role.'))
            else:
                self.stdout.write(self.style.WARNING(f'The "{role_name}" role already exists.'))
        except IntegrityError as e:
            self.stderr.write(self.style.ERROR(f'Error creating the "{role_name}" role: {str(e)}'))
