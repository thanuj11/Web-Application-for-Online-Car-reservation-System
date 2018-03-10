from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from .models import SignUp, Login, Search, HomeModel
from django.contrib.auth.models import User
from bootstrap_datepicker.widgets import DatePicker

class SignUpForm(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput)
	class Meta:
		model= SignUp
		fields=['username','firstname','lastname','password']
		
	
                
                
                
                
				
class LoginForm(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput)
	class Meta:
		model= Login
		fields=['username','password']
                
				
class SearchForm(forms.ModelForm):
	class Meta:
		model=Search
		fields=['searchtext']
		
categories= ( ('clearlake','clearlake'),('galveston','galveston'),('highlands','highlands'),('downtown','downtown'))

class HomeForm(forms.ModelForm):

	pickup= forms.ChoiceField(choices=categories, required=True)
	dropoff= forms.ChoiceField(choices=categories, required=True)

	class Meta:
		model= HomeModel
		widgets= {
		'username': forms.TextInput(attrs={'placeholder': 'What\'s your name?'}),
		'startdate': forms.TextInput(attrs={'placeholder': "YYYY-MM-DD"}),
		'enddate': forms.TextInput(attrs={'placeholder': "YYYY-MM-DD"})
		}
		fields= ['pickup','dropoff','startdate','enddate','username']
		
		
class ContactForm(forms.Form):
	contact_name = forms.CharField(required=True)
	contact_email = forms.EmailField(required=True)
	content = forms.CharField(
		required=True,
		widget=forms.Textarea
    )
	class Meta:
		fields=['contact_name','contact_email','content']