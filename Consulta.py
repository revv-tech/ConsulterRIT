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
        divisor = freq + k * (1 - b + b * (COLECCTIONS[pNumColecction].listaDocsData[pNumDoc].cantTerms / VOCABULARY.avgdl))
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
    keys = dict(sorted(pDict.items(), key=lambda item: item[1],reverse=True))

    return keys

def main():
    directoryRunner()
    consulta = "compresión de archivos y manejo de archivos comprimidos.".lower()
    dict = getSimDQ(consulta)
    #print(dict)
    dictSorted = sortDict(dict)
    i = 35
    for word in dictSorted:
        if i == 0:
            return
        print(word,dictSorted[word])
        i -= 1

main()




