from django.db import models
from vendor.models import Vendor
from django.contrib.auth.models import User


class CategoryModel(models.Model):
    category_name = models.CharField(max_length = 200)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.category_name

class ProductModel(models.Model):
    vendor = models.ForeignKey(Vendor,on_delete=models.CASCADE)
    product_name = models.CharField(max_length=60,blank=False)
    product_category = models.ForeignKey(CategoryModel,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='media/product/')
    price = models.IntegerField(null=True,blank=True,default=0)
    quantity = models.IntegerField(default=0,null=True,blank=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.product_name
    
    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url

class Offer(models.Model):
    offer_type = {('Price Offer','Price Offer'),('Percentage Offer','Percentage Offer')}
    offer_type = models.CharField(default='Price Offer',max_length= 220,choices=offer_type)
    product = models.ForeignKey(ProductModel,on_delete=models.CASCADE,null=True)
    offer = models.FloatField(null=True)
    offer_expiry = models.DateField(null=True)

class OfferByCategory(models.Model):
    offer_type = {('Price Offer','Price Offer'),('Percentage Offer','Percentage Offer')}
    offer_type = models.CharField(default='Price Offer',max_length= 220,choices=offer_type)
    category = models.ForeignKey(CategoryModel,on_delete=models.CASCADE,null=True)
    offer = models.FloatField(null=True)
    offer_expiry = models.DateField(null=True)

class Order(models.Model):
    customer = models.ForeignKey(User, on_delete=models.SET_NULL,blank= True, null=True)
    vendor_id = models.ForeignKey(Vendor, on_delete=models.SET_NULL,blank= True, null=True)
    complete = models.BooleanField(default=False, null=True,blank=False)
    date_ordered = models.DateTimeField(auto_now_add=True)
    status_choice= ( 
    ("pending", "pendig"), 
    ("completed", "completed"),
    ("closed", "closed"),  
   )

    order_status = models.CharField(max_length = 200,choices=status_choice,default = 'Pending')

class OrderItem(models.Model):
    
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, blank = True, null = True)
    product = models.ForeignKey(ProductModel, on_delete=models.SET_NULL, blank = True, null = True)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

class ShippingAdress(models.Model):
    customer = models.ForeignKey(User, on_delete=models.SET_NULL,blank= True, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, blank = True, null = True)
    address = models.CharField(max_length = 200,null = True)
    city = models.CharField(max_length = 200,null = True)
    state = models.CharField(max_length = 200,null = True)
    zipcode = models.CharField(max_length = 200,null = True)
    country = models.CharField(max_length = 200,null = True)
    date_added = models.DateTimeField(auto_now_add=True)

