"""csi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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

from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as authviews
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from frontpage import views as frontviews
from dashboard import views as dashviews
from forum import views as forumviews
from newsletters import views as newsviews
from gallery import views as galleryviews
from dashboard.views import *

# if settings.DEBUG:
#         urlpatterns += static(settings.MEDIA_URL,
#                               document_root=settings.MEDIA_ROOT)

urlpatterns = [
    url('admin/', admin.site.urls),
    path('', frontviews.login, name = "login"),
    path('subscribe', newsviews.subscribe, name = "subscribe"),
    url(r'^frontpage/$', frontviews.login, name = "frontpage"),
    url(r'^show_gallery/$', galleryviews.show_gallery, name = "show_gallery"),
    url(r'^dashboard/$', dashviews.dash, name = "dashboard"),#require login to fix
    url(r'^createevent/$', dashviews.dash, name = "createevent"),
    url(r'^$', dashviews.logout, name = "logout"),
    url(r'^forum/$', forumviews.forumpage, name = 'forum'),
    url(r'^events/$', dashviews.EventPage, name = 'events'),
    url(r'^attendance/$', dashviews.attendance, name = 'attendance'),
    url(r'^addclicks/$', dashviews.addEventClicks, name = 'addclicks'),
    path('image_upload', event_image_view, name = 'image_upload'),
    url('^sending_newsletter/$', newsviews.show_newsletter, name = 'show_newsletter'),
    path('pdf_upload', newsviews.pdf_view, name = 'pdf_upload'), 
    path('success', newsviews.success, name = 'success'), 
]

if settings.DEBUG: 
        urlpatterns += static(settings.MEDIA_URL, 
                              document_root=settings.MEDIA_ROOT)
