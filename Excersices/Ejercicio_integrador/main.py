
from manejador_alumnos import ManejadorAlumnos
from manejador_materias import ManejadorMaterias
from clase_menu import Menu




if __name__ == "__main__":
    
    manejadorM = ManejadorMaterias()
    manejadorM.carga()
    
    manejadorA = ManejadorAlumnos()
    manejadorA.carga()
    
    cantidad = 3
    menu = Menu(cantidad)
    opciones = ["Mostrar promedio con y sin aplazos", "Informa promocionales", "Obtener listado ordenado"]
    menu.IngresaOpcion(opciones)
    
    menu.Muestra()
    op = int(input("Ingrese opcion "))
    
    while op != (cantidad + 1):
        if op == 1:
            dni = int(input("Ingrese dni de alumno para ver promedio "))
            manejadorM.calculoProm(dni)
        elif op == 2:
            materia = input("Ingrese materia a buscar ")
            
            lista = manejadorM.devolverDatos(materia)
            for obj in lista:
                
                alumno = manejadorA.buscaDatos(obj.getDni())
                print("DNI           Apellido y Nombre            Fecha         Nota             Año que cursa")
                print(f"{alumno.getDni()},    {alumno.getNombre()}, {alumno.getApellido()}              {obj.getFecha()}     {obj.getNota()}              {alumno.getAnioCursa()}")

        elif op == 3:
            print("Listado alumnos ordenado:    ")
            manejadorA.ordenar()
            manejadorA.muestra()
        else:
            print("Ingreso opcion incorrecta")
        menu.Muestra()
        op = int(input("Ingrese opcion "))