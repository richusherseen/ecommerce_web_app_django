from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from vendor.models import Vendor



@receiver(post_save, sender=Vendor)
def create_profile(sender,instance,created,**kwargs):

    if created:
       User.objects.create(vendor=instance)
       
@receiver(post_save, sender=User)
def save_profile(sender,instance,**kwargs):

    instance.user.save()