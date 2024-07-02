from ViajeroFrecuente import ViajeroFrecuente
import csv

if __name__ == "__main__":
    
    listaViajeros = []
    archivo = open("viajeros.csv")
    reader = csv.reader(archivo, delimiter = ",")
    for fila in reader: 
        viajero = ViajeroFrecuente(int(fila[0]), int(fila[1]), fila[2] , fila[3] , int(fila[4]))
        listaViajeros.append(viajero)
    archivo.close()
    
    """
    1-Comparar las cantidad de millas acumuladas de un viajero frecuente 
    con un valor entero a través de 
    la sobrecarga del operador igual (== o __eq__). 
    Por ejemplo, sea v una instancia de la clase ViajeroFrecuente, 
    debe ser posible realizar tanto v ==  100 como 100 == v.
    """
    if listaViajeros[1] == 200:
        print("Es igual por izquierda \n")
    if 200 == listaViajeros[1]:
        print("Es igual por derecha \n")
    """
    2-Acumular millas se pueda resolver de la siguiente forma: 
    sea v una instancia de la clase ViajeroFrecuente, 
    debe ser posible realizar v =  100 + v.
    """
    
    listaViajeros[1] = listaViajeros[1] + 100
    listaViajeros[1].MostrarDatos()
    listaViajeros[1] = 100 + listaViajeros[1]
    listaViajeros[1].MostrarDatos()
    
    """
    3-Canjear millas se pueda resolver de la siguiente forma: 
    sea v una instancia de la clase ViajeroFrecuente,
    debe ser posible realizar v =  100 - v.
    
    """
    listaViajeros[1] = listaViajeros[1] - 100
    listaViajeros[1].MostrarDatos()
    listaViajeros[1] = 100 - listaViajeros[1] 
    listaViajeros[1].MostrarDatos()
    