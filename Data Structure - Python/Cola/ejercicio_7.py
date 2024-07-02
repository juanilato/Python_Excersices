from clase_encadenada import ColaEncadenada
import random

from clase_recepcionista import Recepcionista

if __name__ =="__main__":
    

    cola = ColaEncadenada()
    
    
    frecuenciaClientes = int(input("Ingrese frecuencia clientes "))
    
    tiempoAtencion = int(input("Ingrese tiempo de atención "))
    
    tiempo_atencion_medico = int(input("Ingrese tiempo de atención del médico: "))
    
    
    tiempo_max = int(input("Ingrese tiempo máximo de atención "))
    
   
    
    
    reloj = 0
        
    recepcionista = Recepcionista(tiempoAtencion)
    
    
    
    colas_especialidad = [ColaEncadenada(),ColaEncadenada(), ColaEncadenada(),ColaEncadenada()]
    doctores = [Recepcionista(tiempo_atencion_medico), Recepcionista(tiempo_atencion_medico), Recepcionista(tiempo_atencion_medico), Recepcionista(tiempo_atencion_medico)]

    contador_noTurno = 0 #Contador gente sin turno
    
    while reloj < tiempo_max:
            numero_aleatorio = random.random()
            probabilidad_llegada = 1 / frecuenciaClientes #Calculo con frecuencia de clientes
            
            
            if numero_aleatorio <= probabilidad_llegada and reloj <= 60: #Si llega cliente y esta dentro de la primera hora, se puede sacar turno
                cola.insertar(reloj)
            elif reloj > 60:
                contador_noTurno += 1 #Si esta fuera de la primera hora se cuenta como persona que no pudo sacar turno 

                
                    
                
                
            if recepcionista.getTiempo() == 0 and not cola.vacio(): #Si el recepcionista esta libre y hay gente en cola se lo atiende
                dato = int(cola.suprimir()) 
                recepcionista.sumarDato(dato)
                recepcionista.contarCant()   #computamos el tiempo de atencion del mismo y que un cliente fue atendido por recepcionista
                recepcionista.setTiempo() #reseteamos el tiempo de atención de recepcionista
                
                pos = random.randint(0,3)  #Número random para especialidades
                if doctores[pos].getCant() < 10: #si no se atendieron 10 clientes en esa especialidad, se puede atender el cliente
                    doctores[pos].contarCant() #se suma cliente atendido en especialidad
                    colas_especialidad[pos].insertar(reloj) #se inserta en la cola de la especialidad

                    if doctores[pos].getTiempo() == 0 and not colas_especialidad[pos].vacio(): #Si doctor esta libre y cliente esta esperando se atiende
                            dato = int(colas_especialidad[pos].suprimir())
                            doctores[pos].sumarDato(dato)
                            doctores[pos].contarCant() #Se computa el tiempo de espera acumulador y contador por especialidad
                            doctores[pos].setTiempo #Se setea el tiempo de atención de doctor a 20
                
            
            
        
            reloj += 1 #actualiza reloj
            for doctor in doctores: #Por cada doctor si su tiempo de atencion es mayor a 0 se le actualiza el tiempo
                 if doctor.getTiempo() > 0:
                      doctor.descontarTiempo() 
                 
            if recepcionista.getTiempo() > 0:  #por recepcionista si su tiempo de atención es mayor a 0 se le actualiza el tiempo
                recepcionista.descontarTiempo()
            
            
            
    for i in range(0,4):
         print("Tiempo de espera promedio: Especialidad", i, " ", doctores[i].calculaTiempo()) #tiempo de espera promedio en cada especialidad
         
         
                                            
                                            
                                                    
                                                   
    
    print("Tiempo de espera promedio: ", recepcionista.calculaTiempo()) #tiempo de espera promedio en cola de turnos
    print("Cantidad de gente que no pudo sacar turno: ", contador_noTurno) #cantidad de personas que no pudieron obtener turnos

