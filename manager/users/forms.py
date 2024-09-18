from cProfile import label

from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import password_validators_help_text_html, validate_password, password_changed
from django.contrib.auth.forms import UserCreationForm as BaseUserCreationForm
AuthUser = get_user_model()



class PasswordForm(forms.Form):

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
    def __init__(self, user, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.user = user

    def clean_password(self):
        password = self.cleaned_data.get('password')
        validate_password(password, self.user)

        return password

    def clean_password_confirmation(self):
        password = self.cleaned_data.get('password')
        password_confirmation = self.cleaned_data.get('password_confirmation')

        if password != password_confirmation:
            raise forms.ValidationError('Password not confirmed')

        return password_confirmation


    def save(self):
        password = self.cleaned_data.get('password')
        self.user.set_password(password)
        self.user.save()


        # return super().save(commit)

class UserCreationForm(BaseUserCreationForm):
    password1 = None
    password2 = None

    def clean_password2(self):
        pass
    def save(self, commit=True):
        self.cleaned_data['password1'] = UserCreationForm.password1
        self.cleaned_data['password2'] = UserCreationForm.password2

        user =super(BaseUserCreationForm, self).save(commit=False)
        if commit:
            user.save()
        return user
