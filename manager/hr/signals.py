from django.db import transaction
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model
from .models import Profile
from users.models import Activation
from users.views.activation import send_activation_email

AuthUserModel = get_user_model()

@receiver(pre_save, sender=AuthUserModel)
def inactivate_user(instance, **kwargs):
    if not instance.pk:
        instance.is_active = False
        instance.is_staff = True
        instance.password = None




# @receiver(post_save, sender=AuthUserModel)
# def create_profile(sender, instance, created, **kwargs):
#     print('Signal post_save was catched')
#     if created:
#         Profile(user=instance).save()

@receiver(post_save, sender=AuthUserModel)
def create_activation(instance, created, **kwargs):
    print('Signal post_save was caught in create_activation')
    try:
        with transaction.atomic():
            if created:
                Profile(user=instance).save()
                Activation(user=instance).save()
                send_activation_email(instance)
    except Exception:
        AuthUserModel.objects.get(pk=instance.id).delete()


