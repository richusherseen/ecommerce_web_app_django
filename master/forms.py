from django import forms
from vendor.models import Vendor
from product.models import CategoryModel

class VendorForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    confirm_password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = Vendor
        fields = ['username','password','confirm_password','shope_name','address','mobile_number','email','image'] 
        

class CategoryForm(forms.ModelForm):
    class Meta:
        model = CategoryModel
        fields = ['category_name']
