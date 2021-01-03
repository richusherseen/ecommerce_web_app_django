from django.shortcuts import render,redirect
from django.views.generic import View
from vendor.forms import AddProductForm,AddOffer,AddOfferByCategory

class VendorHome(View):
    def get(self, request):
        return render(request,'vendor.html')

class ProductManagement(View):

    def get(self, request):
        return render(request,'product_management.html')

class AddProduct(View):
    template_name = 'add_product.html'
    form_class = AddProductForm
    
    def get(self,request):

        form = self.form_class()
        context = {

            'form':form
        }
        return render(request,self.template_name,context)

class OfferByProduct(View):
    def get(self,request):
        return render(request,'offer_by_product.html')


class AddOfferView(View):
    template_name = 'add_offer.html'
    form_class = AddOffer
    
    def get(self,request):

        form = self.form_class()
        context = {

            'form':form
        }
        return render(request,self.template_name,context)

class AddOfferByCategoryView(View):
    template_name = 'add_offer_by_category.html'
    form_class = AddOfferByCategory
    
    def get(self,request):

        form = self.form_class()
        context = {

            'form':form
        }
        return render(request,self.template_name,context)

class OrderDetailsView(View):
    def get(self, request):
        return render(request,'vendor_order_details.html')
