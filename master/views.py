from django.shortcuts import render,redirect
from django.views.generic import View,UpdateView,FormView
from master.forms import VendorForm,CategoryForm,UserForm,LoginForm
from vendor.models import Vendor
from customer.models import Profile
from product.models import CategoryModel,OrderItem
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
# render the admin dashboard  


class LoginView(View):
    form_class = LoginForm
    def get(self,request):
        form_class = LoginForm()
        template_name = 'login.html'
        context = {
			'form':form_class,
            }
        return render(request,template_name,context)


class MasterHome(View):
    def get(self, request):
        vendor = Vendor.objects.all().count()
        total_customers = User.objects.all().count()
        total_oders = OrderItem.objects.all().count()
        # print('count',vendor)
        context = {
            'vendor':vendor,
            'total_customers':total_customers,
            'total_oders' : total_oders

        }
        return render(request,'admin.html',context)

# render the vendor management section that contain the section for managing the vendor
class VendorManagement(View):

    def get(self, request):
        vendors = Vendor.objects.all()
        context = {
            'vendors' : vendors
        }
        return render(request,'vendor_management.html',context)

class VendorUpdate(UpdateView):
    model = Vendor
    fields = ['shope_name','address','mobile_number','image']
    
    #template_name_suffix = '_update_form'
    success_url ='/vendor_management'

#view for adding the vendor and delete the vendor 
class AddVendor(FormView):
	template_name = 'add_vendor.html'
	model = User
	form_class = UserForm
	success_url='/vendor_management'
	
	def get(self,request,*args,**kwargs):
		self.object = None
		form_class = self.get_form_class()
		user_form = self.get_form(form_class)
		vendor_form = VendorForm()
		return self.render_to_response(self.get_context_data(form1=user_form,form2=vendor_form))

	def post(self,request,*args,**kwargs):
		self.object = None
		form_class = self.get_form_class()
		user_form =self.get_form(form_class)
		vendor_form = VendorForm(self.request.POST,self.request.FILES)
		
		if(user_form.is_valid() and vendor_form.is_valid()):
			return self.form_valid(user_form, vendor_form)
		else:
			return self.form_invalid(user_form,vendor_form)

	def form_valid(self, user_form, vendor_form):
			self.object = user_form.save()
			self.object.is_staff=True
			self.object.save()
			vendor = vendor_form.save(commit=False)
			vendor.user = self.object
			vendor.save()
			return super(AddVendor, self).form_valid(user_form)

	def form_invalid(self, user_form, vendor_form):
			return self.render_to_response(self.get_context_data(form1=user_form,form2=vendor_form))

def delete_vendor(request,vendor_id):
    vendor=Vendor.objects.get(id=vendor_id)
    vendor.delete()
    return redirect("/vendor_management")


#render the category management section that contain the section for managing the category
class CategoryManagement(View):
    def get(self,request):
        categories = CategoryModel.objects.all()
    
        
        context = {
            'categories': categories
        }
        return render(request,'category_management.html',context)

class CategoryUpdate(UpdateView):
    model = CategoryModel
    fields = ['category_name','image']
    success_url='/category_management'

class AddCategory(View):
    template_name = 'add_category.html'
    form_class = CategoryForm

    def get(self,request):
        form = self.form_class()
        context = {
            'form':form
        }
        return render(request,self.template_name,context)
    
    def post(self,request):
        form = self.form_class(self.request.POST,self.request.FILES)
        if form.is_valid():
            category=request.POST.get('category_name')
            image = request.FILES.get('image')
            print('img',image)
            category = CategoryModel.objects.create(category_name=category,image=image)
            return redirect('category_management')


def delete_category(request,category_id):
    category=CategoryModel.objects.get(id=category_id)
    category.delete()
    return redirect("/category_management")


class OrderDetails(View):
    def get(self,request):
        items = OrderItem.objects.all()
        context={
            'items':items
        }
        return render(request,'order_details.html',context)

class UserDetails(View):
    def get(self,request):
        user = Profile.objects.all()
        context = {
            'users' : user
        }
        return render(request,'user_details.html',context)