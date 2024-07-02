from zope.interface import Interface


#from zope.interface import implementer


    
class Manejador(Interface):
    
    def insertarElemento(self, lista, posicion, elemento):
        if posicion >= 0 and posicion <= len(lista):
            lista[posicion] = elemento
        else:
            raise Exception("Posición incorrecta")
    
    def agregarElemento(self, lista, posicionFin, elemento):
        if posicionFin == len(lista):
            lista[posicionFin] = elemento
    
    def mostrarElemento(self, lista, posicion):
        if posicion >= 0 and posicion <= len(lista):
            print(lista[posicion])
        else:
            raise Exception("Posición incorrecta")
            
