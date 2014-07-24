#!/usr/bin/python
# -*- coding: utf-8 -*-
from django.db import models

# Create your models here.
class TipoEvento3(models.Model):
	Tipo3 = models.CharField(max_length=15)

	def __str__(self):
		return self.Tipo3

class TipoEvento2(models.Model):
	Tipo2 = models.CharField(max_length=15)
	tipo3 = models.ManyToManyField(TipoEvento3)

	def __str__(self):
		return self.Tipo2

class TipoEvento1(models.Model):
	Tipo1 = models.CharField(max_length=15)
	tipo2 = models.ManyToManyField(TipoEvento2)

	def __str__(self):
		return self.Tipo1