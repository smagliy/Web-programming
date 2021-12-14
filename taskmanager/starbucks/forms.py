from .models import Registration
from django.forms import ModelForm, TextInput


class RegistrationForm(ModelForm):
    class Meta:
        model = Registration
        fields = ['username', 'product']

        widgets = {
            "username": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Username'
            }),
            "product": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Product'
            }),
        }
