#!/usr/bin/python
# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'sigesi.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
	url(r'^admin/', include(admin.site.urls)),

	
	#RETOS
	url(r'^retos/', include('apps.retos.urls')),
)
