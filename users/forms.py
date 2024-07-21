from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class LoginForm(forms.Form):
    username = forms.CharField(label="username")
    password = forms.CharField(label="password", widget=forms.PasswordInput(attrs={"id":"password"}))


class NewUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = [ "username", "email", "password1", "password2" ] 
        labels = {}
        help_texts = {}
        error_messages = {}
