from django.shortcuts import render,redirect
from django.views.generic import View,UpdateView
from master.forms import VendorForm,CategoryForm
from vendor.models import Vendor
from django.urls import reverse_lazy
# render the admin dashboard
class MasterHome(View):
    def get(self, request):
        return render(request,'admin.html')

# render the vendor management section that contain the section for managing the vendor
class VendorManagement(View):

    def get(self, request):
        vendors = Vendor.objects.all()
        print(vendors[1].image)
        context = {
            'vendors' : vendors
        }
        return render(request,'vendor_management.html',context)

class VendorUpdate(UpdateView):
    model = Vendor
    fields = ['username','shope_name','address','mobile_number','email','image']
    
    #template_name_suffix = '_update_form'
    success_url ='/vendor_management'

#view for adding the vendor and delete the vendor 
class AddVendor(View):
    template_name = 'add_vendor.html'
    form_class = VendorForm
    
    def get(self,request):

        form = self.form_class()
        context = {

            'form':form
        }
        return render(request,self.template_name,context)
   
    def post(self,request):
        form = self.form_class(request.POST,request.FILES)
       
        if form.is_valid():
            print('innnnnnnnnnnnnnnnnnnnnn')
            # vendor = request.POST.get('vendor')
            # image = request.FILES['image']
            # print(image)
            vendor = Vendor.objects.create(
                username = request.POST.get('username'),
                password = request.POST.get('password'),
                confirm_password=request.POST.get('confirm_password'),
                shope_name=request.POST.get('shope_name'),
                address=request.POST.get('address'),
                mobile_number=request.POST.get('mobile_number'),
                email=request.POST.get('email'),
                image = request.FILES.get('image'))
            vendor.save()
            
            return redirect('vendor_management')
        else:
            print("koooijoif form is not valid")


#render the category management section that contain the section for managing the category
class CategoryManagement(View):
    def get(self,request):
        return render(request,'category_management.html')

class AddCategory(View):
    template_name = 'add_category.html'
    form_class = CategoryForm

    def get(self,request):
        form = self.form_class()
        context = {
            'form':form
        }
        return render(request,self.template_name,context)

class OrderDetails(View):
    def get(self,request):
        return render(request,'order_details.html')

class UserDetails(View):
    def get(self,request):
        return render(request,'user_details.html')