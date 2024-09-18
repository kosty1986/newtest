from cProfile import label

from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import password_validators_help_text_html, validate_password
from .utils import store_uploaded_file

AuthUser = get_user_model()

class UserImageForm(forms.Form):
    image = forms.ImageField(label='Image to upload', required=True)

    def save(self):
        image = self.cleaned_data.get('image')
        store_uploaded_file(image)

# class RegisterForm(forms.Form):
#     first_name = forms.CharField(label='First Name', max_length=255, required=True)
#     last_name = forms.CharField(label='Last Name', max_length=255, required=True)
#     email = forms.EmailField(label='Email address', required=True)
#     password = forms.CharField(
#         label='Password',
#         widget=forms.PasswordInput,
#         required=True,
#         help_text=password_validators_help_text_html
#     )
#     password_confirmation = forms.CharField(
#         label='Password',
#         widget=forms.PasswordInput,
#         required=True,
#         help_text='Please confirm your password'
#     )
#
#     def clean_email(self):
#         email = self.cleaned_data.get('email')
#
#         try:
#             AuthUser.objects.get(email=email)
#         except AuthUser.DoesNotExist:
#             return email
#         else:
#             raise forms.ValidationError('Email is already taken!')
#
#     def clean_password(self):
#         first_name = self.cleaned_data.get('first_name')
#         last_name = self.cleaned_data.get('last_name')
#         email = self.cleaned_data.get('email')
#         password = self.cleaned_data.get('password')
#
#         user = AuthUser(
#             first_name=first_name,
#             last_name=last_name,
#             email=email
#         )
#
#         validate_password(password, user)
#
#         return password
#
#     def clean_password_confirmation(self):
#         password = self.cleaned_data.get('password')
#         password_confirmation = self.cleaned_data.get('password_confirmation')
#
#         if password != password_confirmation:
#             raise forms.ValidationError('Password not confirmed!')
#
#         return password_confirmation
#
#     def save(self):
#         first_name = self.cleaned_data.get('first_name')
#         last_name = self.cleaned_data.get('last_name')
#         email = self.cleaned_data.get('email')
#         password = self.cleaned_data.get('password')
#
#         user = AuthUser.objects.create_user(
            # username=first_name + '.' + last_name,
            # first_name=first_name,
            # last_name=last_name,
#             email=email,
#             password=password,
#         )
#
#         return user

class RegisterForm(forms.ModelForm):
    class Meta:
        model = AuthUser
        fields = ['first_name', 'last_name', 'email', 'password']

    password = forms.CharField(
            label='Password',
            widget=forms.PasswordInput,
            required=True,
            help_text=password_validators_help_text_html
        )
    password_confirmation = forms.CharField(
        label='Password Confirmation',
        widget=forms.PasswordInput,
        required=True,
        help_text='Please confirm your password'
    )

    def save(self, commit=True):
        password = self.cleaned_data.get('password')
        self.instance.set_password(password)

        return super().save(commit)