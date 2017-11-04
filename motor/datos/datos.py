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

# recogemos los datos de la agenda de bilbao de open data bilbao
urlAgendaBilbao = 'http://www.bilbao.eus/cs/Satellite?c=Page&cid=1272990237857&pageid=1272990237857&idioma=es&pagename=Bilbaonet/Page/BIO_ListadoEventosAppInfoBilbao&todos=si'
dstAgendaBilbao = 'datos/EventosInfoBilbao.json'

# recogemos los POI de Bilbao de open data bilbao
urlPOIBilbao = 'http://www.bilbao.eus/aytoonline/jsp/od_dataset.jsp?idioma=&formato=csv&dataset=LugaresInteresTuristico'
dstPOIBilbao = 'datos/LugaresInteresTuristico.csv'

#recogemos la prediccion del tiempo de aemet SOLO para la ciudad de bilbao
aemetAPI = <PON AQUI TU API>
aemetURL = "https://opendata.aemet.es/opendata/api/prediccion/especifica/municipio/horaria/48020/?api_key="
