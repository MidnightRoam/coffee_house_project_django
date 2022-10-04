from django import forms

from .models import Contact


class ContactForm(forms.ModelForm):
    """Newsletter email subscribe form"""
    class Meta:
        model = Contact
        fields = ("email", )
        widgets = {"email": forms.TextInput(attrs={
                "class": "contact__input",
                "placeholder": "enter your email",
                "label": ""
        })
        }
        labels = {
            "email": ""
        }
