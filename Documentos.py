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
    def printDoc(self):
        print("Nombre de Documento: ",self.name)
        print("Path: ",self.path)
        print("ID: ",self.docID)
        print("Longitud: ",self.longitud)
        print("Cantidad de Terminos: ",self.cantTerms)
        print("Pares del Doc: ",self.pares)
        print("Descripcion: ",self.descrip)
        print("Lista Doc: ")
        print(self.listDoc)
        print("")
        return

    
