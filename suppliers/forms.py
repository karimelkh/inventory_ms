from django import forms
from .models import Supplier

class NewSupplForm(forms.ModelForm):
    class Meta():
        model = Supplier
        fields = [
                "suppl_id", "suppl_name", "suppl_desc",
                "suppl_email", "suppl_phone", "suppl_addr",
                "suppl_site", "is_active", "suppl_img"
            ]
        labels = {
            "suppl_id": "id",
            "suppl_name": "name",
            "suppl_desc": "description",
            "suppl_email": "email",
            "suppl_addr": "address",
            "suppl_phone": "phone",
            "suppl_site": "website",
            "is_active": "is active",
            "suppl_img": "supplier image"
        }
        help_texts = {}
        error_messages = {}
