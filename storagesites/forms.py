from django import forms
from .models import Site

class NewSiteForm(forms.ModelForm):
    class Meta():
        model = Site
        fields = [ "site_name", "site_phone", "site_addr", "site_type", "site_img" ]
        labels = { 
              "site_name": "name",
              "site_phone": "phone",
              "site_addr": "address",
              "site_type": "type",
              "site_img": "image",
          }
        help_texts = {}
        error_messages = {}
