from django.contrib import admin
from django.urls import path
from . import views
from customer.views import HomeView,contact,updateItem,ProfieView,EditProfile,CartView,CheckOutView,OrderListView

urlpatterns = [
	path(r'',HomeView.as_view(),name='home_page'),
	path('contact/',views.contact,name='contact_us'),
	path('update_item/',views.updateItem,name='update_item'),
	path(r'profile/',ProfieView.as_view(),name='profile'),
	path(r'profile_edit/',EditProfile.as_view(),name='profile_edit'),
	path('logout/',views.logout_view,name='logout'),
	path(r'cart/',CartView.as_view(),name='cart'),
	path(r'checkout/',CheckOutView.as_view(),name='checkout'),
	path('process_order',views.processOrder,name='process_order'),
	path('view_orders',OrderListView.as_view(),name="view_orders"),
	path('product_list_based_on_category/<str:category_id>/',views.product_list_based_on_category,name='product_list_based_on_category'),

]

