from rest_framework import serializers
from .models import rental

class rentalserializer(serializers.ModelSerializer):
	class Meta:
		model=rental
		fields=('booking_id','car_id','username','pickuplocation','dropofflocation','startdate','enddate')