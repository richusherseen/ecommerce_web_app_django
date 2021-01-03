from django import forms

class LoginForm(forms.Form):
    
    username = forms.CharField(required=True,widget=forms.TextInput(attrs={'placeholder': 'User Name','class' : 'login-form'}))
    password = forms.CharField(required=True,max_length=50, widget=forms.PasswordInput(attrs={'placeholder': 'password','class' : 'login-form'}))
    

class RegisterForm(forms.Form):
    
    username = forms.CharField(required=True,widget=forms.TextInput(attrs={'placeholder': 'User Name','class' : 'login-form'}))
    password = forms.CharField(required=True,max_length=50, widget=forms.PasswordInput(attrs={'placeholder': 'password','class' : 'login-form'}))
    comfirm_password = forms.CharField(max_length=50,widget=forms.PasswordInput(attrs={'placeholder': 'confirm password','class' : 'login-form'}))

