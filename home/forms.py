from django import forms


class AddProductForm(forms.Form):
    id = forms.IntegerField()
    name = forms.CharField()
    price = forms.FloatField()
    stock = forms.IntegerField()
    type = forms.CharField()
    description = forms.TextInput()
    avg_rating = forms.FloatField()
    image = forms.FileField()

class UpdateProductForm(forms.Form):
    id = forms.IntegerField()
    name = forms.CharField()
    price = forms.FloatField()
    stock = forms.IntegerField()
    type = forms.CharField()
    description = forms.TextInput()
    avg_rating = forms.FloatField()
    image = forms.FileField()
