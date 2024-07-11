from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(label="username")
    password = forms.CharField(label="password", widget=forms.PasswordInput(attrs={"id":"password"}))

