#!/usr/bin/python
# -*- coding: utf-8 -*-
from django.contrib import admin
from .models import Evento, Accion, Enlace, Causa, Afectado, Proceso
from .models import TipoEvento1, TipoEvento2, TipoEvento3, Impacto

class ProcesoAdmin (admin.ModelAdmin):
    list_display = ('id', 'descripcion')

class EventoAdmin (admin.ModelAdmin):
   filter_horizontal = ('accion',)

class AccionAdmin (admin.ModelAdmin):
    list_display = ('descripcion', 'tipo')
    list_filter = ('descripcion', 'tipo')
    ordering = ('-descripcion',)
    search_fields = ('descripcion',)  

admin.site.register(Evento, EventoAdmin)
admin.site.register(Accion, AccionAdmin)
admin.site.register(Enlace)
admin.site.register(Causa)
admin.site.register(Afectado)
admin.site.register(Proceso, ProcesoAdmin)
admin.site.register(TipoEvento1)
admin.site.register(TipoEvento2)
admin.site.register(TipoEvento3)
admin.site.register(Impacto)

