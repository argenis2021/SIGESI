#!/usr/bin/python
# -*- coding: utf-8 -*-
from django.contrib import admin
from .models import Diligencia, Organismo, CasoAdministrativo, Denuncia


admin.site.register(Diligencia)
admin.site.register(Organismo)
admin.site.register(CasoAdministrativo)
admin.site.register(Denuncia)
