# -*- coding: utf-8 -*-
'''
	@copyright   : OZVID Technologies Pvt. Ltd < https://ozvid.com >  
	@author      : Shiv Charan Panjeta < shiv@ozvid.com >
'''
from django.conf.urls import url

from .views import ContactView

app_name='contact'

urlpatterns = [
    url(r'^$', ContactView.as_view(), name='contact'),
]
