from django import forms
from django.contrib.auth.hashers import check_password
from django.core.exceptions import ValidationError

from .models import UserToDo


class RegisterUserForm(forms.ModelForm):
    username = forms.CharField(label='Username', required=False, widget=forms.TextInput(attrs={'class': 'form-field'}))
    email = forms.EmailField(label='Email', required=False, widget=forms.EmailInput(attrs={'class': 'form-field'}))
    password = forms.CharField(label='Password', required=False, widget=forms.PasswordInput(attrs={'class': 'form-field'}))

    def clean_email(self):
        email = self.cleaned_data['email']
        if not email:
            raise ValidationError('Please, enter your email')
        if UserToDo.objects.filter(email=email).exists():
            raise ValidationError('Email already exists')
        return email

    def clean_username(self):
        username = self.cleaned_data['username']
        if not username:
            raise ValidationError('Please, enter your username')
        if UserToDo.objects.filter(username=username).exists():
            raise ValidationError('Username already exists')
        return username

    class Meta:
        model = UserToDo
        fields = ('username', 'email', 'password',)


class LoginUserForm(forms.Form):
    email = forms.CharField(label='Email', required=False, widget=forms.TextInput(attrs={'class': 'form-field'}))
    password = forms.CharField(label='Password', required=False, widget=forms.PasswordInput(attrs={'class': 'form-field'}))
    remember_me = forms.BooleanField(label='Remember me', required=False,
                                     widget=forms.CheckboxInput(attrs={'class': "check", 'type': "checkbox"}))
