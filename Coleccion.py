# Coleccion
import csv
import re
from contextlib import suppress
from Documentos import Documents
from Terminos import Termino

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
        # Lista con el vocabulario de la coleccion
        self.vocabulario = []
        # Json
        self.jsonFile = {}

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
        self.cleanList(newList)
        return newList

    # Crea la lista de Documentos
    def documentCreator(self):
        if self.listaDocsName == []:
            return []
        else:
            idDoc = 0
            for doc in self.listaDocsName:
                pathDoc = self.path + "/" + doc
                # Lista filtrada con los terminos de doc
                listaDoc = self.filterTerms(self.leerDoc(pathDoc))
                # Nuevo Doc
                newDoc = Documents(idDoc, pathDoc, doc)
                newDoc.docCalcs(listaDoc)
                print(doc)
                # Agrega terminos a vocabulario de coleccion
                self.termAdder(newDoc.pares)
                # Agregar doc
                self.listaDocsData.append(newDoc)
                # newDoc.printDoc()
                idDoc = idDoc + 1

            self.cantDoc = idDoc
            
            self.calcProm()
            
            return

    # Funcion que agrega los terminos de cada documento
    def termAdder(self, listaPares):

        for par in listaPares:

            term = par[0]

            for termData in self.vocabulario:

                if term == termData.term:
                    termData.addNi()
                    break

            else:

                newTerm = Termino(term, 1)
                self.vocabulario.append(newTerm)

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
        print("Vocabulario de la Coleccion: ")
        print(self.vocabulario)
        return

    def joinWords(self, listWords, cont):
        word = listWords[cont - 1]
        if (word[-1:] == '-' or word[-1:] == '­') and listWords[cont] != '':
            listWords[cont - 1] = word.removesuffix('-') + listWords[cont]
            listWords.pop(cont)
        return

    # noinspection PyUnreachableCode
    def splitDots(self, listWords, word):
        if word != '':
            if word[0] != "." and word[-1:] != '.' and not re.search("\.\.", word):
                listSplited = word.split(".")
                with suppress(ValueError):
                    while True:
                        listSplited.remove("")
                if len(listSplited) > 1:
                    for fragment in listSplited:
                        if re.match(".?[A-Za-z].?", fragment):
                            listWords.append(fragment)
        else:
            listWords.remove(word)
        return

    def searchParameters(self, listWords, word):
        if word[:2] == "--":
            listWords.append(word[2:])
            listWords.append("@" + word[2:])
            listWords.remove(word)
        return
      
    def deleteChars(self, word):
        if word[0] == '\"' or word[0] == '(':
            word = word[1:]
        if re.match("[\":]", word[-1:]):
            word = word[:-1]
        if word[-1:] == ')' and not re.search("\(", word):
            word = word[:-1]
        return word

    def cleanList(self, pListWords):
        cont = 0
        while cont < len(pListWords):
            pListWords[cont] = self.deleteChars(pListWords[cont])
            if cont != len(pListWords) - 1:
                self.joinWords(pListWords, cont + 1)
            self.searchParameters(pListWords, pListWords[cont])
            self.splitDots(pListWords, pListWords[cont])
            cont += 1
        return
    def toJson(self):
        self.docsToJson()
        self.jsonFile[self.name] = []
        self.jsonFile[self.name].append({
            "Path": self.path,
            "CanDocs": self.cantDoc,
            "LongitudAvg": self.longitudAvg
        })


        return
    def docsToJson(self):
        docs  = {}
        for doc in self.listaDocsData:
            doc.toJson()
            docs[doc.name] = doc.jsonFile
        return docs