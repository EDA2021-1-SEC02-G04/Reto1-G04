﻿"""
 * Copyright 2020, Departamento de sistemas y Computación,
 * Universidad de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 """

import config as cf
import model
import csv


"""
El controlador se encarga de mediar entre la vista y el modelo.
"""

# Inicialización del Catálogo de libros
def initCatalog(estructura:str):
    catalog = model.newCatalog(estructura)
    return catalog

def loadData(catalog):
    loadCategorias(catalog)
    loadVideos(catalog)
    

# Funciones para la carga de datos

def loadCategorias(catalog):

    categoriafile = cf.data_dir + 'category-id.csv'

    input_file = csv.DictReader(open(categoriafile, encoding='utf-8'),delimiter='\t')
    for categoria in input_file:
        model.addListaCategorias(catalog, categoria)
def loadVideos(catalog):
    videosfile = cf.data_dir + 'videos-large.csv'
    input_file = csv.DictReader(open(videosfile, encoding='utf-8'))
    for video in input_file:
        model.addVideo(catalog, video)


# Funciones de ordenamiento
def sortVideos(catalog,algoritmo,pais,categoria):
    """
    Ordena los videos por average_rating
    """
    return model.sortVideos(catalog,algoritmo,pais,categoria)

# Funciones de consulta sobre el catálogo
