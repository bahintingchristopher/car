"""
URL configuration for finalsite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
"""

from django.contrib import admin
from django.urls import path, include, re_path #added so that the image will be loaded to site
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve # added serve

urlpatterns = [
    path('admin/', admin.site.urls), #connect to admin py
    path('', include('car.urls')),
]

# This block is essential for serving media files (like car images) 
# during local development (when settings.DEBUG is True).
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

else:
    urlpatterns += [
        re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
    ]