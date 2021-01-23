from django import forms
from django.contrib.auth.models import User
from .models import Profile
from product.models import ShippingAdress
class LoginForm(forms.Form):
    
    username = forms.CharField(required=True,widget=forms.TextInput(attrs={'placeholder': 'User Name','class' : 'login-form'}))
    password = forms.CharField(required=True,max_length=50, widget=forms.PasswordInput(attrs={'placeholder': 'password','class' : 'login-form'}))
    

class RegisterForm(forms.Form):
    
    username = forms.CharField(required=True,widget=forms.TextInput(attrs={'placeholder': 'User Name','class' : 'login-form'}))
    password = forms.CharField(required=True,max_length=50, widget=forms.PasswordInput(attrs={'placeholder': 'password','class' : 'login-form'}))
    comfirm_password = forms.CharField(max_length=50,widget=forms.PasswordInput(attrs={'placeholder': 'confirm password','class' : 'login-form'}))

class UserUpdateForm(forms.ModelForm):

    
    class Meta:

        model = User
        fields = ['username']

class ProfileUpdateForm(forms.ModelForm):

    class Meta:

        model = Profile
        fields = ['image','name','email','phone']

class CheckOutForm(forms.ModelForm):
    class Meta:
        model = ShippingAdress
        fields = ['address','city','state','zipcode']