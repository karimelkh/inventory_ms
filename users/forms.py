from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class LoginForm(forms.Form):
    username = forms.CharField(label="username")
    password = forms.CharField(
        label="password", widget=forms.PasswordInput(attrs={"id": "password"})
    )


class NewUserForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ["username", "email", "password1", "password2"]
        labels = {}
        help_texts = {}
        error_messages = {}
