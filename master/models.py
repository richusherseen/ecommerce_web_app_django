from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Vendor(models.Model):
    Vendor = models.OneToOneField(User,on_delete=models.CASCADE)
    shope_name = models.CharField(max_length=100)
    shope_address = models.CharField(max_length=100)
    
class CategoryModel(models.Model):
    category_name = models.CharField(max_length = 200)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.category_name