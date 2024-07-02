
class Conjunto():
    def __init__(self, datos):
        self.__lista = []
        for num in datos:
            if type(num) == int:
                self.__lista.append(num)
            else:
                print( num + ", no se pudo ingresar, ya que no es un entero")
    
    def muestra(self):
       print(self.__lista)
    def __add__(self, otro):
        listaNueva = []
        for num in self.__lista:
            listaNueva.append(num)    
        for num_otro in otro.__lista:
            bandera = False
            for num in self.__lista:
                if num_otro == num:
                    bandera = True 
            if bandera == False: 
                listaNueva.append(num_otro)
        return Conjunto(listaNueva)
    
    def __sub__(self, otro):
        listaNueva = []
        for num in self.__lista:
            bandera = False
            for num_otro in otro.__lista:
                if num_otro == num:
                    bandera = True
            if bandera == False:
                listaNueva.append(num)
        
        return Conjunto(listaNueva)
    
    def __eq__(self, otro):
        cantidad = 0
        if len(self.__lista) == len(otro.__lista):
            for num in self.__lista:
                bandera = False
                for num_otro in otro.__lista:
                    if num_otro == num:
                        bandera = True
                if bandera == True:
                    cantidad += 1
        if cantidad == len(self.__lista):
            banderaDevolver = True
        else:
            banderaDevolver = False
        return banderaDevolver   
                
                
    