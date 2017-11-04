#! /usr/bin/python3
# -*- coding: utf-8 -*-

"""
	BilboExplorer - Descubre Bilbao!
    Copyright (C) 2017  Kepa Muñoz (kepa10@gmail.com)

	This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""
import json
from datos.datos import aemetAPI,aemetURL
import requests
import urllib3
# desabilitamos los warnings para que no nos de el error de certificado al recoger la peticion de aemet
urllib3.disable_warnings()

r = requests.get(url=aemetURL+aemetAPI, verify=False)
print(r.json()["datos"])

leer = requests.get(url=r.json()["datos"], verify=False)

dia = leer.json()[0]["prediccion"]["dia"]

for predMetDia in dia:

	print ("Fecha: "+ predMetDia["fecha"])
	print ("Amanecer: "+ predMetDia["orto"])
	print ("Anochecer: "+ predMetDia["ocaso"])

	for temperatura in predMetDia["temperatura"]:
		print("temperatura: "+temperatura["value"])
		print("hora: "+temperatura["periodo"])

	for lluvia in predMetDia["precipitacion"]:
		print("lluvia: "+lluvia["value"]+"%")
		print("hora: "+lluvia["periodo"])
