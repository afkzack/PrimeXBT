from typing import Any
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django import forms
from phonenumber_field.formfields import PhoneNumberField
from phonenumber_field.widgets import PhoneNumberPrefixWidget
from django.core.validators import RegexValidator



class SignUpForm(UserCreationForm):

    phone_number = PhoneNumberField(widget=PhoneNumberPrefixWidget(initial='Us'))

    first_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'formInput',
        'type': 'text',
        'placeholder': 'FirstName',
    }))

    last_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'formInput',
        'type': 'text',
        'placeholder': 'LastName',
    }))

    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'class': 'formInput',
        'type': 'email',
        'placeholder': 'Enter Email',
    }))

    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'formInput',
        'type': 'password',
        'placeholder': 'Enter Password',
    }))

    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'formInput',
        'type': 'password',
        'placeholder': 'Enter Password',
    }))

    class Meta:
        model = User
        fields = ('phone_number', 'first_name', 'last_name', 'email', 'password1', 'password2')
