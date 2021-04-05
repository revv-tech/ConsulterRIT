import json

from Coleccion import stopwords
from Indizacion import VOCABULARY
from Indizacion import COLECCTIONS

import _json
from Coleccion import Coleccion
from Vocabulario import Vocabulario
from Terminos import Termino

from Indizacion import directoryRunner

k = 1.2
b = 0.75


def getConsultTerms(pConsult):
    terms = pConsult.split(" ")
    terms = cleanTerms(terms)
    return terms


def cleanTerms(pTerms):
    newTerms = []
    for term in pTerms:
        if (term not in newTerms) and (term not in stopwords):
            newTerms.append(term)
    return newTerms


def getIDF(pTerm):
    """try:
        index = VOCABULARY.terms.index(pTerm)
        return VOCABULARY.terms[index].idf
    except(ValueError):
        return 0"""
    terms = VOCABULARY.terms
    i = 0
    while i < len(VOCABULARY.terms):
        if pTerm == terms[i].term:
            return VOCABULARY.terms[i].idf
        i += 1
    return 0


def getFreqFunct(pTerm, pNumDoc, pNumColecction):
    if pTerm in COLECCTIONS[pNumColecction].listaDocsData[pNumDoc].dic:
        freq = COLECCTIONS[pNumColecction].listaDocsData[pNumDoc].dic[pTerm]
        denominador = freq * (k + 1)
        divisor = freq + k * (
                    1 - b + b * (COLECCTIONS[pNumColecction].listaDocsData[pNumDoc].cantTerms / VOCABULARY.avgdl))
        return denominador / divisor
    return 0


def getSimDQ(pConsult):
    terms = getConsultTerms(pConsult)
    simDQ = {}
    colectionNUM = 0
    while colectionNUM < len(COLECCTIONS):
        documentNUM = 0
        listDocs = COLECCTIONS[colectionNUM].listaDocsData
        while documentNUM < len(listDocs):
            simDQ[listDocs[documentNUM].name] = 0
            for term in terms:
                simDQ[listDocs[documentNUM].name] += getIDF(term) * getFreqFunct(term, documentNUM, colectionNUM)
            documentNUM += 1
        colectionNUM += 1
    return simDQ


def sortDict(pDict):
    keys = dict(sorted(pDict.items(), key=lambda item: item[1], reverse=True))

    return keys
# Creador de archivos
def jsonReader():
    with open("../ConsulterRIT/Indizacion/documentos.json") as file:
        dicDocs = json.load(file)
    with open("../ConsulterRIT/Indizacion/colecciones.json") as file:
        dicColec = json.load(file)
    with open("../ConsulterRIT/Indizacion/vocabulario.json") as file:
        dicVoc = json.load(file)

    jsonToObjects(dicDocs, dicColec, dicVoc)
    return

def jsonToObjects(dicDocs,dicColec,dicVoc):
    global COLECCTIONS
    global VOCABULARY

    COLECCTIONS = []
    terms = []

    for colec in dicColec:

        newColeccion = Coleccion(colec, dicColec[colec]["Path"], dicColec[colec]["Nombres Docs"],dicColec[colec]["LongitudAvg"],dicColec[colec]["CanDocs"])
        newColeccion.documentLoader(dicDocs)
        COLECCTIONS.append(newColeccion)

    for term in dicVoc["Vocabulario"]["Terminos"]:
        newTerm = Termino(term,dicVoc["Vocabulario"]["Terminos"][term]["ni"], dicVoc["Vocabulario"]["Terminos"][term]["idf"])
        terms.append(newTerm)

    VOCABULARY = Vocabulario(dicVoc["Vocabulario"]["N"],terms,dicVoc["Vocabulario"]["Promedio de Longitud"])




    return

def main():

    directoryRunner()
    consulta = "compresión de archivos y manejo de archivos comprimidos.".lower()
    dic = sortDict(getSimDQ(consulta))






main()
#jsonReader()