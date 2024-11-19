from django import forms
from .models import Contact


class ContactForm(forms.ModelForm):
    class Meta: 
        model = Contact
        fields = ('profile_image','name', 'contact_number', 'email',)
