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
from DISClib.Algorithms.Sorting import quicksort as qs
from DISClib.Algorithms.Sorting import mergesort as ms
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
               'categorias': None,'paises': None}

    catalog['videos'] = lt.newList(datastructure=estructura)
    catalog['categorias'] = lt.newList(datastructure=estructura,cmpfunction=comparecategorias)
    catalog['paises'] = lt.newList(datastructure=estructura,cmpfunction=comparepaises)
    return catalog

# Funciones para agregar informacion al catalogo
def addVideo(catalog, video):
    # Se adiciona el video a la lista de videos
    lt.addLast(catalog['videos'], video)
    paises = video['country'].split(",")
    categorias = video['category_id'].split(",")
    for pais in paises:
        addPaisVideo(catalog, pais.strip(), video)
    for categoria in categorias:
        addCategoriaVideo(catalog, categoria.strip(), video)

def addListaCategorias(catalog, categoria):
    """
    Adiciona una categoria a la lista de categorias
    """
    cat = newCategoria(categoria['name'], categoria['id'])
    lt.addLast(catalog['categorias'], cat)

def addCategoriaVideo(catalog, id_categoria,video):
    """
    Adiciona un categoria a la lista de categorias
    """
    #cat = newCategoria(categoria['name'], categoria['id'])
    #lt.addLast(catalog['categorias'], cat)
    categorias_lista = catalog['categorias']
    posvideo = lt.isPresent(categorias_lista, id_categoria)
    if posvideo > 0:
        categoria = lt.getElement(categorias_lista, posvideo)
    else:
        categoria = newCategoria(nombre_categoria,id)
        lt.addLast(categorias_lista, categoria)
    lt.addLast(categoria['videos'], video)

def addPaisVideo(catalog, nombre_pais, video):
    """
    Adiciona un pais a lista de paises, la cual guarda referencias
    a los videos de dicho pais
    """
    paises_lista = catalog['paises']
    posvideo = lt.isPresent(paises_lista, nombre_pais)
    if posvideo > 0:
        pais = lt.getElement(paises_lista, posvideo)
    else:
        pais = newPais(nombre_pais)
        lt.addLast(paises_lista, pais)
    lt.addLast(pais['videos'], video)


# Funciones para creacion de datos
def newCategoria(name, id):
    """
    Esta estructura almacena las categorias con sus id respectivos.
    """
    categoria = {'name': '', 'id': '', "videos": None}
    categoria['name'] = name
    categoria['id'] = id
    categoria['videos'] = lt.newList('ARRAY_LIST')
    return categoria

def newPais(name):
    """
    Crea una nueva estructura para modelar los libros de
    un autor y su promedio de ratings
    """
    pais = {'name': "", "categorias":None, "videos":None}
    pais['name'] = name
    pais['categorias'] = lt.newList('ARRAY_LIST')
    pais['videos'] = lt.newList('ARRAY_LIST')
    return pais
# Funciones de consulta
def categoria_en_lista(cat_id,lista,comp):
    nueva_lista=lt.newList(datastructure=ARRAY_LIST,cmpfunction=comp)
    for i in range(1,lt.size(lista)+1)
        video=lt.getElement(lista,i)
        if video['category_id']==cat_id:
            lt.addLast(nueva_lista,video)
    return nueva_lista


<<<<<<< HEAD

# Funciones utilizadas para comparar elementos dentro de una lista
def comparepaises(pais1, pais2):
    if (pais1.lower() == pais2['name'].lower()):
        return 0
    return -1
def comparecategorias(categoria1_id, categoria2_id):
    if (categoria1_id.lower() == categoria2_id['id'].lower()):
        return 0
    return -1
=======
# Funciones utilizadas para comparar elementos dentro de una lista
 
>>>>>>> 53ae8a123e28391b55af3b3198940f5bb6d28578
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
def sortVideos(catalog, size,algoritmo,pais,categoria):
    
    lista_ordenar=categoria_en_lista(categoria,lista,comp)
    sub_list = lt.subList(catalog['videos'], 0, size)
    sub_list = sub_list.copy()
    tiempo_inicio = time.process_time()
    if algoritmo=="shell":
        sorted_list = sa.sort(sub_list, cmpVideosByViews)
    elif algoritmo=="selection":
        sorted_list = ss.sort(sub_list, cmpVideosByViews)
    elif algoritmo=="insertion":
        sorted_list = ins.sort(sub_list, cmpVideosByViews)
    elif algoritmo=="merge":
        sorted_list = ms.sort(sub_list, cmpVideosByViews)
    elif algoritmo=="quick":
        sorted_list = qs.sort(sub_list, cmpVideosByViews)
    else:
        return "Vuelva a escribir en minusculas"
    tiempo_final = time.process_time()
    tiempo = (tiempo_final - tiempo_inicio)*1000
    return sorted_list,tiempo
