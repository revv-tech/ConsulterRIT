#Documentos

class Documents:

    def __init__(self,docID,path,nameDoc):

        #Nombre del Doc
        self.name = nameDoc
        #Lista de Terminos del Documento
        #self.listDoc = listDoc
        #Numero consecutivo unico generado aleatoriamente
        self.docID = docID
        #Ruta del Documento
        self.path = path
        #Descripcion
        self.descrip = []
        #Numero de terminos distintos del documento
        self.cantTerms = 0
        #Longitud del Documento (Suma de las frecuencias de todos los terminos del documento
        self.longitud = 0
        #Lista de Vectores (Orden Alfabetico)
        self.pares = []
        #Diccionario Palabras
        self.dic = {}
        # Json
        self.jsonFile = {}
        
    def printDoc(self):
        print("Nombre de Documento: ",self.name)
        print("Path: ",self.path)
        print("ID: ",self.docID)
        print("Longitud: ",self.longitud)
        print("Cantidad de Terminos: ",self.cantTerms)
        print("Pares del Doc: ",self.pares)
        print("")
        print("Descripcion: ",self.descrip)
        print("")
        print("Diccionario: ", self.dic)
        print("")
        return
    
    #Dada la lista filtrada del documentos
    def docCalcs(self,listDoc):
        
        alphabeticList = sorted(set(listDoc))
        self.dic = dict((term,listDoc.count(term)) for term in set(listDoc))
        self.cantTerms = len(self.dic)
        self.listPares(alphabeticList,self.dic)
        
        if len(listDoc) <= 200:
            self.descrip = listDoc
        else:
            i = 0
            while i < 200:
                self.descrip.append(listDoc[i])
                i = i + 1

    def listPares(self,alphList,dic):
        
        pares = []

        for elem in alphList:

            self.longitud = self.longitud + dic[elem]
            par = [elem,dic[elem]]
            pares.append(par)

        self.pares = pares
        self.dic = {pares[i][0]: pares[i][1] for i in range(0, len(pares), 2)}

    def toJson(self):
        self.jsonFile = {
            "DocID" : self.docID,
            "Path"  : self.path,
            "Descripcion" : self.descrip,
            "CanTerm" : self.cantTerms,
            "Longitud" : self.longitud,
            "Pares" : self.dic
        }
        return
    
