from django.db import models
from django.contrib.auth.models import User
class Vendor(models.Model):
    vendor = models.OneToOneField(User, on_delete=models.CASCADE)
    shope_name = models.CharField(max_length=100)
    address=models.CharField(max_length = 200)
    mobile_number=models.CharField(max_length=12)
   
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)
    
