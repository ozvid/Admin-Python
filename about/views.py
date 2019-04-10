# -*- coding: utf-8 -*-
'''
	@copyright   : OZVID Technologies Pvt. Ltd < https://ozvid.com >  
	@author      : Shiv Charan Panjeta < shiv@ozvid.com >
'''

from django.shortcuts import render

def about(request):
    return render(request, 'about/about.html')
