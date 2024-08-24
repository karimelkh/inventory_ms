from django import forms

from .models import Item


class NewItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = [
            "id",
            "ttl",
            "desc",
            "qty",
            "img",
            "prod",
            "suppl",
            "cat",
            "site",
        ]
        labels = {
            "id": "id",
            "ttl": "title",
            "desc": "description",
            "qty": "stock",
            "img": "image",
            "prod": "product",
            "suppl": "supplier",
            "cat": "category",
            "site": "site",
        }
        help_texts = {}
        error_messages = {}

class UpdateItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = [
            "id",
            "ttl",
            "desc",
            "qty",
            "img",
            "prod",
            "suppl",
            "cat",
            "site",
        ]
        labels = {
            "ttl": "title",
            "desc": "description",
            "qty": "stock",
            "img": "image",
            "prod": "product",
            "suppl": "supplier",
            "cat": "category",
            "site": "site",
        }
        widgets = {
                "id": forms.HiddenInput(),
                }
        help_texts = {}
        error_messages = {}
