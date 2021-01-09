from django.shortcuts import render,redirect
from django.views.generic import View,UpdateView
from vendor.forms import AddProductForm,AddOffer,AddOfferByCategory
from product.models import *
from vendor.models import Vendor

class VendorHome(View):
    def get(self, request):
        return render(request,'vendor.html')

class ProductManagement(View):

    def get(self, request):
        vendor=Vendor.objects.get(user = self.request.user.id)
        products = ProductModel.objects.filter(vendor_id = vendor)
        context = {
            'products':products
        } 
        return render(request,'product_management.html',context)

class AddProduct(View):
    template_name = 'add_product.html'
    form_class = AddProductForm
    
    def get(self,request):
        print("user in get",request.user)
        form = self.form_class()
        context = {

            'form':form
        }
        return render(request,self.template_name,context)
    def post(self,request):
        print("user in post",self.request.user)
        form = self.form_class(request.POST,request.FILES)
        if form.is_valid:

            vendor=Vendor.objects.get(user = self.request.user.id)
            # product_category = request.POST.get('product_category')
            product_name = request.POST.get('product_name')
            price = request.POST.get('price')
            quantity = request.POST.get('quantity')
            image = request.FILES.get('image')
            product_category =CategoryModel.objects.get(id = request.POST.get('product_category'))
            print('vendor ======',vendor)
            print('Product form is valid')
            product = ProductModel.objects.create(vendor=vendor,product_name=product_name,product_category=product_category,price=price,quantity=quantity,image=image)
            product.save()
            return redirect('product_management')
        else:
            print('Product form is not valid')

class ProductUpdate(UpdateView):
    model = ProductModel
    fields = '__all__'
    success_url='/product_management'

def delete_product(request,product_id):
    product=ProductModel.objects.get(id=product_id)
    product.delete()
    return redirect("/product_management")

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

class OfferByCategoryView(View):
    def get(self,request):
        return render(request,'offer_by_category.html')
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
