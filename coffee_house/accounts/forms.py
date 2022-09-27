from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm

from .models import User


class UserLoginForm(AuthenticationForm):
    """User sign in form"""
    username = forms.CharField(widget=forms.TextInput(attrs={
        "id": "email__signup",
        "placeholder": "Enter your username"
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        "id": "password__signup",
        "placeholder": "Enter your password"
    }))

    class Meta:
        model = User
        fields = ('username', 'password')

    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'shadow__input'


class UserRegistrationForm(UserCreationForm):
    """User sign up form"""
    first_name = forms.CharField(widget=forms.TextInput(attrs={
        "id": "name__signup",
        "placeholder": "First name",
    }))
    last_name = forms.CharField(widget=forms.TextInput(attrs={
        "id": "surname__signup",
        "placeholder": "Last name",
    }))
    username = forms.CharField(widget=forms.TextInput(attrs={
        "id": "username__signup",
        "placeholder": "Username",
    }))
    email = forms.CharField(widget=forms.EmailInput(attrs={
        "id": "email__signup",
        "placeholder": "Email",
    }))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        "id": "password__signup",
        "placeholder": "Enter your password",
    }))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        "id": "password2__signup",
        "placeholder": "Repeat your password",
    }))

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(UserRegistrationForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'shadow__input'
