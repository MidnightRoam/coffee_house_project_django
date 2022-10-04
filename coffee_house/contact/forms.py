from django import forms
from snowpenguin.django.recaptcha3.fields import ReCaptchaField

from .models import Contact


class ContactForm(forms.ModelForm):
    """Newsletter email subscribe form"""
    captcha = ReCaptchaField()

    class Meta:
        model = Contact
        fields = ("email", "captcha")
        widgets = {"email": forms.TextInput(attrs={
                "class": "contact__input",
                "placeholder": "enter your email",
                "label": ""
        })
        }
        labels = {
            "email": ""
        }
