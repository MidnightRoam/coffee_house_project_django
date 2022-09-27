from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm

from .models import User


class UserLoginForm(AuthenticationForm):
    """User sign in form"""

    class Meta:
        model = User
        fields = ('username', 'password')
