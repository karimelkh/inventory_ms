from django import forms
from .models import Supplier

class NewSupplForm(forms.ModelForm):
    class Meta():
        model = Supplier
        fields = [
                "id", "name", "desc",
                "email", "phone", "addr",
                "site", "is_active", "img"
            ]
        labels = {
            "id": "id",
            "name": "name",
            "desc": "description",
            "email": "email",
            "addr": "address",
            "phone": "phone",
            "site": "website",
            "is_active": "is active",
            "img": "supplier image"
        }
        help_texts = {}
        error_messages = {}

class UpdateSupplForm(forms.ModelForm):
    class Meta():
        model = Supplier
        fields = [
                "id", "name", "desc",
                "email", "phone", "addr",
                "site", "is_active", "img"
            ]
        labels = {
            "name": "name",
            "desc": "description",
            "email": "email",
            "addr": "address",
            "phone": "phone",
            "site": "website",
            "is_active": "is active",
            "img": "supplier image"
            }
        widgets = {
                "id": forms.HiddenInput(),
            }
        help_texts = {}
        error_messages = {}
