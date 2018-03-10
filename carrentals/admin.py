from django.contrib import admin
from .models import category,car,rental
from django.contrib.admin import AdminSite
# Register your models here.

class MyAdminSite(AdminSite):
	site_header='Monthly Python Administration'

secret_key='abcdefgh'
	
admin_site= MyAdminSite(name=secret_key)
admin_site.register(car)
admin_site.register(rental)