from django.urls import path
from vendor.views import *
urlpatterns = [
	 path(r'vendor_home/',VendorHome.as_view(),name='vendor_home'),
	 path('product_management',ProductManagement.as_view(), name = 'product_management'),
	 path('add_product',AddProduct.as_view(), name = 'add_product'),
	 path('offer_by_product',OfferByProduct.as_view(), name = 'offer_by_product'),
	 path('add_offer',AddOfferView.as_view(), name = 'add_offer'),
	 path('offer_by_category',AddOfferByCategoryView.as_view(), name = 'offer_by_category'),
	 path('vendor_order_details',OrderDetailsView.as_view(), name = 'vendor_order_details'),
	# path('user_details',UserDetails.as_view(), name = 'user_details'),
]