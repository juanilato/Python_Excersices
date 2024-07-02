from clase_email import Email

if __name__=="__main__":
    """
    1- Ingresar el nombre de una persona y su dirección de e-mail (instancia de la clase Email) 
    y luego imprima el siguiente mensaje:
        Estimado <nombre> te enviaremos tus mensajes a la dirección <dirección de correo>.
    """
    nombre = input("Ingrese su nombre ")
    correo = input("Ingrese su correo ")
    persona = Email(None, None, None, None)
    persona.crearCuenta(correo)
    print("Estimado "+ nombre + " te enviaremos tus mensajes a la dirección " + persona.retornaEmail())
    """
    2- Para la instancia creada en el ítem anterior, modificar la contraseña, 
    teniendo en cuenta que se debe ingresar la contraseña actual, y ésta debe
    ser igual a la registrada en la instancia. Luego se debe ingresar la nueva
    contraseña y realizar la modificación correspondiente.
    """
    
    antigua = str(input("Ingrese contraseña actual "))
    nueva = str(input("Ingrese contraseña nueva "))
    
    if persona.cambioContraseña(antigua, nueva) == -1:
        print("Solicitud no ha sido realizada ")
    else: 
        print("Solicitud realizada con exito ")
    """
    3- Crear un objeto de clase Email, a partir de una dirección de correo, como por ejemplo: 
        informatica.fcefn@gmail.com, wicc2023@unsj-cuim.edu, juanLiendro1957@yahoo.com, etc.
    """
    objeto1 = Email(None, None, None, None)
    correo ="informatica.fcefn@gmail.com"
    objeto1.crearCuenta(correo)
    objeto2 = Email(None, None, None, None)
    correo = "wicc2023@unsj-cuim.edu"
    objeto2.crearCuenta(correo)
    objeto3 = Email(None, None, None, None)
    correo = "juanLiendro1957@yahoo.com"
    objeto3.crearCuenta(correo)
    
    