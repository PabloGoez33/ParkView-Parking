#from modelo.funcionalidades import *
import tkinter as tk
from constantes import style
from pantallas import *

class Manager(tk.Tk):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("PARKVIEW - PARKING")
        container = tk.Frame(self)
        container.pack(
            side = tk.TOP,
            fill = tk.BOTH,
            expand = True
        )
        container.configure(background = style.BACKGROUND)
        container.grid_columnconfigure(0, weight = 1)
        container.grid_rowconfigure(0, weight = 1)

        self.frames = {}
        for F in (Inicio, Pantalla):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row = 0, column = 0, sticky = tk.NSEW)

        self.show_frame(Inicio)

    def show_frame(self, container):
        frame = self.frames[container]
        frame.tkraise()

"""
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
            

main()"""