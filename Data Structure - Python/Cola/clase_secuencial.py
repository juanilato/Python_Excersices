
import numpy as np


class ColaSec:
    __cantidad = 0
    __primero = 0
    __ultimo = 0
    __cola = []
    __tamanio = 0
    
    def __init__(self, tamanio):
        self.__tamanio = tamanio
        self.__primero = -1
        self.__ultimo = -1
        self.__cantidad = 0
        self.__cola = np.zeros(tamanio, dtype = int)
        
        
        
    def insertar(self, elemento):
            
        if self.vacia():
            self.__cantidad += 1 
            self.__primero += 1
            self.__ultimo += 1
            self.__cola[self.__ultimo] = elemento
            
        elif self.__cantidad < self.__tamanio:
            self.__cantidad += 1 
            self.__ultimo = (self.__ultimo + 1) % self.__tamanio
            self.__cola[self.__ultimo] = elemento
            
        else:
            print("Esta lleno")

        
        
    def suprimir(self):
        if self.vacia():
            print("Vacia ")
        
        else:
            elemento = self.__cola[self.__primero] 
            self.__cola[self.__primero] = 0
            self.__primero = (self.__primero + 1) % self.__tamanio
            self.__cantidad -= 1
            
            
        return elemento 
    
    def llena(self):
        return self.__ultimo == self.__tamanio
    
    
    def vacia(self):
        return self.__cantidad == 0
        
    def __str__(self):
        print(self.__cola)
        return 
    