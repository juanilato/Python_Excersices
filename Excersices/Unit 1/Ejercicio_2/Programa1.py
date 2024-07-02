import csv 
from ViajeroFrecuente import ViajeroFrecuente
from Menu import Menu
from validador import validaViajero

if __name__=="__main__":
    """
    1- Leer de un archivo separado por comas 
    los datos para crear instancias de la clase 
    ViajeroFrecuente, y almacenarlas en una lista.
    """
    archivo = open('viajeros.csv')
    reader = csv.reader(archivo, delimiter=',')
    listaViajeros = []
    for fila in reader:
            viajero = ViajeroFrecuente(fila[0], int(fila[1]), fila[2],fila[3], int(fila[4]))
            listaViajeros.append(viajero)
    archivo.close()
    """
    2- El usuario ingresa por teclado un número de viajero frecuente, el sistema presente un menú con las siguientes opciones:

        a- Consultar Cantidad de Millas.

        b- Acumular Millas.

        c- Canjear Millas.
    """
    cantidad = int(input("Ingrese cantidad de opciones del menú: "))
    Menu1 = Menu(cantidad)
    Menu1.IngresaOpcion()
    
    num_viajero = int(input("Ingrese Número de viajero frecuente: "))
    if validaViajero(num_viajero, listaViajeros)!=-1:
        i = validaViajero(num_viajero, listaViajeros)
        Menu1.Muestra()
        opcion = int(input("Ingrese opcion: "))
        while opcion != (cantidad + 1): 
            if opcion == 1:
                #consulta cantidad de millas
                num = listaViajeros[i].cantidadTotalMillas()
                print("Sus millas son: ", num)
            elif opcion == 2:
                #acumula millas
                num = int(input("Ingrese cantidad de millas a acumular "))
                listaViajeros[i].acumularMillas(num)
            elif opcion == 3: 
                #canjear Millas
                num = int(input("Ingrese millas a canjear "))
                listaViajeros[i].canjearMillas(num)
            else: print("Ingreso opcion incorrecta")
            Menu1.Muestra()
            opcion = int(input("Ingrese opcion: "))
        
    print("Saliendo del sistema")
        


        
