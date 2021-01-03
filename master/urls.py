from django.contrib import admin
from django.urls import path
from master.views import (MasterHome,VendorManagement,
AddVendor,CategoryManagement,
AddCategory,OrderDetails,
UserDetails)

urlpatterns = [
	path(r'master/',MasterHome.as_view(),name='master_home'),
	path('vendor_management',VendorManagement.as_view(), name = 'vendor_management'),
	path('add_vendor',AddVendor.as_view(), name = 'add_vendor'),
	path('category_management',CategoryManagement.as_view(), name = 'category_management'),
	path('add_category',AddCategory.as_view(), name = 'add_category'),
	path('order_details',OrderDetails.as_view(), name = 'order_details'),
	path('user_details',UserDetails.as_view(), name = 'user_details'),
]
	

