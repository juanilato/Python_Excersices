class Menu ():
    def __init__ (self, cantidad):
        self.__cantidad = cantidad
        self.__i = 0
        self.__lista = []

    def IngresaOpcion(self):
        while self.__cantidad > self.__i:
            texto = input("Ingrese opcion ")
            self.__lista.append(texto)
            self.__i = self.__i + 1
        
        print("Ya ingreso las maximas opciones para el menu")
    def Muestra (self):
        i = 1
        for opcion in self.__lista:
            print(f"{i} {opcion}")
            i = i +1
        print (f"{i} Salir ")




