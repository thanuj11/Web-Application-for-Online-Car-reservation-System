#carrentals views
import datetime
from datetime import date
from django.shortcuts import render
from django.contrib.auth import authenticate,login as dj_login
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect
from .models import car, category, rental
from django.db.models import F
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
import csv
from bs4 import BeautifulSoup
import requests
import csv

# Create your views here.
stdate= datetime.datetime.today()
stdatetoday= datetime.datetime.today().strftime('%Y-%m-%d')
enddate= datetime.datetime.today()+datetime.timedelta(days=1)
@login_required
def car_list(request):
	global stdate
	global enddate
	if request.method=='POST':
		stloc= request.POST.get('pickup')
		dploc= request.POST.get('dropoff')
		stdate= request.POST.get('startdate')
		enddate= request.POST.get('enddate')
		print(stdate)
		if(stdate<enddate and stdate>=stdatetoday and enddate>stdatetoday):
			
			list1= car.objects.filter(pickuplocation=stloc)
			list=list1.filter(dropofflocation=dploc)
			#list=list2.filter(status="Available")
			print(list)
		else:
			return HttpResponse("<h2> please check the dates and try again </h2><br> <a href='/'> HomePage </a>")
		
		#print(list.status)
		#list1.save()	
		
			
		
	else:
		list=[]
		stdate= datetime.date.today()
		enddate= datetime.date.today()+datetime.timedelta(days=1)
		print(list)
	return render(request,'results.html',{"list":list})

@login_required	
def car_cart(request):
	if request.method=="GET":
		id= request.GET.get('id')
		#print(id)
		cart_list= car.objects.get(car_id=id)
		cart_list_id= cart_list.car_id
		#print(cart_list_id)
		userna=request.user
		#print(request.user)
		pick=cart_list.pickuplocation
		drop=cart_list.dropofflocation
		start= stdate
		end= enddate
		
		#print(stdate)
		#print(cart)
		#print(cart_list.status)
		if(stdate<enddate):
			cart1= rental.objects.create(car_id=cart_list,username=userna,pickuplocation=pick,dropofflocation=drop, startdate=start, enddate=end)
			#print(cart1)
			try:
				#rows=['id','username','pickuplocation','dropofflocation','startdate','enddate']
				fopen= open('dat.txt','a')
				#for i in cart1:
				
					
				fopen.write(str(cart1.booking_id)+" " + str(cart1.username)+ " " + cart1.pickuplocation+ " " + cart1.dropofflocation+ " " + str(start)+ " " + str(end))
				fopen.write("\n")
			finally:
				fopen.close()
		else:
			return HttpResponse("<h2> please check the dates anf try again </h2><br> <a href='/'> HomePage </a>")
		
		cart_list.status="NotAvailable"
		cart_list.save()
		cart2= rental.objects.all()
		for c in cart2:
			
			if (str(c.enddate)<stdatetoday):
				rental.objects.filter(car_id=c.car_id).delete()
				
				
		#with open('C:/studies/python/django/online_reservation/templates/cart.html') as file:
		#	soup = BeautifulSoup(file,'lxml')
		#source= requests.get('http://127.0.0.1:8000/history/').text  # now source have all the code inthe website in html format

		#soup= BeautifulSoup(source,'lxml')
		#x= soup.find('title')
		#print(x)		#c2.save()
		
		cart= rental.objects.filter(username=userna)
		
	return render(request,'cart.html',{"cart":cart})
	
@login_required	
def history(request):
	userna=request.user
	cart= rental.objects.filter(username=userna)
	return render(request,'history.html',{"cart":cart})
	
	
