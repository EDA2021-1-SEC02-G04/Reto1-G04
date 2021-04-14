"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad
 * de Los Andes
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
import sys
import controller
from DISClib.ADT import list as lt
assert cf


"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""

def printMenu():
    print("Bienvenido")
    print("1- Cargar información en el catálogo")
    print("2- Videos con más views")
    print("3- Video con mayor tiempo en trending de un pais")
    print("4- Video que más dias ha sido trending en una categoria")
    print("5- Videos con más likes en un pais con un tag en especifico")
    print("0- Salir")

def initCatalog(estructura:str):
    """
    Inicializa el catalogo de videos
    """
    return controller.initCatalog(estructura)


def loadData(catalog):
    
    """
    Carga los videos en la estructura de datos
    """
    controller.loadData(catalog)

def printResults(videos, sample):
    size = lt.size(videos)
    if size > sample:
        print("Los ", sample, " videos con más views son:")
        i=1
        while i <= sample:
            video = lt.getElement(videos,i)
            print("Trending date: "+ video["trending_date"]+ ' Titulo: ' + video['title'] + " Canal: "
            + video["channel_title"]+  " Fecha de publicación: "
            + video["publish_time"]+" views: " + video["views"]  + " likes: "+video["likes"] +" dislikes: " +video["dislikes"])
            i+=1
def printTags(videos, sample):
    size = lt.size(videos)
    if size > sample:
        print("Los ", sample, " videos con más likes son:")
        i=1
        while i <= sample:
            video = lt.getElement(videos,i)
            print(' Titulo: ' + video['title'] + " Canal: "
            + video["channel_title"]+  " Fecha de publicación: "
            + video["publish_time"]+" views: " + video["views"]  + " likes: "+video["likes"] +" dislikes: " +video["dislikes"]+" Tags:: " +video["tags"]+" Pais: "+video["country"])
            i+=1


def print_categoria_trending(result):
    video=lt.getElement(result,1)
    print('Titulo: ' + video['name'] + " Canal: "
            + video["channel"]+  " Categoria_id: "
            + str(video["categoria"])+" Días Trending: " + str(video["trending"])+" Pais: "+video["pais"])
    
def print_categoria_pais(result):
    video=lt.getElement(result,1)
    print('Titulo: ' + video['name'] + " Canal: "
            + video["channel"]+  " Días Trending: " + str(video["trending"])+ " Pais: "+video["pais"])
    return    
"""
Menu principal
"""
continuar=True
while continuar==True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')
    if int(inputs[0]) == 1:
        print("Cargando información de los archivos ....")
        catalog = initCatalog("ARRAY_LIST")
        loadData(catalog)
        print('Videos cargados: ' + str(lt.size(catalog['videos'])))
        print('Categorias cargadas: ' + str(lt.size(catalog['categorias'])))
        print('Paises cargados: ' + str(lt.size(catalog['paises'])))
        print("Tiempo [ms]: ", f"{answer[0]:.3f}", "  ||  ",
              "Memoria [kB]: ", f"{answer[1]:.3f}")
    elif int(inputs[0]) == 2:
        numeroT=int(input("¿Que tan grande quiere que sea el top? "))
        pais= input("Indique el pais que desea analizar: ").lower()
        categoria= input("Indique la categoria que desea analizar: ").lower()
        print("Cargando videos con más views ....")
        answer = controller.sortVideos(catalog,pais,categoria)
        printResults(answer[2],numeroT)
        print("Tiempo [ms]: ", f"{answer[0]:.3f}", "  ||  ",
              "Memoria [kB]: ", f"{answer[1]:.3f}")
    elif int(inputs[0]) == 3:
        print("Cargando videos con mayor tiempo en trending en un pais ....")
        pais=input("Indique el pais que desea analizar: ")
        answer=controller.trending_paises(catalog,pais)
        print_categoria_pais(answer[2])
        print("Tiempo [ms]: ", f"{answer[0]:.3f}", "  ||  ",
              "Memoria [kB]: ", f"{answer[1]:.3f}")
    elif int(inputs[0]) == 4:
        categoria= input("Indique la categoria que desea analizar: ").lower()
        print("Cargando video con más dias en trending en una categoria ....")
        answer = controller.trending_categoria(catalog,categoria)
        print_categoria_trending(answer[2])
        print("Tiempo [ms]: ", f"{answer[0]:.3f}", "  ||  ",
              "Memoria [kB]: ", f"{answer[1]:.3f}")
    elif int(inputs[0]) == 5:
        print("Cargando videos con más likes de un tag en especifico ....")
        tag=input("Indique el tag: ")
        pais= input("Indique el pais que desea analizar: ").lower()
        answer=controller.sortLikes(tag,catalog,pais)
        numeroT=int(input("¿Que tan grande quiere que sea el top? "))
        printTags(answer[2],numeroT)
        print("Tiempo [ms]: ", f"{answer[0]:.3f}", "  ||  ",
              "Memoria [kB]: ", f"{answer[1]:.3f}")
        

    elif int(inputs[0]) == 0:
        continuar=False

    else:
        sys.exit(0)
sys.exit(0)
