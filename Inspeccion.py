from Coleccion import Coleccion
from Documentos import Documents
from Vocabulario import Vocabulario
from Indizacion import VOCABULARY
from Indizacion import COLECCTIONS

from Consulta import searchDoc

def printDoc(pDocName):
    doc = searchDoc(pDocName)
    if doc != -1:
        doc.printDoc()
    else:
        print("No se encontro el docuento solicitado")
    return

def getTerms(pTerm):

    try:
        idx = VOCABULARY.terms.index(pTerm) - 5
        if idx < 0:
            idx = 0
    except(ValueError):
        print("No se encontro el termino solicitado")
        return
    for j in range (0, 10):
        try:
            VOCABULARY.terms[idx+j].printTerm()
        except(IndexError):
            print(j)
            break
    return

