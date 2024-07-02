from clase_encadenada import ColaEncadenada
import random



if __name__ =="__main__":
    
    acum = 0
    cantidad = 0
    
    cola = ColaEncadenada()
    
    frecuenciaClientes = int(input("Ingrese frecuencia clientes "))
    
    tiempoAtencion = int(input("Ingrese tiempo de atención ")) 
    cajero = 0
    
    tiempo_max = int(input("Ingrese tiempo máximo de atención "))
    
    
    
    reloj = 0
        
    while reloj < tiempo_max:
            numero_aleatorio = random.random()
            probabilidad_llegada = 1 / frecuenciaClientes
            
            
            if numero_aleatorio <= probabilidad_llegada:
                
                
                cola.insertar(reloj)
                
            if cajero == 0 and not cola.vacio():
                dato = int(cola.suprimir())
                acum += dato
                cantidad += 1
                cajero = tiempoAtencion
                
            
        
            reloj += 1
            
            if cajero > 0: 
                cajero -= 1
            
            
    tiempoPromedioDeEspera = acum / cantidad
        
    print("Tiempo de espera promedio: ", tiempoPromedioDeEspera)
        

    
