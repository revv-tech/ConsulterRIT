from Consulta import searchDoc, indexTerm, printTerm

def printDoc(pDocName):
    doc = searchDoc(pDocName)
    if doc != -1:
        doc.printDoc()
    else:
        print("No se encontro el docuento solicitado")
    return


def printTerms(pTerm):
    idx = indexTerm(pTerm)
    for j in range(0, 10):
        try:
            printTerm(idx + j)
        except(IndexError):
            print(j)
            break
    return
