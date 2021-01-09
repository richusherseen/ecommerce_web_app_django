from django.shortcuts import render,redirect
from django.views.generic import TemplateView,View,CreateView,ListView
from customer.models import ContactUs
from customer.forms import RegisterForm,LoginForm
from django.contrib.auth.models import User,auth
from django.contrib.auth import login,authenticate,logout
class HomeView(View):
	form_class = LoginForm
	form_class2 = RegisterForm
	model = User
	def get(self,request):
		
		form_class = LoginForm() 
		form_class2 = RegisterForm()      
		template_name = 'index.html'
		context = {
			'form':form_class,
			'form2':form_class2
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
					return render(request,'index.html')

			else:
				print('not authenticated')
			
		
def contact(request):
	if request.method == 'POST':
		name = request.POST['name']
		email = request.POST['email']
		subject = request.POST['subject']
		message = request.POST['message']
		
		feedback = ContactUs.objects.create(name=name,email=email,subject=subject,message=message)
		

	return render(request,'contact us.html')
