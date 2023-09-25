def menu1() -> int:
    print("--------------------------------------")
    print("\tBIENVENIDO A PARKVIEW\t\t")
    print("--------------------------------------")
    print("1. Menú.")
    print("2. Salir.")
    print("--------------------------------------")
    opcion = int(input("Ingrese la opcion: "))
    print("--------------------------------------")
    return opcion

def menu2() -> int:
    print("--------------------------------------")
    print("\t     MENU PARKVIEW\t\t")
    print("--------------------------------------")
    print("1. Registro.")
    print("2. Log in.")
    print("3. Salir.")
    print("--------------------------------------")
    opcion = int(input("Ingrese la opcion: "))
    print("--------------------------------------")
    return opcion

def menu3() -> int:
    print("--------------------------------------")
    print("\t     MENU PARKVIEW\t\t")
    print("--------------------------------------")
    print("1. Mirar celdas disponibles.")
    print("2. Reservar celda.")
    print("3. Ingresar placa.")
    print("4. Cancelar reserva.")
    print("5. Calcular pago.")
    print("6. Generar recibo.")
    print("7. Salir.")
    print("--------------------------------------")
    opcion = int(input("Ingrese la opcion: "))
    print("--------------------------------------")
    return opcion

def registro():
    nombre_completo = input("Ingrese su nombre completo: ")
    cedula = int(input("Ingrese su cedula: "))
    contraseña = input("Ingrese su clave nueva: ")
    correo_electronico = input("Ingrese su correo electronico: ")
    regi = Registro(nombre_completo, cedula, contraseña, correo_electronico)
    print("Perfil Registrado")
    return regi

class Registro:

    def __init__(self, nombre: str, cedula: int, contraseña: str, correo: str):
        self.nombre_completo: str = nombre
        self.cedula: int = cedula
        self.contraseña: str = contraseña
        self.correo_electronico: str = correo

    def login(self):
        print(self.cedula)
        print(self.contraseña)
        print("--------------------------------------")
        print("\t\tLOGIN")
        print("--------------------------------------")
        cedu = int(input("CEDULA: "))
        contra = input("CONTRASEÑA: ")
        print("--------------------------------------")
        if cedu == self.cedula and contra == self.contraseña:
            print("Bienvenido al sistema de PARKVIEW")
            opcion = menu3()
        else:
            print("Contraseña o usuario incorrecto")
            print("Olvido su contraseña, ¿Desea restaurarla?")
            print("1. Si.")
            print("2. No.")
            opcion = int(input("Ingrese la opcion: "))
            if opcion == 1:
                self.olvido_contraseña()
    
    def olvido_contraseña(self):
        COD = 33
        print("---------------------------------------")
        print(" SISTEMA DE RECUPERACION DE CONTRASEÑA")
        print("---------------------------------------")
        correo = input("Ingrese su correo electronico: ")
        if correo == self.correo_electronico:
            print("Correo enviado")
            print(f"El codigo que llego al correo es {COD}")
            codigo = int(input("Ingrese el codigo que fue enviado al correo: "))
            if codigo == COD:
                cedu = int(input("Ingrese su cedula: "))
                if cedu == self.cedula:
                    nue_clav = input("Ingrese su nueva clave: ")
                    self.contraseña = nue_clav
                    print("Contraseña cambiada con exito.")
                    self.login()