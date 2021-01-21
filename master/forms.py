from django import forms
from vendor.models import Vendor
from product.models import CategoryModel
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserForm(UserCreationForm):

	class Meta:
		model = User
		fields = ['first_name','last_name','email','username','password1','password2']
        
class VendorForm(forms.ModelForm):
    
    class Meta:
        model = Vendor
        fields = ['shope_name','address','mobile_number','image'] 
        

class CategoryForm(forms.ModelForm):
    class Meta:
        model = CategoryModel
        fields = ['category_name','image']


class LoginForm(forms.Form):
    
    username = forms.CharField(required=True,widget=forms.TextInput(attrs={'placeholder': 'User Name','class' : 'login-form'}))
    password = forms.CharField(required=True,max_length=50, widget=forms.PasswordInput(attrs={'placeholder': 'password','class' : 'login-form'}))

