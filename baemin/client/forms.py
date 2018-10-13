from django.forms import ModelForm
from .models import Client
from django import forms

class ClientForm(ModelForm):
    class Meta:
        model=Client
        fields=("name","contact","address","description",)
        widgets={
            "name":forms.TextInput(attrs={"class":"form-control"}),
            "contact":forms.TextInput(attrs={"class":"form-control"}),
            "address":forms.TextInput(attrs={"class":"form-control"}),
            "description":forms.Textarea(attrs={"class":"form-control"}),
        }
