from django.contrib import admin
from django.urls import path
from . import views
from customer.views import HomeView,contact,updateItem

urlpatterns = [
	path(r'',HomeView.as_view(),name='home_page'),
	path('contact/',views.contact,name='contact_us'),
	path('update_item/',views.updateItem,name='update_item'),
]

