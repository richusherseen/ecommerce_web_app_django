from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver


class CustomUser(AbstractUser):
    user_type_data=((1,"MD"),(2,"Vendor"),(3,"Customer"))
    user_type=models.CharField(default=1,choices=user_type_data,max_length=10)

class AdminMD(models.Model):
    id=models.AutoField(primary_key=True)
    admin=models.OneToOneField(CustomUser,on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at =models.DateTimeField(auto_now=True)
    objects=models.Manager()


class ContactUs(models.Model):

    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()

    def __str__(self):
        return self.name
        
class Profile(models.Model):

    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    image = models.ImageField(default = 'default.jpg',upload_to='profile_pics')
    address = models.TextField(blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):

        return  self.user.username


@receiver(post_save, sender=CustomUser)
def create_profile(sender, instance, created, **kwargs):
    if created:
        if instance.user_type==1:
            AdminMD.objects.create(admin = instance)
        if instance.user_type==2:
            Vendor.objects.create(admin = instance)
        if instance.user_type==3:
            Customer.objects.create(user = instance)




@receiver(post_save,sender=CustomUser)
def save_user_profile(sender,instance,**kwargs):
    if instance.user_type==1:
        instance.adminmd.save()
    if instance.user_type==2:
        instance.vendor.save()
    if instance.user_type==3:
        instance.customer.save()
    