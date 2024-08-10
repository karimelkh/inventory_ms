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
            "suppl",
            "cat",
            "site",
        ]
        labels = {
            "id": "article",
            "ttl": "title",
            "desc": "description",
            "qty": "stock",
            "img": "image",
            "suppl": "supplier",
            "cat": "category",
            "site": "site",
        }
        help_texts = {}
        error_messages = {}
