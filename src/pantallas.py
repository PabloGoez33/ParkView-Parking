import tkinter as tk
from constantes import style
import sys
from modelo.funcionalidades import *

class Inicio(tk.Frame):

    def __init__(self, parent, controller):
        super().__init__(parent)
        self.configure(background = style.BACKGROUND)
        self.controller = controller

        self.init_widgets()

    def mover_menu_login(self):
        self.controller.show_frame(Menu_Login)
    
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
            **style.STYLE_TEXTO,
            command = self.mover_menu_login
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
            **style.STYLE_TEXTO,
            command = sys.exit
        ).pack(
            side = tk.TOP,
            fill = tk.X,
            padx = 20,
            pady = 25
        )


class Menu_Login(tk.Frame):

    def __init__(self, parent, controller):
        super().__init__(parent)
        self.configure(background = style.BACKGROUND)
        self.controller = controller

        self.init_widgets()

    def mover_registro(self):
        self.controller.show_frame(Registro)
    
    def mover_login(self):
        self.controller.show_frame(Login)
    
    def init_widgets(self):
        tk.Label(
            self,
            text = "LOGIN PARKVIEW",
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
            text = "REGISTRO",
            justify = tk.CENTER,
            **style.STYLE_TEXTO,
            command = self.mover_registro
        ).pack(
            side = tk.TOP,
            fill = tk.X,
            padx = 20,
            pady = 25
        )
        tk.Button(
            Frame_Opciones,
            text = "LOG-IN",
            justify = tk.CENTER,
            **style.STYLE_TEXTO,
            command = self.mover_login
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
            **style.STYLE_TEXTO,
            command = sys.exit
        ).pack(
            side = tk.TOP,
            fill = tk.X,
            padx = 20,
            pady = 25
        )


class Registro(tk.Frame):

    def __init__(self, parent, controller):
        super().__init__(parent)
        self.configure(background = style.BACKGROUND)
        self.controller = controller

        self.init_widgets()

    def mover_menu_login(self):
        self.controller.show_frame(Menu_Login)

    def limpiar_campos(self):
        if self.entry_nombre_completo and self.entry_cedula and self.entry_contraseña and self.entry_correo_electronico:
            self.entry_nombre_completo.delete(0, tk.END)
            self.entry_cedula.delete(0, tk.END)
            self.entry_contraseña.delete(0, tk.END)
            self.entry_correo_electronico.delete(0, tk.END)
    
    def init_widgets(self):
        tk.Label(
            self,
            text = "REGISTRO",
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
        tk.Label(
            Frame_Opciones,
            text = "Nombre completo",
            justify = tk.CENTER,
            **style.STYLE_CUERPO
        ).pack(
            side = tk.TOP,
            fill = tk.X,
            padx = 20,
            pady = 25
        )
        self.entry_nombre_completo = tk.Entry(Frame_Opciones)
        self.entry_nombre_completo.pack(
            side = tk.TOP,
            fill = tk.X,
            padx = 20
        )
        tk.Label(
            Frame_Opciones,
            text = "Cedula",
            justify = tk.CENTER,
            **style.STYLE_CUERPO
        ).pack(
            side = tk.TOP,
            fill = tk.X,
            padx = 20,
            pady = 25
        )
        self.entry_cedula = tk.Entry(Frame_Opciones)
        self.entry_cedula.pack(
            side = tk.TOP,
            fill = tk.X,
            padx = 20
        )
        tk.Label(
            Frame_Opciones,
            text = "Contraseña",
            justify = tk.CENTER,
            **style.STYLE_CUERPO
        ).pack(
            side = tk.TOP,
            fill = tk.X,
            padx = 20,
            pady = 25
        )
        self.entry_contraseña = tk.Entry(
            Frame_Opciones,
            show = "*"
        )
        self.entry_contraseña.pack(
            side = tk.TOP,
            fill = tk.X,
            padx = 20
        )
        tk.Label(
            Frame_Opciones,
            text = "Correo electronico",
            justify = tk.CENTER,
            **style.STYLE_CUERPO
        ).pack(
            side = tk.TOP,
            fill = tk.X,
            padx = 20,
            pady = 25
        )
        self.entry_correo_electronico = tk.Entry(Frame_Opciones)
        self.entry_correo_electronico.pack(
            side = tk.TOP,
            fill = tk.X,
            padx = 20
        )
        
        tk.Button(
            Frame_Opciones,
            text = "REGISTRAR",
            justify = tk.CENTER,
            **style.STYLE_TEXTO,
            command = lambda : (registro(self.entry_nombre_completo, self.entry_cedula, self.entry_contraseña, self.entry_correo_electronico),
                                self.limpiar_campos(),
                                self.mover_menu_login())
        ).pack(
            side = tk.TOP,
            fill = tk.X,
            padx = 20,
            pady = 25
        )


class Login(tk.Frame):

    def __init__(self, parent, controller):
        super().__init__(parent)
        self.configure(background = style.BACKGROUND)
        self.controller = controller

        self.init_widgets()

    def mover_menu_principal(self):
        self.controller.show_frame(Menu_Principal)

    def accion_boton(self):
        pass
        #if self.entry_correo_electronico == Reg
        #Pasar objetos entre frames porque registro devuelve un objeto como obtengo el objeto
    
    def init_widgets(self):
        tk.Label(
            self,
            text = "LOGIN",
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
        tk.Label(
            Frame_Opciones,
            text = "Correo electronico",
            justify = tk.CENTER,
            **style.STYLE_CUERPO
        ).pack(
            side = tk.TOP,
            fill = tk.X,
            padx = 20,
            pady = 25
        )
        self.entry_correo_electronico = tk.Entry(
            Frame_Opciones
        )
        self.entry_correo_electronico.pack(
            side = tk.TOP,
            fill = tk.X,
            padx = 20
        )
        tk.Label(
            Frame_Opciones,
            text = "Contraseña",
            justify = tk.CENTER,
            **style.STYLE_CUERPO
        ).pack(
            side = tk.TOP,
            fill = tk.X,
            padx = 20,
            pady = 25
        )
        self.entry_contraseña = tk.Entry(
            Frame_Opciones,
            show = "*"
        )
        self.entry_contraseña.pack(
            side = tk.TOP,
            fill = tk.X,
            padx = 20
        )
        tk.Button(
            Frame_Opciones,
            text = "INICIAR SESION",
            justify = tk.CENTER,
            **style.STYLE_TEXTO,
            command = self.mover_menu_principal
        ).pack(
            side = tk.TOP,
            fill = tk.X,
            padx = 20,
            pady = 25
        )

        """tk.Button(
            Frame_Opciones,
            text = "MENÚ",
            justify = tk.CENTER,
            **style.STYLE_TEXTO,
            command = self.mover_menu_login
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
            **style.STYLE_TEXTO,
            command = sys.exit
        ).pack(
            side = tk.TOP,
            fill = tk.X,
            padx = 20,
            pady = 25
        )"""

class Menu_Principal(tk.Frame):
    
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.configure(background = style.BACKGROUND)
        self.controller = controller