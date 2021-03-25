import math

class Termino:

    def __init__(self,term,ni):

        # Char del termino
        self.term = term
        # Cantidad de documentos en los que aparece
        self.ni = ni
        # Valor de idf en BM-25
        self.idf = 0

    def calcIDF(self,N):

        idf = math.log((((N - self.ni - 0.5)) / ((self.ni - 0.5))), 2)
        if idf < 0:
            self.idf = 0
        else:
            self.idf = idf
    def addNi(self):
        self.ni = self.ni + 1

    def print(self):
        print("")
        print("Termino: ", self.term)
        print("Cantidad de Documentos (ni): ",self.ni)
        print("idf: ",self.idf)
        print("")
