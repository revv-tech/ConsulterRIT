from Coleccion import stopwords
from Indizacion import VOCABULARY
from Indizacion import COLECCTIONS
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
    return VOCABULARY.terms[pTerm].idf


def getFreqFunct(pTerm, pNumDoc, pNumColecction):
    if pTerm in COLECCTIONS[pNumColecction].listaDocsData[pNumDoc].dic:
        freq = COLECCTIONS[pNumColecction].listaDocsData[pNumDoc].dic[pTerm]
        denominador = freq * (k + 1)
        divisor = freq + k * (1 - b + b * (COLECCTIONS[pNumColecction].cantTerms / VOCABULARY.avgdl))
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
                simDQ[listDocs[documentNUM].name] += getSimDQ(term) * getFreqFunct(term, documentNUM, colectionNUM)
            documentNUM += 1
        colectionNUM += 1
    return simDQ


def sortDict(pDict):
    keys = {key: v for key, v in sorted(pDict.items(), key=lambda item: item[1])}
    keys = [*keys]
    return keys.reverse()

def main():
    directoryRunner()
    consulta = "compresión de archivos y manejo de archivos comprimidos"
    dict = getSimDQ(consulta)
    dictSorted = sortDict(dict)
    print(dictSorted)

main()




