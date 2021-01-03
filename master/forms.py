from django import forms
from master.models import Vendor,CategoryModel

class VendorForm(forms.ModelForm):
    class Meta:
        model = Vendor
        fields = ['vendor','shope_name','address','mobile_number'] 
        

class CategoryForm(forms.ModelForm):
    class Meta:
        model = CategoryModel
        fields = ['category_name']
