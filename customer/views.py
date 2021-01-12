from django.shortcuts import render,redirect
from django.views.generic import TemplateView,View,CreateView,ListView
from customer.models import ContactUs
from customer.forms import RegisterForm,LoginForm
from django.contrib.auth.models import User,auth
from django.contrib.auth import login,authenticate,logout
from product.models import ProductModel
from django.http import HttpResponse,JsonResponse
class HomeView(View):
	form_class = LoginForm
	form_class2 = RegisterForm
	model = User
	
	def get(self,request):
		
		form_class = LoginForm() 
		form_class2 = RegisterForm()      
		template_name = 'index.html'
		products = ProductModel.objects.all()
		print(products)
		context = {
			'form':form_class,
			'form2':form_class2,
			'products':products
		}
		return render(request,template_name,context)
	
	def post(self,request):
		
		form2 = self.form_class2(request.POST)
		if form2.is_valid():
			password=request.POST.get('password')
			user = User.objects.create(username = request.POST.get('username'))
			user.set_password(password)
			user.save()
			return redirect('/home')
		
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
					products = ProductModel.objects.all()
					context = {
						
						'products':products
					}
					return render(request,'index.html',context)

			else:
				print('not authenticated')

def updateItem(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']
    print("Action:", action)
    print("ProductId:", productId)

    customer=request.user.customer
    product=ProductModel.objects.get(id=productId)
    vendor=product.vendor
    print("dealer",vendor)
    order, created = Order.objects.get_or_create(customer=customer,complete=False)
    order.customer=vendor
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
	
def contact(request):
	if request.method == 'POST':
		name = request.POST['name']
		email = request.POST['email']
		subject = request.POST['subject']
		message = request.POST['message']
		
		feedback = ContactUs.objects.create(name=name,email=email,subject=subject,message=message)
		

	return render(request,'contact us.html')


