from django import forms
from .models import Item

class NewItemForm(forms.ModelForm):
    class Meta():
        model = Item
        fields = [ "prod_id", "prod_title", "prod_desc", "stock", "img", "suppl", "cat", "locat" ]
        labels = {
            "prod_id": "id",
            "prod_title": "title",
            "prod_desc": "description",
            "stock": "stock",
            "img": "image",
            "suppl": "supplier",
            "cat": "category",
            "locat" : "site",
        }
        help_texts = {}
        error_messages = {}

class UpdateItemForm(forms.ModelForm):
    class Meta():
        model = Item
        fields = [ "prod_id", "prod_title", "prod_desc", "stock", "img", "suppl", "cat", "locat" ]
        labels = {
            "prod_id": "id",
            "prod_title": "title",
            "prod_desc": "description",
            "stock": "stock",
            "img": "image",
            "suppl": "supplier",
            "cat": "category",
            "locat" : "site",
        }
        help_texts = {}
        error_messages = {}

