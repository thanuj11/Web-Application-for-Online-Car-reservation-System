# carrentals models

from django.db import models

# Create your models here.
class category(models.Model):
	category_type= models.CharField(max_length=50,unique=True)
	amount= models.IntegerField(default=0)

class car(models.Model):
	car_id= models.IntegerField(unique=True)
	brand= models.CharField(max_length=50)
	model=models.CharField(max_length=50)
	production_year= models.IntegerField(default=0)
	color=models.CharField(max_length=50)
	status= models.CharField(max_length=50)
	pickuplocation=models.CharField(max_length=50)
	dropofflocation= models.CharField(max_length=50)
	category_type= models.ForeignKey('category',on_delete=models.CASCADE,related_name='cars')
	def car_count(self,):
		return self.car_id.count()
	

	
class rental(models.Model):
	booking_id = models.AutoField(primary_key=True)
	car_id= models.ForeignKey('car', on_delete=models.CASCADE, related_name='rentals')
	username= models.CharField(max_length=50)
	pickuplocation=models.CharField(max_length=50)
	dropofflocation= models.CharField(max_length=50)
	startdate=models.DateField()
	enddate= models.DateField()
	
