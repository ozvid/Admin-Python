'''
	@copyright   : OZVID Technologies Pvt. Ltd < https://ozvid.com >  
	@author      : Shiv Charan Panjeta < shiv@ozvid.com >
'''

from django.shortcuts import render
from django.contrib.auth import views as auth_views

from django.contrib.auth import authenticate, login as auth_login

from accounts.models import *
def login(request, template_name=None, extra_context=None):
    template_name = 'accounts/login.html'
    response = auth_views.login(request, template_name)

    def get_success_url(self):
        url = self.get_redirect_url()
        return url or resolve_url(settings.LOGIN_REDIRECT_URL)   
    return response


def logout(request):
    response = auth_views.logout(request, next_page='/')
        
    return response