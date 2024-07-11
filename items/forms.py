from django import forms

class NewItemForm(forms.Form):
    id = forms.IntegerField(label="ID")
    title = forms.CharField(label="title", widget=forms.TextInput(attrs={"id":"title"}))
    description = forms.CharField(label="description")
    quantity = forms.IntegerField(label="quantity")
    supplier = forms.IntegerField(label="supplier")
    category = forms.IntegerField(label="category")
    location = forms.IntegerField(label="location")
    img = forms.ImageField(label="image")
