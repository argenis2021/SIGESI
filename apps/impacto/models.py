#!/usr/bin/python
# -*- coding: utf-8 -*-
from django.db import models

# Create your models here.

class Afectado(models.Model):
    cedula = models.IntegerField()
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)

    def __unicode__(self):
        return self.nombre
        
class Impacto(models.Model):
    impacto = models.CharField(max_length=15)

    def __unicode__(self):
        return self.impacto