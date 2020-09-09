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
    title       = forms.CharField(label = "",widget = forms.TextInput(attrs={"placeholder" : "Your title"}))
    description = forms.CharField(required = False ,
                                  widget = forms.Textarea(
                                      attrs = {
                                          "placeholder" : "Your title",
                                          "class" : "new class name two",
                                          "id" : "my_id_pom",
                                          "rows" : 20,
                                          "cols" : 80
                                      }
                                    )
                                )
    price       = forms.DecimalField(initial = 199.99) 