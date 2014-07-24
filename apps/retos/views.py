#!/usr/bin/python
# -*- coding: utf-8 -*-
from django.views.generic import CreateView
from .models import Evento
# Create your views here.
class RegistrarEvento(CreateView):
	template_name = 'retos/registrarEvento.html'
	model = Evento