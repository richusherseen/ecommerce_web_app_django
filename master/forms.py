from django import forms
from master.models import Vendor,CategoryModel

class VendorForm(forms.ModelForm):
    class Meta:
        model = Vendor
        fields = '__all__' 

class CategoryForm(forms.ModelForm):
    class Meta:
        model = CategoryModel
        fields = ['category_name']
