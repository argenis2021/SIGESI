#!/usr/bin/python
# -*- coding: utf-8 -*-
from django.db import models

# Create your models here.

class Denuncia(models.Model):
	fecha = models.DateField()
	observacion = models.CharField(max_length=100)

class Diligencia(models.Model):
	fecha = models.DateField()
	contacto = models.CharField(max_length=30)
	anexo = models.CharField(max_length=20)

class Organismo(models.Model):
	Nombre_organismo = models.CharField(max_length=20)

	def __unicode__(self):
		return self.Nombre_organismo

class CasoAdministrativo(models.Model):
	descripcion = models.CharField(max_length=50)
	fecha_inicio = models.DateField()
	fecha_cierre = models.DateField()
	monto_perdida = models.IntegerField()
	monto_recuperado = models.IntegerField()
	decision = models.CharField(max_length=50)
	denuncia = models.ForeignKey(Denuncia)
	diligencia = models.ManyToManyField(Diligencia)
	organismo = models.ForeignKey(Organismo)

	def __unicode__(self):
		return self.descripcion
