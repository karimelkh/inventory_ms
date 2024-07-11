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

# class NewItemForm(forms.Form):
#     id = forms.IntegerField(label="ID")
#     title = forms.CharField(label="title", widget=forms.TextInput(attrs={"id":"title"}))
#     description = forms.CharField(label="description")
#     quantity = forms.IntegerField(label="quantity")
#     supplier = forms.IntegerField(label="supplier")
#     category = forms.IntegerField(label="category")
#     location = forms.IntegerField(label="location")
#     img = forms.ImageField(label="image")
