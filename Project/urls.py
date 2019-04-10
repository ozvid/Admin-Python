'''
	@copyright   : OZVID Technologies Pvt. Ltd < https://ozvid.com >  
	@author      : Shiv Charan Panjeta < shiv@ozvid.com >
'''

from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin

urlpatterns = [
    url(r'^jet/', include('jet.urls', 'jet')),
    url(r'^jet/dashboard/', include('jet.dashboard.urls', 'jet-dashboard')),
    url(r'^admin/', admin.site.urls),

    url(r'^ckeditor/', include('ckeditor_uploader.urls')),

    url(r'^contact/', include('contact.urls', namespace='contact')),
    url(r'^blog/', include('blog.urls', namespace='blog')),
    url(r'^accounts/', include('accounts.urls', namespace='accounts')),

    url(r'^about/', include('about.urls', namespace='about')),
    url(r'', include('core.urls', namespace='core')),
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
