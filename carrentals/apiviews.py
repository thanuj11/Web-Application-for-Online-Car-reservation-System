from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import rental
from .serializers import rentalserializer
# Create your views here.

@api_view(['GET','DELETE','PUT'])
def get_delete_update_rental(request, pk):
	try:
		p= rental.objects.get(pk= pk)
	except rental.DoesNotExist:
		return Response(status=status.HTTP_404_NOT_FOUND)
		
	if request.method=='GET':
		puppies=rental.objects.get(pk=pk)
		serializer=rentalserializer(puppies)
		return Response(serializer.data)
	elif request.method=='POST':
		return Response({})
	elif request.method=='PUT':
		serializer = rentalserializer(p, data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
	
	if request.method=='DELETE':
		p.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)
	
	
		
		
@api_view(['GET','POST'])
def get_post_rental(request):
	
		
	if request.method=='GET':
		puppies=rental.objects.all()
		serializer=rentalserializer(puppies,many=True)
		return Response(serializer.data)
	elif request.method=='POST':
		data = {
			'booking_id': request.data.get('booking_id'),
			'car_id': (request.data.get('car_id')),
			'username': request.data.get('username'),
			'pickuplocation': request.data.get('pickuplocation'),
			'dropofflocation': request.data.get('dropofflocation'),
			'startdate': request.data.get('startdate'),
			'enddate': request.data.get('enddate')
		}
		serializer = rentalserializer(data=data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
	