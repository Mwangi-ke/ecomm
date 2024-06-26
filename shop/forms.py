from django import forms
from .models import Product,TV,AudioSystem

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'photo', 'price', 'details', 'category', 'is_draft', 'in_stock']



class SearchForm(forms.Form):
    query = forms.CharField(max_length=100, required=True)


class ProductSearchForm(forms.Form):
    PRODUCT_TYPE_CHOICES = (
        ('', 'All Products'),
        ('TV', 'TVs'),
        ('AudioSystem', 'Audio Systems'),
        ('Laptop', 'Laptops'),
    )
    product_type = forms.ChoiceField(choices=PRODUCT_TYPE_CHOICES, required=False)
    search_query = forms.CharField(max_length=255, required=False)    


class Form(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name','category','subcategory','condition','brand', 'price', 'details', 'photo', 'in_stock']


