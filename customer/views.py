from django.shortcuts import render
from django.views.generic import TemplateView,View,CreateView,ListView
from customer.models import ContactUs

class HomeView(TemplateView):       
	template_name = 'index.html'

def contact(request):
	if request.method == 'POST':
		name = request.POST['name']
		email = request.POST['email']
		subject = request.POST['subject']
		message = request.POST['message']
		
		feedback = ContactUs.objects.create(name=name,email=email,subject=subject,message=message)
		

	return render(request,'contact us.html')
