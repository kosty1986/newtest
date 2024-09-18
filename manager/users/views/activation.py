from lib2to3.fixes.fix_input import context
from re import template
from django.utils.decorators import decorator_from_middleware
from users.middlewares.activation_middleware import ActivationMiddleware
from django.contrib.sites.models import Site
from django.core.mail import EmailMultiAlternatives
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.template.loader import get_template
from users.forms import PasswordForm
from utils.constants import ACTIVATION_AVAILABILITY
from users.models import Activation,AVAILABILITY
from django.utils import timezone

def send_activation_email(user):
    domain = Site.objects.get_current().domain
    url = reverse('users:activation:activate', args=(user.activation.token,))
    activation_url = f'{domain}{url}'

    print('!!!activation url is', activation_url)

    context = {
        'first name': user.first_name,
        'last name': user.last_name,
        'activation_url': activation_url,
        'availability': ACTIVATION_AVAILABILITY
    }

    template = get_template('users/emails/activate.html')
    content = template.render(context)
    mail = EmailMultiAlternatives(
        subject='Your Account has been created',
        body=content,
        to=[user.email]

    )

    mail.content_subtype = 'html'
    mail.send()

@decorator_from_middleware
def activate_user(request, token):
    activation = get_object_or_404(Activation, token=token)
    user = activation.user

    if request.method == 'GET':
        form = PasswordForm(user)
    else:
        form = PasswordForm(user, request.POST)

        if form.is_valid():
            form.save()

            user.is_active = True
            user.save()

            activation.activated_at=timezone.now()
            activation.save()

            return redirect(reverse('home'))

    return render(request, 'users/activation/set_password.html', {
        'token':token,
        'form':form,
    })




@decorator_from_middleware(ActivationMiddleware)
def reset_token_view(request, token):
    if request.method == 'GET':
        return render(request,'users/activation/reset_token.html',{
            'token':token
        })

    activation =get_object_or_404(Activation,token=token)
    activation.expired_at =timezone.now() + timezone.timedelta(**AVAILABILITY)
    activation.save()
    send_activation_email(activation.user)

    return render(request, 'users/activation/reset_token_success.html',{
            'user':activation.user
        })
