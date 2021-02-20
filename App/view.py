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

def printResults(ord_books, sample=10):
    size = lt.size(ord_books)
    if size > sample:
        print("Los primeros ", sample, " libros ordenados son:")
        i=0
        while i <= sample:
            book = lt.getElement(ord_books,i)
            print('Titulo: ' + book['title'] + ' ISBN: ' +
                book['isbn'] + ' Rating: ' + book['average_rating'])
            i+=1


"""
Menu principal
"""
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')
    if int(inputs[0]) == 1:
        print("Cargando información de los archivos ....")
        catalog = initCatalog(input("Que estructura desea:SINGLE LINKED o ARRAY LIST"))
        loadData(catalog)
        print('Videos cargados: ' + str(lt.size(catalog['videos'])))
        print('Categorias cargadas: ' + str(lt.size(catalog['categorias'])))
    elif int(inputs[0]) == 2:
        print("Cargando videos con más views ....")
    elif int(inputs[0]) == 3:
        print("Cargando videos con mayor tiempo en trending en un pais ....")
    elif int(inputs[0]) == 4:
        print("Cargando video con más dias en trending ....")
    elif int(inputs[0]) == 5:
        print("Cargando videos con más likes de un tag en especifico ....")
    elif int(inputs[0]) == 5:
        size = input("Indique tamaño de la muestra: ")
        result = controller.sortBooks(catalog, int(size))
        print("Para la muestra de", size, " elementos, el tiempo (mseg) es: ",
                                          str(result[0]))
        printResults(result[1])

    else:
        sys.exit(0)
sys.exit(0)
