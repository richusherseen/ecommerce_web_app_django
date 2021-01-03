from django.shortcuts import render,redirect
from django.views.generic import View
from master.forms import VendorForm,CategoryForm
# Create your views here.
class MasterHome(View):
    def get(self, request):
        return render(request,'admin.html')

class VendorManagement(View):

    def get(self, request):
        return render(request,'vendor_management.html')

class AddVendor(View):
    template_name = 'add_vendor.html'
    form_class = VendorForm
    
    def get(self,request):

        form = self.form_class()
        context = {

            'form':form
        }
        return render(request,self.template_name,context)

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