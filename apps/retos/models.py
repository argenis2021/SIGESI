#!/usr/bin/python
# -*- coding: utf-8 -*-
from django.db import models
from apps.scad.models import CasoAdministrativo
from apps.tipo.models import TipoEvento1, TipoEvento2, TipoEvento3
from apps.impacto.models import  Impacto, Afectado


#Campos relacionados con RETOS

class Proceso(models.Model):   
    descripcion = models.CharField(max_length=100)

    def __unicode__(self):
        return self.descripcion

class Accion(models.Model):
    descripcion = models.CharField(max_length=100)
    tipo = models.CharField(max_length=20)

    def __unicode__(self):
        return self.tipo

    #class Meta:
        #ordering = ['descripcion']

class Enlace(models.Model):
    website = models.URLField()

class Causa(models.Model):
    descripcion = models.CharField(max_length=100)
    tipo = models.CharField(max_length=20)

class Evento(models.Model):
    fecha_recepcion = models.DateField()
    fecha_ocurrencia = models.DateField()
    nobre_evento = models.CharField(max_length=20)
    descripcion = models.CharField(max_length=100)
    proceso = models.ForeignKey(Proceso)
    afectado = models.ManyToManyField(Afectado)
    accion = models.ManyToManyField(Accion)
    causa = models.ManyToManyField(Causa)
    enlace = models.ManyToManyField(Enlace)
    tipo1 = models.ForeignKey(TipoEvento1)
    tipo2 = models.ForeignKey(TipoEvento2)
    tipo3 = models.ForeignKey(TipoEvento3)
    impacto = models.ForeignKey(Impacto)
    caso_administrativo = models.ForeignKey(CasoAdministrativo)