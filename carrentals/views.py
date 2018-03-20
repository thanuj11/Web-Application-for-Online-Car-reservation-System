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

from .fusioncharts import FusionCharts
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
		#print(cart_list.brand)
		#print(cart_list.model)
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
			print(cart1.car_id.brand)
			try:
				#rows=['id','username','pickuplocation','dropofflocation','startdate','enddate']
				fopen= open('dat.txt','a')
				#for i in cart1:
				
					
				fopen.write(str(cart1.booking_id)+" "+ cart_list.brand+ " " +cart_list.model+" " + str(cart1.username)+ " " + cart1.pickuplocation+ " " + cart1.dropofflocation+ " " + str(start)+ " " + str(end))
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
				rental.objects.filter(booking_id=c.booking_id).delete()
				
				
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
	
	
def chart(request):
	# Chart data is passed to the `dataSource` parameter, as dict, in the form of key-value pairs.
	dataSource = {}
    # setting chart cosmetics
	dataSource['chart'] = { 
		"caption" : "Top 10 Most Populous Cars",
		"paletteColors" : "#0075c2",
		"bgColor" : "#ffffff",
		"borderAlpha": "20",
		"canvasBorderAlpha": "0",
		"usePlotGradientColor": "0",
		"plotBorderAlpha": "10",
		"showXAxisLine": "1",
		"xAxisLineColor" : "#999999",
		"showValues" : "0",
		"divlineColor" : "#999999",
		"divLineIsDashed" : "1",
		"showAlternateHGridColor" : "0"
		}
     
      
	dataSource['data'] = []
      # The data for the chart should be in an array wherein each element of the array is a JSON object as
      # `label` and `value` keys.
      # Iterate through the data in `Country` model and insert in to the `dataSource['data']` list.
	
	
	for key in rental.objects.all():
		data = {}
		data['label'] = key.car_id.brand
		#data['value'] = rental.objects.filter(car_id=key.car_id).distinct().count()
		data['value'] = rental.objects.filter(car_id=key.car_id).count()
		
		if key.car_id.brand not in data['label']:
			pass
		else:
			dataSource['data'].append(data)
		#count=0
		#print(data.values())
		#for key.car_id.brand in data['label']:
		#	count=count+1
		#	print(count)
		#if(count==1):
		
			
			
			

      # Create an object for the Column 2D chart using the FusionCharts class constructor               
	column2D = FusionCharts("column2D", "ex1" , "600", "400", "chart-1", "json", dataSource)
      # returning complete JavaScript and HTML code, which is used to generate chart in the browsers.
	return render(request, 'fusioncharts-html-template.html', {'output': column2D.render()}) 
  
  	
	
