# contact/forms.py
from django import forms
from .models import ContactSubmission


class ContactForm(forms.Form):
    name = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    phone = forms.CharField(required=False)
    service_type = forms.ChoiceField(choices=ContactSubmission.SERVICE_CHOICES, required=True)
    used_before = forms.ChoiceField(choices=ContactSubmission.USED_BEFORE_CHOICES, required=True)
    message = forms.CharField(widget=forms.Textarea, required=True)
 #  reCAPTCHA verification handled manually as import continues to fail