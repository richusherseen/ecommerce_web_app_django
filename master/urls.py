from django.contrib import admin
from django.urls import path
from master.views import MasterHome

urlpatterns = [
	path(r'master/',MasterHome.as_view(),name='master_home'),
]
	

