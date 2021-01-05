from django.contrib import admin
from django.urls import path
from master.views import (MasterHome,VendorManagement,
	AddVendor,CategoryManagement,
	AddCategory,OrderDetails,
	UserDetails,VendorUpdate,CategoryUpdate,
	LoginView)
from master import views
urlpatterns = [
	path('login',LoginView.as_view(), name = 'login'),
	path(r'master/',MasterHome.as_view(),name='master_home'),
	path('vendor_management',VendorManagement.as_view(), name = 'vendor_management'),
	path('vendor_edit/<int:pk>/',VendorUpdate.as_view(), name = 'vendor_edit'),
	path('add_vendor/',AddVendor.as_view(), name = 'add_vendor'),
	path('delete_vendor/<str:vendor_id>/',views.delete_vendor, name = 'delete_vendor'),
	path('category_management',CategoryManagement.as_view(), name = 'category_management'),
	path('category_edit/<int:pk>/',CategoryUpdate.as_view(), name = 'category_edit'),
	path('add_category',AddCategory.as_view(), name = 'add_category'),
	path('order_details',OrderDetails.as_view(), name = 'order_details'),
	path('user_details',UserDetails.as_view(), name = 'user_details'),
	path('delete_category/<str:category_id>/',views.delete_category, name = 'delete_category'),
]
	

