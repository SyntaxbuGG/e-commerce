from .models import Address, Company, User


from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.core.exceptions import ValidationError


class CustomUserCreationForm(UserCreationForm):
    address = forms.ModelChoiceField(queryset=Address.objects.all(),required=False)
    company = forms.ModelChoiceField(queryset=Company.objects.all(), required=False)
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2', 'address', 'company']

        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control',}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'password1': forms.PasswordInput(attrs={'class': 'form-control'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-control'}),
            'address': forms.TextInput(attrs={'class': 'form-control'}),
            'company': forms.TextInput(attrs={'class:': 'form-control'})

        }
