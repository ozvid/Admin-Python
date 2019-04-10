# -*- coding: utf-8 -*-
'''
	@copyright   : OZVID Technologies Pvt. Ltd < https://ozvid.com >  
	@author      : Shiv Charan Panjeta < shiv@ozvid.com >
'''
from django.shortcuts import render

def home(request):
    return render(request, 'core/home.html')
