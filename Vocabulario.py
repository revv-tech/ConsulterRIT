#Vocabulario

class Vocabulario:

    def __init__(self, N = 0, terms = [], avgdl = 0):

        self.N = N
        self.terms = terms
        self.avgdl = avgdl
        self.jsonFile = {}
    
    def calcIDF(self):
        for term in self.terms:

            term.calcIDF(self.N)
            
        return
    
    def addTerms(self,listaTerms):
        
        if self.terms == []:
            
            self.terms = listaTerms
            
        else:
            for elem in listaTerms:
                for termOficial in self.terms:

                    if elem.term == termOficial.term:

                        termOficial.ni = termOficial.ni + elem.ni

                else:

                    self.terms.append(elem)

    # Ordena Vocabulario Alfabeticamente
    def sortVoc(self):
        self.terms = sorted(self.terms, key=lambda x: x.term, reverse=True)


    def print(self):
        print("Vocabulario")
        print("Cantidad Documentos: ", self.N)
        print("Vocabulario General: ")
        for term in self.terms:
            term.printTerm()


    def toJsonFile(self):
        self.jsonFile["Vocabulario"] = {
            "N" : self.N,
            "Promedio de Longitud" : self.avgdl,
            "Terminos" : self.termsToJson()
        }
        return

    def termsToJson(self):
        dic = {}
        for term in self.terms:
            term.toJsonFile()
            dic[term.term] = term.jsonFile
        return dic