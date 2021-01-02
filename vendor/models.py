from django.db import models

class VendorModel(models.Model):
    vendor = models.OneToOneField(User, on_delete=models.CASCADE)
    address=models.CharField(max_length = 200,null = True)
    mobile_number=models.CharField(max_length=13, null=True, blank=True)
    image= models.ImageField(null = True, blank = True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)

