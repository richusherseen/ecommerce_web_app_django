from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Vendor(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,null = True)
    
    shope_name = models.CharField(max_length=100)
    address=models.CharField(max_length = 200)
    mobile_number=models.CharField(max_length=12)
    image = models.ImageField(null=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)

    # def __str__(self):
    #     return self.user.username

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url
    

