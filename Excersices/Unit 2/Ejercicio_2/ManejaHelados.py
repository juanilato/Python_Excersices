from clase_helado import Helado

class ManejaHelados:
    def __init__(self):
        self.__lista = []
    def addHelado(self, gramos, precio, sabores):
        helado = Helado(gramos, precio)
        helado.addSabor(sabores, len(sabores))
        self.__lista.append(helado)
    def muestraHelados(self):
        for helado in self.__lista:
            print(helado)
    def cuentaGramos(self, cod):
        sumador = 0
        for helado in self.__lista:
            if helado.buscaSabor(cod) != -1:
                sumador += helado.getGramos() / helado.getLen()
                
        return sumador
    def cuentaTipo(self, tipo):
        contador = 0
        for helado in self.__lista:
            if helado.getGramos() == tipo:
                contador += 1
                
        return contador
    def sumador(self):
        sumador = 0
        for helado in self.__lista:
            sumador += helado.getPrecio()
        
        return sumador 