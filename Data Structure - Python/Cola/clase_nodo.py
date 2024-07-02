
class Nodo:
    __dato: int
    __siguiente: object
    def __init__(self,dato):
        self.__dato = dato
        self.__siguiente = None
        
    def setSiguiente(self, siguiente):
        self.__siguiente = siguiente
        
    def getSiguiente(self):
        return self.__siguiente
    
    def getDato(self):
        return self.__dato
    

        
    def __str__(self):
        return str(self.__dato)