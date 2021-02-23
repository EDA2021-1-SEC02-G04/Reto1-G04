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

def printResults(videos, sample=10):
    size = lt.size(videos)
    if size > sample:
        print("Los ", sample, " videos con más views son:")
        i=1
        while i <= sample:
            video = lt.getElement(videos,i)
            print('Titulo: ' + video['title'] + " views: " + video["views"]+ " canal: "
            + video["channel_title"] + " fecha trending: "+ video["trending_date"]+" Fecha de publicación: "
            + video["publish_time"] + " likes: "+video["likes"] +" dislikes: " +video["dislikes"])
            i+=1


"""
Menu principal
"""
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')
    if int(inputs[0]) == 1:
        print("Cargando información de los archivos ....")
        catalog = initCatalog(input("Que estructura desea, SINGLE_LINKED o ARRAY_LIST: "))
        loadData(catalog)
        print('Videos cargados: ' + str(lt.size(catalog['videos'])))
        print('Categorias cargadas: ' + str(lt.size(catalog['categorias'])))
    elif int(inputs[0]) == 2:
        print("Cargando videos con más views ....")
        size = input("Indique tamaño de la muestra: ")
        algoritmo=input("¿Con que algoritmo quiere que se desarrolle el proceso: shell,insertion o selection?")
        result = controller.sortVideos(catalog, int(size),algoritmo)

        print("Para la muestra de", size, " videos, el tiempo (mseg) es: ", str(result[1]))
        printResults(result[0])
    elif int(inputs[0]) == 3:
        print("Cargando videos con mayor tiempo en trending en un pais ....")
    elif int(inputs[0]) == 4:
        print("Cargando video con más dias en trending ....")
    elif int(inputs[0]) == 5:
        print("Cargando videos con más likes de un tag en especifico ....")


    else:
        sys.exit(0)
sys.exit(0)
