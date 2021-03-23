# Coleccion
import csv
import os
import re
from contextlib import suppress
from Documentos import Documents

stopwords = ["a", "ante", "bajo", "cabe", "con", "contra", "de", "desde", "e", "el", "en", "entre", "hacia",
             "hasta", "ni", "la", "le", "lo", "los", "las", "o", "para", "pero", "por", "que", "segun", "sin",
             "so", "uno", "unas", "unos", "y", "sobre", "tras", "u", "un", "una"]


class Coleccion:

    def __init__(self, name, path, lista):

        # Nombre del Directorio
        self.name = name
        # Ruta completa del Directorio
        self.path = path
        # Numero de documentos
        self.cantDoc = 0
        # Longitud Promedio de Documentos
        self.longitudAvg = 0
        # Lista de los documentos nombres
        self.listaDocsName = lista
        # Lista Documentos en Objetos
        self.listaDocsData = []

    # Filtrador de Terminos
    def filterTerms(self, listaDoc):

        newList = []
        while listaDoc:
            # Elimina strings vacios y los guines sueltos de la lista del documento
            if listaDoc[0] != '' and listaDoc[0] != '-':
                # Filtra los stopwords
                if not (listaDoc[0].lower() in stopwords):
                    # Agrega el termino a la nueva lista
                    newList.append(listaDoc[0].lower())
            # Siguiente termino
            listaDoc = listaDoc[1:]
        # Retorna lista de terminos adecuados al formato
        newList = self.joinWords(newList)
        newList = self.splitDots(newList)
        newList = self.searchParameters(newList)
        return newList

    # Crea la lista de Documentos
    def documentCreator(self):
        if self.listaDocsName == []:
            return []
        else:
            idDoc = 0
            for doc in self.listaDocsName:
                pathDoc = self.path + "/" + doc
                # Poner filtrador
                listaDoc = self.filterTerms(self.leerDoc(pathDoc))
#<<<<<<< Updated upstream
                #Nuevo Doc
                newDoc = Documents(listaDoc,idDoc,pathDoc,doc)
                newDoc.docCalcs()
                #Agregar doc
                self.listaDocsData.append(newDoc)
                #newDoc.printDoc()
                idDoc = idDoc + 1

            self.cantDoc = idDoc
            self.calcProm()
            return
        """"=======
                        # Nuevo Doc
                        newDoc = Documents(listaDoc, idDoc, pathDoc, doc)
                        # Agregar doc
        >>>>>>> Stashed changes"""

    def leerDoc(self, archivo):
        lista = []
        fo = open(archivo, "r")
        reader = csv.reader(fo)

        for row in reader:
            if row:
                segmentoAux = row[0].split(" ")
                segmentoCompleto = segmentoAux + self.eliminaComas(row[1:])
                lista += segmentoCompleto

        return lista

    def eliminaComas(self, segmento):

        newList = []
        for row in segmento:
            raw = row.split(" ")
            for x in raw:
                if x != '':
                    newList.append(x)

        return newList

    def calcProm(self):
        prom = 0
        for doc in self.listaDocsData:
            
            prom = prom + doc.longitud
            
        self.longitudAvg = prom/len(self.listaDocsData)
            
    def printColeccion(self):
        print("Nombre de Coleccion: ", self.name)
        print("Path: ", self.path)
        print("Cantidad de Docs: ", self.cantDoc)
        print("Cantidad Promedio Long.: ", self.longitudAvg)
        print("Lista de los documentos: ", self.listaDocsName)
        print("")
        return

    def joinWords(self, listWords):
        cont = 1
        while cont < len(listWords):
            word = listWords[cont - 1]
            if word[-1:] == '-' and listWords[cont] != '':
                listWords[cont - 1] = word.removesuffix('-') + listWords[cont]
                listWords.pop(cont)
            cont += 1
        return listWords

    # noinspection PyUnreachableCode
    def splitDots(self, listWords):
        for word in listWords:
            if word[0] != "." and word[-1:] != '.' and not re.search("\.\.", word):
                listSplited = word.split(".")
                with suppress(ValueError):
                    while True:
                        listSplited.remove("")
                if len(listSplited) > 1:
                    for fragment in listSplited:
                        if re.match(".?[A-Za-z].?", fragment):
                            listWords.append(fragment)
        return listWords

    def searchParameters(self, listWords):
        for word in listWords:
            if word[:2] == "--":
                listWords.append(word[2:])
                listWords.append("@" + word[2:])
                listWords.remove(word)
        return listWords
    #