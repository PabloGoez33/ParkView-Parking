import tkinter as tk
from constantes import style

class Inicio(tk.Frame):

    def __init__(self, parent, controller):
        super().__init__(parent)
        self.configure(background = style.BACKGROUND)
        self.controller = controller
        self.menus = tk.StringVar(self, value = "Menu_1")

        self.init_widgets()
    
    def init_widgets(self):
        tk.Label(
            self,
            text = "BIENVENIDOS A PARKVIEW",
            justify = tk.CENTER,
            **style.STYLE_TITULO
        ).pack(
            side = tk.TOP,
            fill = tk.BOTH,
            expand = True,
            padx = 20,
            pady = 25
        )
        Frame_Opciones = tk.Frame(self)
        Frame_Opciones.configure(background = style.BACKGROUND)
        Frame_Opciones.pack(
            side = tk.TOP,
            fill = tk.BOTH,
            expand = True,
            padx = 20,
            pady = 25
        )
        tk.Button(
            Frame_Opciones,
            text = "MENÚ",
            justify = tk.CENTER,
            **style.STYLE_TEXTO
        ).pack(
            side = tk.TOP,
            fill = tk.X,
            padx = 20,
            pady = 25
        )
        tk.Button(
            Frame_Opciones,
            text = "SALIR",
            justify = tk.CENTER,
            **style.STYLE_TEXTO
        ).pack(
            side = tk.TOP,
            fill = tk.X,
            padx = 20,
            pady = 25
        )




class Pantalla(tk.Frame):

    def __init__(self, parent, controller):
        super().__init__(parent)
        self.configure(background = style.BACKGROUND)
        self.controller = controller