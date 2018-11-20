from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class LoginForm(forms.Form):
    username = forms.CharField(widget = forms.TextInput(attrs = {'class' : 'form-control form-control-sm', 'placeholder' : 'Username'}), error_messages = {'required' : 'Please enter your username'})

    password = forms.CharField(widget = forms.PasswordInput(attrs = {'class' : 'form-control form-control-sm', 'placeholder' : 'Password'}), error_messages = {'required' : 'Please enter your password'})


class SignUpForm(UserCreationForm):
    username = forms.CharField(widget = forms.TextInput(attrs = {'class' : 'form-control form-control-sm', 'placeholder' : 'Username'}))

    email = forms.CharField(widget = forms.EmailInput(attrs = {'class' : 'form-control form-control-sm', 'placeholder' : 'E-mail'}))

    password1 = forms.CharField(widget = forms.PasswordInput(attrs = {'class' : 'form-control form-control-sm', 'placeholder' : 'Password'}))

    password2 = forms.CharField(widget = forms.PasswordInput(attrs = {'class' : 'form-control form-control-sm', 'placeholder' : 'Confirm Password'}))
