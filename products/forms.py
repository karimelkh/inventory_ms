from django import forms

from .models import Product


class NewProdForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
                "id",
                "ttl",
                "desc",
                "cat",
                "img",
                ]
        labels = {
                "id": "id",
                "ttl": "title",
                "desc": "description",
                "cat": "category",
                "img": "image",
                }
        widgets = {}
        help_texts = {}
        error_messages = {}


class UpdateProdForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
                "id",
                "ttl",
                "desc",
                "cat",
                "img",
                ]
        labels = {
                "ttl": "title",
                "desc": "description",
                "cat": "category",
                "img": "image",
                }
        widgets = {
                "id": forms.HiddenInput(),
                }
        help_texts = {}
        error_messages = {}
