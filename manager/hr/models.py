from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator

# from hr.management.commands.set_permissions import AuthUserModel

AuthUserModel = get_user_model()


class MyModel(models.Model):
    class Meta:
        abstract = True

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Employer(MyModel):
    class Meta:
        db_table = 'employers'

    name = models.CharField(max_length=255, unique=True, null=False)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=False, default=1)
    employees = models.ManyToManyField(settings.AUTH_USER_MODEL, through='Employee', related_name='employees')


    def get_employees_nr(self):
        return self.employees.count()

    get_employees_nr.short_description = 'Employees No.'

    def __str__(self):
        return self.name



class Employee(MyModel):
    class Meta:
        db_table = 'employees'

    employer = models.ForeignKey(Employer, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    wage = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        default=100.00,
        null=False,
        validators=[MinValueValidator(0.00)]
    )

    def first_name(self):
        return self.user.first_name

    first_name.short_description = 'First Name'
    first_name.order_field= 'user__first_name'

    def last_name(self):
        return self.user.last_name

    first_name.short_description = 'Last Name'
    first_name.order_field = 'user__last_name'

    def employer_name(self):
        return self.employer.name

    employer_name.short_description = 'Employer Name'
    employer_name.order_field = 'employer__name'

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name}'

class Profile(MyModel):
    class Meta:
        db_table = 'profiles'

    user = models.OneToOneField(AuthUserModel, on_delete=models.CASCADE)
    avatar =models.ImageField(upload_to='profiles', null=True, default=None)




