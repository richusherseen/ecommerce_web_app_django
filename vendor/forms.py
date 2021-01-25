from django import forms
from product.models import ProductModel,Offer,OfferByCategory,Order

class AddProductForm(forms.ModelForm):
    class Meta:
        model = ProductModel
        
        exclude = ('vendor','created_at','updated_at','offer_price')

class AddOffer(forms.ModelForm):
    class Meta:
        model = Offer
        # fields = '__all__'
        exclude = ('vendor','product','offer_start','offer_expiry','offer_name')

class AddOfferByCategory(forms.ModelForm):
    class Meta:
        model = OfferByCategory
        fields = '__all__'

