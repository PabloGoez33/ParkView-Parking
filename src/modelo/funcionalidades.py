def registro(nombre_completo, cedula, contraseña, correo_electronico):
    regi = Usuario.Registro(nombre_completo, cedula, contraseña, correo_electronico)
    f = open("registros.txt", "a")
    f.write(f"\n Resgistro: \n Nombre Completo= {nombre_completo} \n Cedula= {cedula} \n Contraseña= {contraseña} \n Correo= {correo_electronico} \n")
    f.close
    return regi

def iniciar_sesion(cedula, contraseña):
    iniciar = Usuario.Login(cedula, contraseña)
    iniciar.validar_contraseña(cedula, contraseña)
    return iniciar

def registrar_vehiculo(tipo, placa):
    vehiculo = Usuario.Registrar_Vehiculo(tipo, placa)
    print("vehiculo registrado correctamente")
    vehi = tipo.title()
    if vehi == "Carro":
        print("La tarifa de parqueo para los carros es de 15.000 por hora")
    else:
        print("La tarifa de parqueo para las motos es de 9.000 por hora")
    return vehiculo


def cambio_contraseña(cedula, contraseña):
    cambio = Usuario.Cambiar_Contraseña(cedula, contraseña)
    print("La contraseña se cambió correctamente")

class Usuario:
    class Registro:
        def __init__(self, nombre: str, cedula: int, contraseña: str, correo: str):
            self.nombre_completo: str = nombre
            self.cedula: int = cedula
            self.contraseña: str = contraseña
            self.correo_electronico: str = correo
            print("Perfil Registrado")


    class Login:
        def __init__(self, cedula: int, contraseña: str):
            self.cedula: int = cedula
            self.contraseña: str = contraseña
        
        def validar_contraseña(self, cedula: int, contraseña: str):
            f = open("registros.txt", "r")
            f.close
            print(f)
            print("Usuario logueado correctamente")
            print("Bienvenido")

    
    class Cambiar_Contraseña:
        def __init__(self, cedula: int, contraseña: str):
            self.cedula: int = cedula
            self.contraseña: str = contraseña

    class Registrar_Vehiculo:
        def __init__(self, tipo_vehiculo:str, placa: str):
            self.tipo_vehiculo: str = tipo_vehiculo
            self.placa: str = placa
    
    class Seleccionar_Celda:
        def __init__(self):
            pass
            
    class Reservar_Celda:
        def __init__(self):
            pass
    
    class Cancelar_Reserva:
        def __init__(self, cedula: int):
            self.cedula: int = cedula

    class Descuento:
        def __init__(self, cedula: int):
            self.cedula: int = cedula

    class Calcular_Pago:
        def __init__(self):
            pass

    class Generar_Recibo:
        def __init__(self):
            pass