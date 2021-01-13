from django.shortcuts import render,redirect
from django.views.generic import TemplateView,View,CreateView,ListView
from customer.models import ContactUs
from customer.forms import RegisterForm,LoginForm,UserUpdateForm,ProfileUpdateForm
from django.contrib.auth.models import User,auth
from django.contrib.auth import login,authenticate,logout
from product.models import *
from .models import Profile
from django.http import HttpResponse,JsonResponse
import json

class HomeView(View):
	form_class = LoginForm
	form_class2 = RegisterForm
	model = User
	
	def get(self,request):
		
		form_class = LoginForm() 
		form_class2 = RegisterForm()      
		template_name = 'index.html'
		products = ProductModel.objects.all()
		if request.user.is_authenticated:
			customer=request.user
			order = Order.objects.get(customer=customer)
			cartItems=order.get_cart_items
		else:
			items=[]
			order ={'get_cart_total':0,'get_cart_items':0,'shipping':False}
			cartItems=order['get_cart_items']
			print("get",cartItems)
		print(products)
		context = {
			'form':form_class,
			'form2':form_class2,
			'products':products,
			'cartItems':cartItems
		}
		return render(request,template_name,context)
	
	def post(self,request):
		
		form2 = self.form_class2(request.POST)
		if form2.is_valid():
			password=request.POST.get('password')
			user = User.objects.create(username = request.POST.get('username'))
			user.set_password(password)
			user.save()
			return redirect('profile')
		
		form = self.form_class(request.POST)
		if form.is_valid():
			username = request.POST.get('username')
			password = request.POST.get('password')
			print('username===',username)
			print('password====',password)
			user = auth.authenticate(username=username,password=password)
			print('user ====',user)
			if user is not None:
				print('user is not none')
				login(request,user)
				if user.is_superuser:
					print('super user')
					return render(request,"admin.html")
				if user.is_staff:
					print('staffff')
					return render(request,'vendor.html')
				else:
					print('customer')
					if request.user.is_authenticated:
						customer=request.user
						order, created = Order.objects.get_or_create(customer=customer,complete=False)
						cartItems=order.get_cart_items
						print("post",cartItems)
					else:
						items=[]
						order ={'get_cart_total':0,'get_cart_items':0,'shipping':False}
						cartItems=order['get_cart_items']
					products = ProductModel.objects.all()
					context = {
						
						'products':products,
						'cartItems':cartItems
					}
					return render(request,'index.html',context)

			else:
				print('not authenticated')

#function for add to cart
def updateItem(request):
	data = json.loads(request.body)
	print("giufdbgi",data)
	productId = data['productId']
	action = data['action']
	print("Action:", action)
	print("ProductId:", productId)

	customer=request.user
	print("cud",customer)
	product=ProductModel.objects.get(id=productId)
	vendor=product.vendor
	print("dealer",vendor)
	order, created = Order.objects.get_or_create(customer=customer,complete=False)
	order.vendor_id=vendor
	order.save()
	
	orderItem, created = OrderItem.objects.get_or_create(order=order,product=product)

	if action == 'add':
		orderItem.quantity = (orderItem.quantity + 1)
	elif action == 'remove':
		orderItem.quantity = (orderItem.quantity - 1)

	orderItem.save()

	if orderItem.quantity <=0:
		orderItem.delete()
	


	return JsonResponse('Item was added' , safe=False) 

class ProfieView(View):
	
	def get(self,request):
		
		profiles = Profile.objects.get(user = request.user.id)
		print('profilesssss',profiles)
		items=[]
		order ={'get_cart_total':0,'get_cart_items':0,'shipping':False}
		cartItems=order['get_cart_items']

		context={
		'cartItems':cartItems,
		'profiles':profiles
		
		}
		return render(request,'profile.html',context)

class EditProfile(View):

	def get(self,request):
		
		u_form = UserUpdateForm(instance=request.user)
		p_form = ProfileUpdateForm(instance=request.user.profile)

		context={

			'u_form': u_form,
			'p_form': p_form
		}

		return render(request,'edit_profile.html',context)

	def post(self,request):

		u_form = UserUpdateForm(request.POST,instance=request.user)
		p_form = ProfileUpdateForm(request.POST,request.FILES,
		instance=request.user.profile)
		print(p_form)
		if u_form.is_valid() and p_form.is_valid():


			u_form.save()
			p_form.save()
			
			return redirect('profile')

def contact(request):
	if request.method == 'POST':
		name = request.POST['name']
		email = request.POST['email']
		subject = request.POST['subject']
		message = request.POST['message']
		
		feedback = ContactUs.objects.create(name=name,email=email,subject=subject,message=message)
		

	return render(request,'contact us.html')


