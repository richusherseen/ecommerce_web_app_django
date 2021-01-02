from django.contrib import admin
from django.urls import path
from . import views
from customer.views import HomeView,contact

urlpatterns = [
	path(r'home/',HomeView.as_view(),name='home_page'),
	path('contact/',views.contact,name='contact_us'),
]

