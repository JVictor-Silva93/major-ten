from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True, help_text="We'll never share your email.")

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2',]


class LoginForm(AuthenticationForm):
    remember_me = forms.BooleanField(required=False, initial=False)

