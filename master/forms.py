from django import forms
from master.models import Vendor
class VendorForm(forms.ModelForm):
    class Meta:
        model = Vendor
        fields = '__all__' 
