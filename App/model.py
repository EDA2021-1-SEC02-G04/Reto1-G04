"""
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
 *
 * Contribuciones:
 *
 * Dario Correal - Version inicial
 """


import config as cf
from DISClib.ADT import list as lt
from DISClib.Algorithms.Sorting import shellsort as sa
from DISClib.Algorithms.Sorting import selectionsort as ss
from DISClib.Algorithms.Sorting import insertionsort as ins
assert cf
import time

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""
# Construccion de modelos
def newCatalog(estructura:str):
    """
    Inicializa el catálogo de videos. Crea una lista vacia para guardar
    todos los videos, adicionalmente, crea una lista vacia para las categorias. Retorna el catalogo inicializado.
    """
    catalog = {'videos': None,
               'categorias': None,}

    catalog['videos'] = lt.newList(datastructure=estructura)
    catalog['categorias'] = lt.newList(datastructure=estructura)

    return catalog

# Funciones para agregar informacion al catalogo
def addVideo(catalog, video):
    # Se adiciona el libro a la lista de libros
    lt.addLast(catalog['videos'], video)


def addCategoria(catalog, categoria):
    """
    Adiciona un categoria a la lista de categorias
    """
    cat = newCategoria(categoria['name'], categoria['id'])
    lt.addLast(catalog['categorias'], cat)


# Funciones para creacion de datos
def newCategoria(name, id):
    """
    Esta estructura almacena las categorias con sus id respectivos.
    """
    categoria = {'name': '', 'id': ''}
    categoria['name'] = name
    categoria['id'] = id
    return categoria
# Funciones de consulta

# Funciones utilizadas para comparar elementos dentro de una lista

def cmpVideosByViews(video1, video2):
    """
    Devuelve verdadero (True) si los 'views' de video1 son menores que los del video2
    Args:
    video1: informacion del primer video que incluye su valor 'views'
    video2

    # Funciones de ordenamiento
    """
    
    if (float(video1['views']) > float(video2['views'])):
        return True
    else:
        return False
def sortVideos(catalog, size):
    sub_list = lt.subList(catalog['videos'], 0, size)
    sub_list = sub_list.copy()
    tiempo_inicio = time.process_time()
    sorted_list = sa.sort(sub_list, cmpVideosByViews)
    tiempo_final = time.process_time()
    tiempo = (tiempo_final - tiempo_inicio)*1000
    return sorted_list,tiempo
