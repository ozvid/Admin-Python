# -*- coding: utf-8 -*-
'''
	@copyright   : OZVID Technologies Pvt. Ltd < https://ozvid.com >  
	@author      : Shiv Charan Panjeta < shiv@ozvid.com >
'''
from django.conf.urls import url

from . import views

app_name='core'

urlpatterns = [
    url(r'^$', views.home, name='home'),
]
