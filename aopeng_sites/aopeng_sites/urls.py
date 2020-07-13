"""aopeng_sites URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
#from django.contrib import admin
from django.urls import path
from django.urls import reverse
from django.conf.urls import url, include

import xadmin
xadmin.autodiscover()

from xadmin.plugins import xversion
xversion.register_models()

from django.urls import include
from django.urls import  path

urlpatterns = [
	#url(r'^xadmin/', xadmin.site.urls),
	#url(r'^factory/', factory.urls), 
	path('xadmin/', xadmin.site.urls),
	# path('op_xadmin/', include('op_xadmin.urls'))
	]

#urlpatterns = [
#    path('xadmin/', xadmin.site.usrls),
#]