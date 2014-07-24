#!/usr/bin/python
# -*- coding: utf-8 -*-
# ruta a nuestro archivo CSV
csv_filepathname="/home/argenis/djcode/sigesi/organismos.csv"
# ruta a nuestro proyecto de django
your_djangoproject_home="/home/argenis/djcode/sigesi/"

import sys,os
sys.path.append(your_djangoproject_home)
os.environ['DJANGO_SETTINGS_MODULE'] = 'sigesi.settings'

# importamos nuestro modelo
from apps.retos.models import Accion

import csv
dataReader = csv.reader(open(csv_filepathname), delimiter=',', quotechar='"')

for row in dataReader:
    if row[0] != 'DESCRIPCION': # ignoramos la primera línea del archivo CSV
        accion = Accion()
        accion.descripcion = row[0]
        accion.tipo = row[1]
        accion.save()