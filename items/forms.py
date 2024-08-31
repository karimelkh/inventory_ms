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
            "price",
            "currency",
            "img",
            "prod",
            "suppl",
            "site",
        ]
        labels = {
            "id": "id",
            "ttl": "title",
            "desc": "description",
            "qty": "stock",
            "price": "price",
            "currency": "currency",
            "img": "image",
            "prod": "product",
            "suppl": "supplier",
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
            "price",
            "currency",
            "img",
            "prod",
            "suppl",
            "site",
        ]
        labels = {
            "ttl": "title",
            "desc": "description",
            "qty": "stock",
            "price": "price",
            "currency": "currency",
            "img": "image",
            "prod": "product",
            "suppl": "supplier",
            "site": "site",
        }
        widgets = {
                "id": forms.HiddenInput(),
                }
        help_texts = {}
        error_messages = {}
