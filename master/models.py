from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Vendor(models.Model):
    Vendor = models.OneToOneField(User,on_delete=models.CASCADE)
    shope_name = models.CharField(max_length=100)
    shope_address = models.CharField(max_length=100)
    
