from django.db import models

class CategoryModel(models.Model):
    category_name = models.CharField(max_length = 200)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.category_name

class ProductModel(models.Model):
    vendor = models.ForeignKey(VendorModel,on_delete=models.CASCADE)
    product_name = models.CharField(max_length=60,blank=False)
    product_category = models.ForeignKey(CategoryModel,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='media/product/')
    price = models.IntegerField(null=True,blank=True,default=0)
    offer_price = models.IntegerField(null=True,blank=True)
    quantity = models.IntegerField(default=0,null=True,blank=True)

    def __str__(self):
        return self.p_name

class Offer(models.Model):
     
    offer_name = models.CharField(max_length= 220, null=True)
    product = models.ForeignKey(ProductModel,on_delete=models.CASCADE,null=True)
    vendor = models.ForeignKey(VendorModel,on_delete=models.CASCADE,null=True)
    discount_amount = models.FloatField(null=True)
    offer_start = models.DateField(auto_now_add=True, null=True)
    offer_expiry = models.DateField(null=True)

class Order(models.Model):
    customer = models.ForeignKey(User, on_delete=models.SET_NULL,blank= True, null=True)
    vendor_id = models.ForeignKey(VendorModel, on_delete=models.SET_NULL,blank= True, null=True)
    date_ordered = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False, null=True,blank=False)
    transaction_id = models.CharField(max_length = 200, null = True )
    status_choice= ( 
    ("pending", "pendig"), 
    ("completed", "completed"),
    ("closed", "closed"),  
   )

    order_status = models.CharField(,max_length = 200,choices=status_choice,default = 'Pending')

class OrderItem(models.Model):
    product = models.ForeignKey(ProductModel, on_delete=models.SET_NULL, blank = True, null = True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, blank = True, null = True)
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

