from django.db import models
from django.forms import ModelForm
# Create your models here.
from django import forms
class SignUp(models.Model):
	username= models.CharField(max_length=50, unique= True)
	firstname=models.CharField(max_length=50)
	lastname= models.CharField(max_length=50)
	password=models.CharField(max_length=50)
	license= models.CharField(max_length=50)
	
class Login(models.Model):

	username=models.CharField(max_length=50)
	password= models.CharField(max_length=50)
	
class Search(models.Model):
	searchtext= models.CharField(max_length=50)

categories= ( ('clearlake','clearlake'),('galveston','galveston'),('highlands','highlands'),('downtown','downtown'))
		
class HomeModel(models.Model):
	pickup= models.CharField(max_length=20,choices=categories)
	dropoff= models.CharField(max_length=20,choices=categories)
	username= models.CharField(max_length=50)
	startdate = models.DateField()
	enddate= models.DateField()
	
	
	
	
