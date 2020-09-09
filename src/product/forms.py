from django import  forms

from .models import  Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            'title',
            'description',
            'price'
        ]


# https://docs.djangoproject.com/en/3.1/ref/forms/fields/,
class RawProductForm(forms.Form):
    title       = forms.CharField()
    description = forms.CharField()
    price       = forms.DecimalField() 