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

import time
from geopy.geocoders import Nominatim


class geolocalizacion:

    def __init__(self, direccion):
        self.direccion = direccion

    def obtenerCoordenadas(self):
        geolocator = Nominatim()
        if (self.direccion!=''):
            # dejamos 2 sg para no sobrecargar la API
            time.sleep(2)
            location = geolocator.geocode(self.direccion)
            if location is not None:
                print((location.latitude, location.longitude))
            else:
                print("")
