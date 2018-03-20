"""online_reservation URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
from django.contrib.auth import views as auth_views
from userdetails import views as details
from carrentals import views as cars
from carrentals import apiviews as av
from carrentals.admin import admin_site
from django_otp.admin import OTPAdminSite

admin.site.__class__ = OTPAdminSite
urlpatterns = [
    url(r'^$',details.home, name='home'),
	url(r'^admin/', admin_site.urls),
	url(r'^myadmin/', admin_site.urls),
	url(r'^signup/$',details.signup, name='signup'),
	url(r'^login/$',details.login, name='login'),
	url(r'^logout/$',auth_views.LogoutView.as_view(),name='logout'),
	url(r'^results/$', cars.car_list,name='car_list'),
	url(r'^cart/$', cars.car_cart,name='cart'),
	url(r'^about/$',details.about, name='about'),
	url(r'^contact/$',details.contact, name='contact'),
	url(r'^history/$', cars.history,name='history'),
	url(r'^chart/$',cars.chart, name='chart'),
	
	
	url(r'^reset/$',
    auth_views.PasswordResetView.as_view(
        template_name='password_reset.html',
        email_template_name='password_reset_email.html',
        subject_template_name='password_reset_subject.txt'
    ),
    name='password_reset'),
url(r'^reset/done/$',
    auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'),
    name='password_reset_done'),
url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
    auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'),
    name='password_reset_confirm'),
url(r'^reset/complete/$',
    auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'),
    name='password_reset_complete'),

url(r'^settings/password/$', auth_views.PasswordChangeView.as_view(template_name='password_change.html'),
    name='password_change'),
url(r'^settings/password/done/$', auth_views.PasswordChangeDoneView.as_view(template_name='password_change_done.html'),
    name='password_change_done'),
	
	
	
	url(r'^api/v1/rental/(?P<pk>\d+)/$',av.get_delete_update_rental,name='get_delete_update_rental'),
	url(r'^api/v1/rental/$',av.get_post_rental,name='get_post_rental'),
	url(
        r'^api-auth/',
        include('rest_framework.urls', namespace='rest_framework')
    ),
	

	
	
	
	
	
	
]
