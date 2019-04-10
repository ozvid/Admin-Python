# -*- coding: utf-8 -*-
'''
	@copyright   : OZVID Technologies Pvt. Ltd < https://ozvid.com >  
	@author      : Shiv Charan Panjeta < shiv@ozvid.com >
'''
from django.conf.urls import url

from . import views
from .views import PostListView, PostDetailView, PostListByTagView

app_name='blog'

urlpatterns = [
    url(r'^(page(?P<page>\d+)/)?$', PostListView.as_view(), name='post-list'),
    url(r'^tags/(?P<slug>[-\w]+)/(page(?P<page>\d+)/)?$',
        PostListByTagView.as_view(), name='post-list-by-tag'),
    url(r'^archive/$', views.post_archive, name='post-archive'),
    url(r'^(?P<slug>[-\w]+)/$', PostDetailView.as_view(), name='post-detail'),
]
