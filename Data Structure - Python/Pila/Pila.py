import numpy as np


class Pila:
    __tope=0
    __cant=0
    __arreglo=[]
    
    def __init__(self,cant):
        self.__tope= 0
        self.__cant=cant
        self.__arreglo= np.empty(cant)
        
        
    def apilar(self,elemento):
        if not self.llena():
            self.__arreglo[self.__tope]=elemento
            self.__tope += 1
            
 

            
    def desapilar(self):
        if not self.vacia():
            self.__tope -= 1
            elemento = self.__arreglo[self.__tope]
            self.__arreglo[self.__tope] = None
            
        return elemento
    
    def tope(self):
        return self.__tope
    
    
    def vacia(self):
        return self.__tope == 0
    
    def llena(self):
        return self.__cant==self.__tope
    
    def print(self):
        list=[]
        while not self.vacia() :

            ele=self.desapilar()
            print(ele)
            list.append(ele)
            
        list.reverse()
        for i in list:
            self.apilar(i)
            


