# from django import forms
# from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
#
# from .models import Order
#
#
# class OrderForm(forms.ModelForm):
#     """Order form"""
#     first_name = forms.CharField(widget=forms.TextInput(attrs={
#         'id': 'name',
#         'placeholder': 'Enter your first name',
#         'value': '{{ user.first_name }}'
#     }))
#     last_name = forms.CharField(widget=forms.TextInput(attrs={
#         'id': 'surname',
#         'placeholder': 'Enter your last name',
#         'value': '{{ user.last_name }}'
#     }))
#     quantity = forms.IntegerField(widget=forms.NumberInput)
#     price = forms.DecimalField(widget=forms.TextInput)
#
#     class Meta:
#         model = Order
#         fields = ("user", "product", "quantity", "created_timestamp")
