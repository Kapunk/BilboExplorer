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
from datos.datos import dstAgendaBilbao

# leemos el json con los datos de la agenda de eventos
leer = json.loads(open(dstAgendaBilbao,encoding='utf-8').read())

# de cada evento sacamos sus datos
for evento in leer:

	if 'titulo' in evento:
		print ("titulo " + evento["titulo"])
	if 'tipo' in evento:
		print ("tipo " + evento["tipo"])
	if 'lugar' in evento:
		print ("lugar " + evento["lugar"])
	if 'direccion' in evento:
		print ("direccion " + evento["direccion"])
	if 'fecha_desde' in evento:
		print ("fecha_desde " + evento["fecha_desde"])
	if 'id' in evento:
		print ("id " + evento["id"])
	if 'observaciones' in evento:
		print ("observaciones " + evento["observaciones"])
	if 'info' in evento:
		print ("info " + evento["info"])
	if 'leyenda' in evento:
		#leer = json.loads(open('EventosInfoBilbao.json',encoding="utf8").read())
		for leyenda in evento["leyenda"]:
			print (leyenda)
	if 'parametros' in evento:
		print ("parametros " + evento["parametros"])
	if 'distritos' in evento:
		for distrito in evento["distritos"]:
			print (distrito)
	print ("___________________")
