#!/usr/bin/python
# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url
from .views import RegistrarEvento

urlpatterns = patterns('',
url(r'^registrar/$' , RegistrarEvento.as_view(), name="registrar_evento")
)