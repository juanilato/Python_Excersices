
from clase_nodo import Nodo

class ColaEncadenada:
    __inicio: Nodo
    __final: Nodo
    __cantidad: int
    
    def __init__(self):
        self.__inicio = None
        self.__final = None
        self.__cantidad = 0
        
    
    def insertar(self, dato):
        nodo = Nodo(dato) #carga dado en un nodo
        #si esta vacío guarda principio y final en nodo y guarda un anterior para futuros cambios
        
        
        if self.vacio():
            
            nodo.setSiguiente(None)
            
            self.__final = nodo
            self.__inicio = nodo
            
            
        
        #si no esta vacio setea el siguiente del anterior guardado en el nuevo nodo
        #luego setea el final al nuevo nodo y asigna un valor al siguiente... None
        #vuelve a guardar el anterior
        else:
            
            self.__final.setSiguiente(nodo) 
            
            self.__final = nodo
            
            self.__final.setSiguiente(None)
            
            
            
        self.__cantidad += 1
    
    #Si no esta vacio getea dato del inicio y setea inicio al siguiente del inicio
    def suprimir(self):
       if not self.vacio():
        dato = self.__inicio.getDato()
        self.__inicio = self.__inicio.getSiguiente()
        self.__cantidad -= 1
        return dato
    

    def getCantidad(self):
        return self.__cantidad
    #Esta vacio si la cantidad es 0
    def vacio(self):
        return self.__cantidad == 0
       