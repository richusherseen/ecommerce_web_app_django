from django.db import models
from django.contrib.auth.models import User
class Vendor(models.Model):
    username = models.CharField(max_length=50,null=True)
    password = models.CharField(max_length=50,null=True)
    confirm_password = models.CharField(max_length=50,null=True)
    shope_name = models.CharField(max_length=100)
    address=models.CharField(max_length = 200)
    mobile_number=models.CharField(max_length=12)
    email = models.EmailField(null=True)
    image = models.ImageField(null=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url
    
