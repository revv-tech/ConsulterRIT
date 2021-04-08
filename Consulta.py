import json

from Coleccion import Coleccion
from Coleccion import stopwords
from Indizacion import COLECCTIONS
from Indizacion import VOCABULARY
from Indizacion import directoryRunner
from Terminos import Termino
from Vocabulario import Vocabulario

#COLECCTIONS = COLECCTIONS
#VOCABULARY = VOCABULARY

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

def createHTML(pDict, pCant, pName, pConsult):
    newHTML = open("../ConsulterRIT/Consultas/" + pName + ".html", 'w')
    msg = "<html>" \
          "<head>" \
          "<title>Consulta: " + pConsult + "</title>" \
                                           "</head>" \
                                           "<body>"
    i = 1
    for key in pDict:
        if i <= pCant:
            doc = searchDoc(key)
            docInfo = "<h3>#" + str(i) + "     " + str(pDict[key]) + "     " + doc.path + "</h3>"
            docInfo += "<h4>Descripcion:</h4>" \
                       "<p>"

            for word in doc.descrip:
                docInfo += word + " "
            docInfo += "</p>"
            msg += docInfo
        else:
            break
        i += 1
    msg += "</body>" \
           "</html>"
    newHTML.write(msg)
    newHTML.close()
    return


def searchDoc(pName):
    for colection in COLECCTIONS:
        for document in colection.listaDocsData:
            if document.name == pName:
                return document
    return -1


def createTXT(pDict, pName, pConsult):
    newTXT = open("../ConsulterRIT/Consultas/" + pName + ".esc.txt", 'w')
    msg = "Cosnulta: " + pConsult + "\n" \
                                    "Escalafon: \n"
    i = 1
    for key in pDict:
        if pDict[key] > 0:
            doc = searchDoc(key)
            msg += "#" + str(i) + "\t" + str(doc.docID) + "\t" + str(pDict[key]) + "\n"
        else:
            break
        i += 1
    newTXT.write(msg)
    newTXT.close()
    return


def createConsultas(pDict, pCant, pName="consulta", pConsult=''):
    createHTML(pDict, pCant, pName, pConsult)
    createTXT(pDict, pName, pConsult)
    return


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


def jsonToObjects(dicDocs, dicColec, dicVoc):
    global COLECCTIONS
    global VOCABULARY

    COLECCTIONS = []
    terms = []

    for colec in dicColec:
        newColeccion = Coleccion(colec, dicColec[colec]["Path"], dicColec[colec]["Nombres Docs"],
                                 dicColec[colec]["LongitudAvg"], dicColec[colec]["CanDocs"])
        newColeccion.documentLoader(dicDocs)
        COLECCTIONS.append(newColeccion)

    for term in dicVoc["Vocabulario"]["Terminos"]:
        newTerm = Termino(term, dicVoc["Vocabulario"]["Terminos"][term]["ni"],
                          dicVoc["Vocabulario"]["Terminos"][term]["idf"])
        terms.append(newTerm)

    VOCABULARY = Vocabulario(dicVoc["Vocabulario"]["N"], terms, dicVoc["Vocabulario"]["Promedio de Longitud"])

    return


def main():
    directoryRunner()
    consulta = "compresión de archivos y manejo de archivos comprimidos.".lower()
    dict = sortDict(getSimDQ(consulta))
    print(dict)
    createConsultas(dict, 2, "prueba", consulta)




