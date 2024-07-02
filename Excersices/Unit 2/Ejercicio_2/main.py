from ManejaSabores import ManejaSabores
from ManejaHelados import ManejaHelados
from clase_menu import Menu 


if __name__ == "__main__":
    
    manejaSabores = ManejaSabores()
    manejaSabores.cargar()
    manejaHelados = ManejaHelados()
    
    opciones = ["Registrar un helado vendido","5 Sabores más pedidos","Ingresar un número de sabor y estimar el total de gramos vendidos.","Ingresar por teclado un tipo de helado y mostrar los sabores vendidos en ese tamaño", "Determinar el importe total recaudado por la Heladería"]
    menu = Menu(5)
    menu.IngresaOpcion(opciones)
    
    
    
    menu.Muestra()
    op = int(input("Ingrese opcion: "))
    while op != (menu.getCantidad() + 1):
        if op == 1:
            cantidad = 0
            sabores = []
            manejaSabores.muestra()
            idSabor = int(input("Ingrese sabor de helado, 0 para salir "))
            manejaSabores.contarSabor(idSabor)
            while idSabor != 0 and (cantidad < 3):
                sabor = manejaSabores.busca(idSabor)
                sabores.append(sabor)
                cantidad += 1
                
                
                
                
                idSabor = int(input("Ingrese sabor de helado, 0 para salir "))
                manejaSabores.contarSabor(idSabor)
            
            gramos = int(input("Ingrese cantidad de gramos "))
            precio = int(input("Ingrese precio "))
            
            manejaHelados.addHelado(gramos, precio, sabores)
            
            manejaHelados.muestraHelados()
            
        elif op == 2:
            manejaSabores.ordena()
            manejaSabores.muestraContador()
        elif op == 3:
            manejaSabores.muestra()
            codigo = int(input("Ingrese sabor de helado a buscar: "))
            print(f"Cantidad de gramos del helado solicitado son: {manejaHelados.cuentaGramos(codigo)}")
        elif op == 4:
            tipo = int (input("Ingrese tipo de helado: "))
            print(f"Cantidad de helados de {tipo} gramos, son: {manejaHelados.cuentaTipo(tipo)}")
        elif op == 5:
            print(f"Total vendido: {manejaHelados.sumador()}")
        menu.Muestra()
        op = int(input("Ingrese opcion: "))