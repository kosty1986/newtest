from django.contrib.auth import get_user_model
from django.core.serializers import register_serializer
from django.shortcuts import render, redirect, reverse
from .forms import UserImageForm, RegisterForm
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template

from rest_framework import viewsets
from rest_framework.response import Response
from hr.serializers import RegisterSerializer

AuthUserModel = get_user_model()


def home_page(request):
    print('A fost accesat homepage')
    return render(request, 'homepage.html', {
        'name': 'John',
        'greetings': 'Welcome to our first dinamic website!'
    })

def contact_page(request):
    print('A fost accesat contact_page')
    return render(request, 'contactpage.html', {
        'name': 'John',
        'email': 'john.deere@gmail.com',
        'phone': '+40 744 555 666',
    })

def upload_page(request):
    if request.method == 'GET':
        form = UserImageForm()
    else:
        form = UserImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()

            return redirect(reverse('home'))


    print('A fost accesat upload_page')
    return render(request, 'uploadpage.html', {
        'form':form
    })

def send_email_page(request):
    context = {
        'first_name': 'John',
        'last_name': 'McDonald',
        'company': 'Google Inc.'
    }
    template = get_template('email/email_template.html')
    content = template.render(context)
    mail = EmailMultiAlternatives(
        subject='Your Account has been registered',
        body=content,
        to=['kosty1986@yahoo.com']
    )
    mail.content_subtype = 'html'
    mail.send()

    return redirect(reverse('home'))

# def register_page(request):
#     if request.method == 'GET':
#         form = RegisterForm()
#     else:
#         form = RegisterForm(request.POST)
#         if form.is_valid():
#             form.save()
#
#             return redirect(reverse('home'))
#     return render(request, 'register.html', {
#         'form':form
#     })

class RegisterViewSet(viewsets.ViewSet):
    @staticmethod
    def create(request):
        register_serializer = RegisterSerializer(data=request.POST)

        if register_serializer.is_valid():
            register_serializer.create(register_serializer.validated_data)
            content = {
                'message': 'User was successfully created!!'
            }
            return Response(content, status=200)

        return Response(register_serializer.errors, status=400)

    @staticmethod
    def list(request):
        all_users =AuthUserModel.objects.all()
        register_serializer = RegisterSerializer(all_users, many=True)

        content = {
                'users': register_serializer.data
            }

        return Response(content, status=200)