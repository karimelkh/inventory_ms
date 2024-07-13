from django import forms
from .models import Category

class NewCatForm(forms.ModelForm):
    class Meta():
        model = Category
        fields = [ "cat_id", "cat_name", "cat_desc", "cat_clr" ]
        labels = {
            "cat_id": "id",
            "cat_name": "name",
            "cat_desc": "description",
            "cat_clr": "color"
        }
        help_texts = {}
        error_messages = {}
