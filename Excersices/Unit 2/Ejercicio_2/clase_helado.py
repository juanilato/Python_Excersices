


class Helado:
    def __init__(self, gramos, precio, sabor = None):
        self.__gramos = gramos
        self.__precio = precio
        self.__sabor = []
        if sabor != None:
            self.addSabor(sabor, 1)
            
    
    def addSabor(self, sabor, cantidad):
        for i in range(cantidad):
            self.__sabor.append(sabor[i])
    
    def buscaSabor(self, cod):
        band = False
        i = 0
        while i < len(self.__sabor) and band == False:                    
            if self.__sabor[i].getID() == cod:
                band = True
            else:
                i += 1
        if i < len(self.__sabor):
            saborId = i
        else:
            saborId = -1
        return saborId
    
    def getGramos(self):
        return int(self.__gramos)
    
    def getLen(self):
        return int(len(self.__sabor))
    
    def getPrecio(self):
        return float(self.__precio)
    
    def __str__(self):
        cadena = "Gramos: " + str(self.__gramos) + " "
        cadena += "Precio: " + str(self.__precio) + ", "
        for sabor in self.__sabor:
            cadena += str(sabor)
        
        return cadena
    
            