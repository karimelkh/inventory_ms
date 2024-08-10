from django import forms
from .models import Site

class NewSiteForm(forms.ModelForm):
    class Meta():
        model = Site
        fields = [ "id", "name", "phone", "addr", "type", "img" ]
        labels = {
              "id": "id",
              "name": "name",
              "phone": "phone",
              "addr": "address",
              "type": "type",
              "img": "image",
          }
        help_texts = {}
        error_messages = {}
