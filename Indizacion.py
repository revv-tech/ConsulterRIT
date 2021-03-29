import os
import csv
import re
from Coleccion import Coleccion
from Vocabulario import Vocabulario

COLECCTIONS = []
VOCABULARY = Vocabulario()


# ================== #
# MANEJO DE ARCHIVOS #
# ================== #
# E: El path del archivo, un string con formato de lista
# S: Ninguna
# D: Guarda el archivo

def guardar(archivo, strLista):
    fo = open(archivo, "w")
    fo.write(strLista)
    fo.close()


# E: La lista con las sublistas de cada instruccion
# S: Una lista
# D: lee la lista y elimina espacios en blanco

def eliminaEspacios(archivoListas):
    for row in archivoListas:
        if "" in row:
            while "" in row:
                row.remove("")

    return archivoListas


# E: El texto de un archivo
# S: Una lista de los elementos de las
# D: Lee el archivo, separa sus elementos y los almacena en una lista de sublistas


def leer(archivo):
    lista = []
    fo = open(archivo, "r")
    reader = csv.reader(fo)
    # print(reader)
    for row in reader:
        if row:
            segmentoAux = row[0].split(" ")
            segmentoCompleto = segmentoAux + eliminaComas(row[1:])
            lista += segmentoCompleto

    return lista


# =====================

# E: El texto del archivo
# S: No tiene
# D: Elimina los comentarios del archivo de texto para convertirlos en lista
def eliminaComas(segmento):
    newList = []
    for row in segmento:
        raw = row.split(" ")
        for x in raw:
            if x != '':
                newList.append(x)

    return newList


# E: El path del archivo
# S:Una lista
# D:lee un archivo y hace las validaciones para colocarlo en la lista
def cargarArchivo(archivo):
    strResultado = leer(archivo)
    if strResultado != "":
        return strResultado
    else:
        return []


# PRUEBA
nameFile = "C:/Users/Marco/Desktop/Documentos TEC/ConsulterRIT/man.es/man1/411toppm.1"


# print(cargarArchivo(nameFile))

# LEER DIRECTORIOS
# E: No tiene
# S: Aun no se
# D: Revisa los files de cada carpeta del directorio Man.es y hace una lista con los nombres de sus files

def directoryRunner():
    # Path
    path = "../ConsulterRIT/man.es"
    # Subcarpetas de Man.es
    carpetsMan_ES = os.listdir(path)
    # Cantidad de Documentos
    N = 0
    # Crea vocabulario
    i = 1
    global VOCABULARY
    # Ciclo que crea listas con los nombres de los documentos que si son aceptados para el proceso
    while i > 0:
        # Saca el nombre de cada subcarpeta de Man.es
        nameCarpet = "man4"
        # Saca la lista de Archivos de Man.es
        contentCarpet = os.listdir(path + "/" + nameCarpet)
        # Lista con los documentos que deben ser aceptados por la terminacion correcta
        filesCarpet = carpetListFilter(contentCarpet)
        # CREACION DE COLECCION
        newColeccion = Coleccion(nameCarpet, path + "/" + nameCarpet, filesCarpet)
        # Crea lista de Documentos
        newColeccion.documentCreator()
        # Actualizar cantidad de Documentos
        N = N + newColeccion.cantDoc
        newColeccion.printColeccion()
        # Agrega termino al vocabulario
        VOCABULARY.addTerms(newColeccion.vocabulario)
        # Agregar a COLECCTIONS
        COLECCTIONS.append(newColeccion)
        VOCABULARY.avgdl += COLECCTIONS[0].longitudAvg  # DESCOMPONER LISTA
        i -= 1
        carpetsMan_ES = carpetsMan_ES[1:]
    # Agrega la cantidad de documentos al vocabulario
    VOCABULARY.N = N
    # Calcula el idf para cada termino
    VOCABULARY.calcIDF()
    VOCABULARY.avgdl = VOCABULARY.avgdl / len(COLECCTIONS)
    # Vocab.sortVoc()
    # Imprime el vocabulario
    return


# Filtrador de Lista de Documentos para que tengan terminacion correcta
def carpetListFilter(listFiles):
    correctFiles = []
    for elem in listFiles:

        if re.match("\.[12345678]", elem[-2:]):
            correctFiles.append(elem)

    return correctFiles


#directoryRunner()
