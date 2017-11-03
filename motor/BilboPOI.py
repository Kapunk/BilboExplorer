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


import csv
from datos.datos import dstPOIBilbao

with open(dstPOIBilbao, encoding='iso-8859-1') as csvfile:
    leer = csv.reader(csvfile, delimiter=';')
    for lugar in leer:
        print(lugar[0],lugar[1],lugar[6],lugar[4],lugar[8],lugar[10],lugar[11])
