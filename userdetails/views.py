from django.shortcuts import render
from django.contrib.auth import authenticate,login as dj_login
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect
from .models import SignUp, Login
from .forms import SignUpForm, LoginForm, SearchForm, HomeForm
from django.http import HttpResponse
from .forms import ContactForm

# for contact form
from django.core.mail import EmailMessage
from django.shortcuts import redirect
from django.template import Context
from django.template.loader import get_template

#above are dependencies for contact form


# Create your views here.

def signup(request):
	
	
	
	if request.method=='POST':
		form = SignUpForm(request.POST)
		username= request.POST.get('username')
		password= request.POST.get('password')
		print(password)
		user = User.objects.create_user(username, 'abc@thanuj.com', password)
		user.save()
		if form.is_valid():
			signin= form.save(commit=False)
			
			
			return redirect('login')
	else:
		form=SignUpForm()
	return render(request,'signup.html',{"form":form})
	
	
def login(request):
	title="welcome"
	
	form = LoginForm(request.POST or None)
	if form.is_valid():
		
		username= request.POST.get('username')
		password= request.POST.get('password')
		userlog = authenticate(username=username, password=password)
		
		if userlog is not None:
			dj_login(request,userlog)
			#userna=User.objects.get(username=username)
			#print(userna)
			
			return redirect('home')
			
		else:
			return redirect('login')
		
		
	#print(request.user) -- to get the current user username	
	return render(request,'login.html',{"form":form})
		
		
		
		

	
	
def home(request):
	form= SearchForm(request.POST or None)
	form1=HomeForm(request.POST or None)
	return render(request,'home.html',{"form":form,"form1":form1})
	
	
def about(request):
	return render(request,'about.html')
	
def contact(request):
	form=ContactForm
	if request.method == 'POST':
		form = form(data=request.POST)

		if form.is_valid():
			contact_name = request.POST.get(
				'contact_name'
            , '')
			contact_email = request.POST.get(
				'contact_email'
            , '')
			form_content = request.POST.get('content', '')

            # Email the profile with the 
            # contact information
			template = get_template('contact_template.txt')
			context = {
				'contact_name': contact_name,
				'contact_email': contact_email,
				'form_content': form_content,
				}
			content = template.render(context)

			email = EmailMessage(
				"New contact form submission",
				content,
				"Your website" +'',
				['youremail@gmail.com'],
				headers = {'Reply-To': contact_email }
			)
			email.send()
			return HttpResponse('Your Message has been sent succesfully <br/></br>'  + "<a href='/' > Home Page </a>")

    
	return render(request,'contactus.html',{"form":form})
	