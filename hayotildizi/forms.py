from django.forms import *

from .views import *
from .models import *
from django import forms

class ContactsForm(ModelForm):
    class Meta:
        model = Contact_us
        fields = "__all__"
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Name'}),
            'email': forms.TextInput(attrs={'placeholder': 'Email'}),
            'subject': forms.TextInput(attrs={'placeholder': 'Subject'}),
            'messages': forms.TextInput(attrs={'placeholder': 'Messages'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].label = ""
        self.fields['email'].label = ""
        self.fields['subject'].label = ""
        self.fields['messages'].label = ""


