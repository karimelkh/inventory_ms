from django import forms
from .models import Category

class NewCatForm(forms.ModelForm):
    class Meta():
        model = Category
        fields = [ "id", "name", "desc", "clr" ]
        labels = {
            "id": "id",
            "name": "name",
            "desc": "description",
            "clr": "color"
        }
        help_texts = {}
        error_messages = {}

class UpdateCatForm(forms.ModelForm):
    class Meta():
        model = Category
        fields = [ "id", "name", "desc", "clr" ]
        labels = {
            "name": "name",
            "desc": "description",
            "clr": "color"
        }
        widgets = {
                "id": forms.HiddenInput(),
                }
        help_texts = {}
        error_messages = {}
