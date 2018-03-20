from django.contrib import admin
from .models import category,car,rental
from django.contrib.admin import AdminSite
from userdetails.models import Login,SignUp
# Register your models here.

class MyAdminSite(AdminSite):
	site_header='Python Administration'
	site_title = "online portal"
	index_title = "Welcome to Online car reservation system Portal"
	actions = ["mark_immortal"]
	
	def mark_immortal(self, request, queryset):
		queryset.update(is_immortal=True)

		
admin_site= MyAdminSite(name="admin1")





admin_site.register(car)
admin_site.register(rental)

admin_site.register(Login)
admin_site.register(SignUp)



	