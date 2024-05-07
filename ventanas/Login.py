import os
from tkinter import *
from customtkinter import *
from componentes_graficos.LtkButton import LtkButtonFill
from componentes_graficos.LtkEntry import LtkEntryLine
from ventanas.FrameMenuPrincipal import FrameMenuPrincipal
from util import ProcesarImagenes, comprobar_credenciales

class Login(Frame):

    def __init__(self):

        self.ventana = CTk()
        self.ventana.geometry("820x480")
        self.ventana.configure(fg_color="#FFFFFF")
        self.ventana.resizable(False, False)

        self.ruta_ventana = os.path.dirname(os.path.abspath(__file__))


        image_path = '../imagenes/Hotel.jpg'

        # Guardar la imagen como un atributo de la clase
        ruta_imagen = os.path.join(self.ruta_ventana, image_path)
        self.imagen = ProcesarImagenes.rescale_image(image_path=ruta_imagen, new_width=400, new_height=480)

        self.etiqueta_imagen = Label(self.ventana, image=self.imagen)
        self.etiqueta_imagen.place(x=0, y=0)

        self.etiqueta_bienvenida = CTkLabel(self.ventana, text="Welcome back! Please login to your account...", font=("Poppins", 12), fg_color="#FFFFFF", text_color="#387782")
        self.etiqueta_bienvenida.place(x=460, y=100)

        self.etiqueta_titulo = CTkLabel(self.ventana, text="Login", font=("Poppins", 20, "bold"), fg_color="#FFFFFF")
        self.etiqueta_titulo.place(x=460, y=40)


        self.etiqueta_entrada_empleado = CTkLabel(self.ventana, text="nombre empleado: ", font=("Poppins", 12), fg_color="#FFFFFF")
        self.etiqueta_entrada_empleado.place(x=460, y=150)

        self.entrada_nombre_empleado = LtkEntryLine(self.ventana)
        self.entrada_nombre_empleado.configure(width=280, height=30)
        self.entrada_nombre_empleado.place(x=460, y=180)


        self.etiqueta_clave = CTkLabel(self.ventana, text="clave de acceso: ", font=("Poppins", 12), fg_color="#FFFFFF")
        self.etiqueta_clave.place(x=460, y=230)
        self.entrada_clave = LtkEntryLine(self.ventana)
        self.entrada_clave.configure(width=280, height=30)
        self.entrada_clave.place(x=460, y=260)

        self.boton_iniciar_sesion = LtkButtonFill(self.ventana, nombre="Iniciar Sesión", funcion=lambda :self.comprobar_acceso())
        self.boton_iniciar_sesion.configure(width=280, height=40)
        self.boton_iniciar_sesion.place(x=460,y=340)


        self.ventana.mainloop()

    def comprobar_acceso(self):
        """
        Comprueba si el nombre de usuario y la contraseña ingresados son correctos.
        """
        nombre_empleado = self.entrada_nombre_empleado.get_text()
        clave = self.entrada_clave.get_text()

        if comprobar_credenciales.comprobar_acceso(nombre_empleado, clave):
            self.crear_ventana_principal()
        else:
            print("Acceso denegado")


    def crear_ventana_principal(self):
        """
        Crea la ventana principal del sistema.
        """







