from Pila import Pila



def cargaRegresiva(pila, tamanio):
    while tamanio > 0:
        pila.apilar(tamanio)
        tamanio -= 1
        

if __name__=="__main__":
    tamanio = int(input("Ingrese tamaño de discos pa jugar: "))
    pila1=Pila(tamanio)
    pila2=Pila(tamanio)
    pila3=Pila(tamanio)
    
    cargaRegresiva(pila1, tamanio)
    
    
    print("Opcion 1. Mover Ficha torre 1")
    print("Opcion 2. Mover Ficha torre 2")
    print("Opcion 3. Mover Ficha torre 3")
    print("4. Mostrar resultado")
    op = int(input("Ingrese opcion"))
    while op != 0:
        if op == 1 and not pila1.vacia():
            moverA = int(input("Ingrese torre a mover ficha: "))
            if moverA == 2:
                if pila2.vacia():
                    ele1 = pila1.desapilar()
                    pila2.apilar(ele1)
                else:
                    ele1 = pila1.desapilar()
                    ele2 = pila2.desapilar()
                    if ele1 > ele2:
                        pila1.apilar(ele1)
                        pila2.apilar(ele2)        
                    else:
                        pila2.apilar(ele2)
                        pila2.apilar(ele1)
                    
                                        
            elif moverA == 3:
                if pila3.vacia():
                    ele1 = pila1.desapilar()
                    pila3.apilar(ele1)
                else:
                    ele1 = pila1.desapilar()
                    ele3 = pila3.desapilar()
                    if ele1 > ele3:
                        pila1.apilar(ele1)
                        pila3.apilar(ele3)        
                    else:
                        pila3.apilar(ele3)
                        pila3.apilar(ele1)
            else: 
                print("Opcion incorrecta")
        elif op == 2 and not pila2.vacia():
            moverA = int(input("Ingrese torre a mover ficha: "))
            if moverA == 1:
                if pila1.vacia():
                    ele2 = pila2.desapilar()
                    pila1.apilar(ele2)
                else:
                    ele2 = pila2.desapilar()
                    ele1 = pila1.desapilar()
                    if ele2 > ele1:
                        pila2.apilar(ele2)
                        pila1.apilar(ele1)        
                    else:
                        pila1.apilar(ele1)
                        pila1.apilar(ele2)
            elif moverA == 3:
                
                if pila3.vacia():
                    ele2 = pila2.desapilar()
                    pila3.apilar(ele2)
                else:
                    ele2 = pila2.desapilar()
                    ele3 = pila3.desapilar()
                    if ele2 > ele3:
                        pila2.apilar(ele2)
                        pila3.apilar(ele3)        
                    else:
                        pila3.apilar(ele3)
                        pila3.apilar(ele2)
            else: 
                print("Opcion incorrecta")

        elif op == 3 and not pila3.vacia():
            moverA = int(input("Ingrese torre a mover ficha: "))
            if moverA == 1:
                if pila1.vacia():
                    ele3 = pila3.desapilar()
                    pila1.apilar(ele3)
                else:
                    ele1 = pila1.desapilar()
                    ele3 = pila3.desapilar()
                    if ele3 > ele1:
                        pila1.apilar(ele1)
                        pila3.apilar(ele3)        
                    else:
                        pila1.apilar(ele1)
                        pila1.apilar(ele3)
            
            elif moverA == 2:
                if pila2.vacia():
                    ele3 = pila3.desapilar()
                    pila2.apilar(ele3)
                else:
                    ele2 = pila2.desapilar()
                    ele3 = pila3.desapilar()
                    if ele3 > ele2:
                        pila2.apilar(ele2)
                        pila3.apilar(ele3)        
                    else:
                        pila2.apilar(ele2)
                        pila2.apilar(ele3)
            else: 
                print("Opcion incorrecta")

        elif op == 4:
            print("Pila 1" )
            pila1.print()
            print("Pila 2 ")
            pila2.print()
            print("Pila 3 ")
            pila3.print()
        else:
            print("No ingreso opcion valida")
        
        print("Opcion 1. Mover Ficha torre 1")
        print("Opcion 2. Mover Ficha torre 2")
        print("Opcion 3. Mover Ficha torre 3")
        print("4. Mostrar resultado")
        op = int(input("Ingrese opcion"))
        