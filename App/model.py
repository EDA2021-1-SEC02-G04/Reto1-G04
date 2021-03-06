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
               'categorias': None,'paises': None, 'trending':None}

    catalog['videos'] = lt.newList(datastructure=estructura)
    catalog['categorias'] = lt.newList(datastructure=estructura,cmpfunction=comparecategorias)
    catalog['paises'] = lt.newList(datastructure=estructura,cmpfunction=comparepaises)
    catalog['trending'] = lt.newList(datastructure=estructura,cmpfunction=comparetrending)
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

def addTrending(trending_lista,video):
    video
    posvideo = lt.isPresent(trending_lista, video)
    if posvideo > 0:
        vid=lt.getElement(trending_lista, posvideo)
        dias=vid['trending']
        dias+=1
        vid['trending']=dias
        lt.changeInfo(trending_lista,posvideo,vid)
    else:
        trending = newTrending(video,trending_lista)
        lt.addLast(trending_lista, trending)

# Funciones para creacion de datos
def traduccion(categoria,catalog):
    m=catalog["categorias"]
    for i in range(1,lt.size(m)): 
        c=lt.getElement(m,i)
        if c['name'] == categoria:
            x=c['id']
            return x
            break

def newCategoria(name, id):
    """
    Esta estructura almacena las categorias con sus id respectivos.
    """
    categoria = {'name': '', 'id': '', "videos": None}
    categoria['name'] = name.lower().strip()
    categoria['id'] = id
    categoria['videos'] = lt.newList('ARRAY_LIST')
    return categoria

def newPais(name):
    """
    Crea una nueva estructura para modelar los libros de
    un autor y su promedio de ratings
    """
    pais = {'name': "", "categorias":None, "videos":None}
    pais['name'] = name.lower()
    pais['categorias'] = lt.newList('ARRAY_LIST')
    pais['videos'] = lt.newList('ARRAY_LIST')
    return pais

def newTrending(video,catalog):
    """
    Crea una nueva estructura para modelar los libros de
    un autor y su promedio de ratings
    """
    trending = {'id':None, 'name': None, 'channel':None, "categoria":None, 'pais': None, "trending":None}
    trending['id']=video['video_id']
    trending['name'] = video['title']
    trending['channel'] = video['channel_title']
    trending['categoria'] = video['category_id']
    trending['pais'] = video['country']
    trending['trending']=1
    return trending
# Funciones de consultaP

def categoria_en_lista(categoria,lista,comp,catalog):
    nueva_lista=lt.newList(datastructure='ARRAY_LIST',cmpfunction=comp)
    cat_id=traduccion(categoria,catalog)
    for i in range(1,lt.size(lista)):
        video=lt.getElement(lista,i)
        if video['category_id']==cat_id:
            lt.addLast(nueva_lista,video)
    return nueva_lista

def Pais_en_lista(pais,lista,catalog):
    nueva_lista=lt.newList(datastructure='ARRAY_LIST',cmpfunction=comparepaises)
    for i in range(1,lt.size(lista)):
        video=lt.getElement(lista,i)
        if video['country']==pais:
            lt.addLast(nueva_lista,video)
    return nueva_lista

def tags_en_lista(tag,lista,catalog):
    nueva_lista=lt.newList(datastructure='ARRAY_LIST',cmpfunction=cmpVideosByLikes)
    for i in range(1,lt.size(lista)):
        video=lt.getElement(lista,i)
        if tag in video["tags"]:
            lt.addLast(nueva_lista,video)
    return nueva_lista



def obtener_videos_pais(catalog,nombre_pais):
    posvideo = lt.isPresent(catalog['paises'], nombre_pais)
    if posvideo > 0:
        pais = lt.getElement(catalog['paises'],posvideo)
        return pais 
    return None
"""
def contar_dias_trending(video_nombre,catalog):
    contador=0
    videos=catalog['videos']
    for i in range(1,lt.size(videos)): 
        nombre=lt.getElement(videos,i)['title'].strip()
        if nombre==video_nombre:
            contador+=1
            print(contador)
    print((contador,video_nombre))
    return contador 
"""
def trending_categoria(catalog,categoria):
    cat_id=traduccion(categoria,catalog)
    indice=lt.isPresent(catalog['categorias'],cat_id)
    lista_videos=lt.getElement(catalog['categorias'],indice)['videos']
    lista_trending=lt.newList(datastructure='ARRAY_LIST',cmpfunction=comparetrending)
    for i in range(1,lt.size(lista_videos)):
        video=lt.getElement(lista_videos,i)
        addTrending(lista_trending,video)
    return lista_trending

def trending_paises(catalog,pais):
    indice=lt.isPresent(catalog['paises'],pais)
    lista_videos=lt.getElement(catalog['paises'],indice)['videos']
    lista_trending=lt.newList(datastructure='ARRAY_LIST',cmpfunction=comparetrending)
    for i in range(1,lt.size(lista_videos)):
        video=lt.getElement(lista_videos,i)
        addTrending(lista_trending,video)
    return lista_trending

def sortTrending(lista_trending):
    sorted_list = ms.sort(lista_trending, cmpVideosByTrending)
    return sorted_list

# Funciones utilizadas para comparar elementos dentro de una lista
def comparepaises(pais1, pais2):
    if (pais1.lower() == pais2['name'].lower()):
        return 0
    return -1
def comparecategorias(categoria1_id, categoria2_id):
    if (categoria1_id == categoria2_id['id']):
        return 0
    return -1
def comparetrending(trending1, trending2):
    if (trending1['title'].strip() == trending2['name'].strip()):
        return 0
    return -1
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
def cmpVideosByLikes(video1, video2):
    
    
    if (float(video1['likes']) > float(video2['likes'])):
        return True
    else:
        return False

def cmpVideosByTrending(video1, video2):
    """
    Devuelve verdadero (True) si los 'views' de video1 son menores que los del video2
    Args:
    video1: informacion del primer video que incluye su valor 'views'
    video2

    # Funciones de ordenamiento
    """
    
    if (float(video1['trending']) > float(video2['trending'])):
        return True
    else:
        return False

def sortLikes(tag,catalog,pais):
    
    pais=obtener_videos_pais(catalog,pais)
    lista_pais=pais['videos']
    lista_tags=tags_en_lista(tag,lista_pais,catalog)
    sorted_list = ms.sort(lista_tags, cmpVideosByLikes)
    return sorted_list

def sortVideos(catalog,pais,categoria):
    algoritmo="shell"
    pais=obtener_videos_pais(catalog,pais)
    lista_pais=pais['videos']
    lista_ordenar=categoria_en_lista(categoria,lista_pais, cmpVideosByViews,catalog)
    tamaño=lt.size(lista_ordenar)
    sub_list = lt.subList(lista_ordenar, 1, tamaño)
    sub_list = sub_list.copy()
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
    return sorted_list
