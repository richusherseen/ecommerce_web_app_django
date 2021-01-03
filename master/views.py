from django.shortcuts import render
from django.views.generic import View
from master.forms import VendorForm
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