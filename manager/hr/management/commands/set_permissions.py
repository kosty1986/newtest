from django.core.management import BaseCommand
from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Permission
from hr.models import Employer,Employee



AuthUserModel=get_user_model()

def get_permissions():
    generic_permissions = {'view', 'add', 'change', 'delete'}
    model_names = {Employer.__name__.lower(),Employee.__name__.lower()}

    permissions = set()
    for model_name in model_names:
        for generic_permission in generic_permissions:
            permissions.add(f'{generic_permission}_{model_name}')


    return permissions

class Command(BaseCommand):
    help = 'Give all the staff users the permissions to Employer and Employee models '

    def handle(self, *args, **options):
        try:
            employer_permissions = get_permissions()
            db_permissions = Permission.objects.filter(codename__in=employer_permissions)
            staff_users = AuthUserModel.objects.filter(is_superuser=False, is_staff=True).all()
            print('employer_permissions',employer_permissions)
            print('db_permissions',db_permissions)
            print('staff_users',staff_users)



            for user in staff_users:
                for db_permission in db_permissions:
                    user.user_permissions.add(db_permission)


        except BaseException as e:
            raise CommandError(e)