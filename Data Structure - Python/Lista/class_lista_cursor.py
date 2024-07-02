import numpy as np
from class_nodo_cursor import Nodo

class ListaCursor:
    
    __disp = 0
    __cab = -1
    
    def __init__(self, tamanio):
        self.__arr = np.empty(tamanio, dtype=Nodo)
        for i in range(0, tamanio-1):
            self.__arr[i] = Nodo()
            
            self.__arr[i].sig(i+1)
            
        self.__arr[tamanio-1] = Nodo()
        self.__arr[tamanio-1].sig(-1)
        
    
    def insertar(self, dato):
        
        if self.__disp != -1:
           
            self.__arr[self.__disp].info(dato)
            auxDisp = self.__arr[self.__disp].getSig()
            
            if self.__cab == -1 or dato < self.__arr[self.__cab].getInfo(): 
                
                self.__arr[self.__disp].sig(self.__cab)
                self.__cab = self.__disp
                self.__disp = auxDisp
                
            else:
                
                aux = self.__cab
                
                while aux != -1 and dato > self.__arr[aux].getInfo():
                    ant = aux
                    aux = self.__arr[aux].getSig()
                
                self.__arr[self.__disp].sig(self.__arr[ant].getSig()) 
                self.__arr[ant].sig(self.__disp) 
                self.__disp = auxDisp
     
    def suprimir(self, dato):
        aux = self.__cab
        band = False
        
        if self.__cab != -1:
            while aux != -1 and self.__arr[aux].getInfo() != dato:
                ant = aux
                aux = self.__arr[aux].getSig()
                
                band = True
                
            

               
            if aux != -1 and band:
                
                self.__arr[ant].sig(self.__arr[aux].getSig())
            
                self.__arr[aux].sig(self.__disp)
                self.__disp = aux
                
            else:
                
                self.__cab = self.__arr[aux].getSig()
                self.__arr[aux].sig(self.__disp)
                self.__disp = aux
                
                              
            
    def muestra(self):
        aux = self.__cab 
        while aux != -1:
            print(self.__arr[aux].getInfo())
            aux = self.__arr[aux].getSig()
                