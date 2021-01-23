from django.shortcuts import render,redirect
from django.views.generic import View,UpdateView,CreateView
from vendor.forms import AddProductForm,AddOffer,AddOfferByCategory
from product.models import *
from customer.models import Profile
from vendor.models import Vendor

class VendorHome(View):
    def get(self, request):
        user=request.user.id
        dealer=Vendor.objects.get(user=user)
        products=ProductModel.objects.filter(vendor=dealer).count()
        order_count=Order.objects.filter(vendor_id=dealer).count()

        customer_count=Profile.objects.all().count()

        # total price counting
        orders=Order.objects.filter(vendor_id=dealer)
        total = 0
        for order in orders:
            try:
                order_total=order.get_cart_total
            except:
                order_total=0
            total=total+order_total


        
        context = {
            'products':products,
            'order_count':order_count,
            'customer_count':customer_count,
            'total':total,
        }
        return render(request,'vendor.html',context)

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
    # success_url = ('/product_management') 
    def get(self,request,pk):

        form = self.form_class()
        context = {

            'form':form
        }
        return render(request,self.template_name,context)


    def post(self,request,pk):
        form = self.form_class(request.POST)
        p_id = self.kwargs['pk']

        product_obj=ProductModel.objects.get(id=p_id)
        offer_name=request.POST.get('offer_name')
        discount_amount=request.POST.get('discount_amount')
        user=request.user.id

        # print("product",product)
        # print("offer_name",offer_name)
        # print("discount_amount",discount_amount)
        # print(p_id)
        vendor=Vendor.objects.get(user=user)
        ofer_exist=Offer.objects.filter(product=product_obj,vendor=vendor).exists()

        if ofer_exist:
            price=product_obj.offer_price
            discount_amounts= int(discount_amount)
            offers_price=price-(int(price)*(discount_amounts/100))

            offer = Offer.objects.get(product=product_obj,vendor=vendor)
            offer.discount_amount=discount_amount
            offer.offer_name=offer_name
            offer.save()
            product_obj.price=offers_price
            product_obj.save()
            
        else:
            offers=Offer.objects.create(offer_name=offer_name,discount_amount=discount_amount,product=product_obj,vendor=vendor)
            # offers.save()
            price=product_obj.price
            product_obj.offer_price=price
            discount_amounts= int(discount_amount)
            offer_price=price-(int(price)*(discount_amounts/100))
            product_obj.price=offer_price
            product_obj.save()

        return redirect('/product_management')
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


