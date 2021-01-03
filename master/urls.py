from django.contrib import admin
from django.urls import path
from master.views import MasterHome,VendorManagement,AddVendor

urlpatterns = [
	path(r'master/',MasterHome.as_view(),name='master_home'),
	path('vendor_management',VendorManagement.as_view(), name = 'vendor_management'),
	path('add_vendor',AddVendor.as_view(), name = 'add_vendor'),
]
	

