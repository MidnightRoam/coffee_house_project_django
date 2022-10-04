from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm

from .models import User


class UserLoginForm(AuthenticationForm):
    """User sign in form"""
    username = forms.CharField(widget=forms.TextInput(attrs={
        "id": "email__auth",
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
        'class': 'block'
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
        "id": "email__auth",
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


class UserProfileForm(UserChangeForm):
    """User profile change form"""
    username = forms.CharField(widget=forms.TextInput(attrs={
        'readonly': True,
        'id': 'username__profile'
    }))
    email = forms.CharField(widget=forms.EmailInput(attrs={
        'readonly': True,
        'id': 'email__input',
    }))
    image = forms.ImageField(widget=forms.FileInput(), required=False)
    first_name = forms.CharField(widget=forms.TextInput(attrs={
        'id': "profile__name",
        'placeholder': 'First name'
    }))
    last_name = forms.CharField(widget=forms.TextInput(attrs={
        'id': "profile__surname",
        'placeholder': 'Last name'
    }))
    age = forms.CharField(widget=forms.TextInput(attrs={
        'id': "age__input",
        'placeholder': 'Age',
    }), required=False)
    sex = forms.CharField(widget=forms.TextInput(attrs={
        'id': "sex__input",
        'placeholder': 'Sex'
    }), required=False)
    country = forms.CharField(widget=forms.TextInput(attrs={
        'id': "country__input",
        'placeholder': "Country"
    }), required=False)
    city = forms.CharField(widget=forms.TextInput(attrs={
        'id': "city__input",
        'placeholder': 'City'
    }), required=False)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'age', 'sex', 'country', 'city', 'image')

    def __init__(self, *args, **kwargs):
        super(UserProfileForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'profile-fields'
