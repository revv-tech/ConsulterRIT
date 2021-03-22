#Documentos

class Documents:

    def __init__(self,listDoc,docID,path,nameDoc):

        #Nombre del Doc
        self.name = nameDoc
        #Lista de Terminos del Documento
        self.listDoc = listDoc
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
        print("Lista Doc: ")
        print(self.listDoc)
        print("")
        return
    
    #Dada la lista filtrada del documentos
    def docCalcs(self):
        
        alphabeticList = sorted(set(self.listDoc))
        self.dic = dict((term,self.listDoc.count(term)) for term in set(self.listDoc))
        self.cantTerms = len(self.dic)
        self.listPares(alphabeticList,self.dic)
        
        if len(self.listDoc) <= 200:
            self.descrip = self.listDoc
        else:
            i = 0
            while i < 200:
                self.descrip.append(self.listDoc[i])
                i = i + 1

    def listPares(self,alphList,dic):
        
        pares = []

        for elem in alphList:
            self.longitud = self.longitud + dic[elem]
            par = [elem,dic[elem]]
            pares.append(par)
            
        self.pares = pares
           
    
