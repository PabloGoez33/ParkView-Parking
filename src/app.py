from modelo.funcionalidades import *


def main():

    regi = 0
    
    opcion = menu1()

    if opcion == 1:
        opcion2 = menu2()

        if opcion2 == 1:
            
            regi = registro()
            print(regi.nombre_completo)
            regi.login()
        elif opcion2 == 2:
            if regi == 0:
                print("Debe registrarse primero.")
                regi = registro()
                regi.login()
            

main()