from Consulta import searchDoc
from Indizacion import VOCABULARY, directoryRunner


def printDoc(pDocName):
    doc = searchDoc(pDocName)
    if doc != -1:
        doc.printDoc()
    else:
        print("No se encontro el docuento solicitado")
    return


def printTerms(pTerm):
    idx = 0
    for i in range (0, len(VOCABULARY.terms)):
        if VOCABULARY.terms[i].term == pTerm:
            idx = i - 5
            break
    if idx < 0:
        idx = 0
    for j in range(0, 10):
        try:
            VOCABULARY.terms[idx + j].printTerm()
        except(IndexError):
            print(j)
            break
    return