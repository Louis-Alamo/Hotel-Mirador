from tkinter import *
from customtkinter import CTkLabel
from front_end.componentes_graficos.individuales.LtkButton.LtkButtonFill import LtkButtonFill
from front_end.componentes_graficos.individuales.LtkEntry.LtkEntryLine import LtkEntryLine
from front_end.ventanas.FrameMenuPrincipal import FrameMenuPrincipal
from util import ProcesarImagenes, comprobar_credenciales

class Login(Frame):

    def __init__(self, master, width, height, **kwargs):
        super().__init__(master=master, width=width,bg="#FFFFFF", height=height, **kwargs)

        #Se agrego para que un pendejo no modifique el tamaño de ventana
        master.resizable(False, False)

        self.master = master
        image_path = '../../imagenes/Hotel.jpg'

        # Guardar la imagen como un atributo de la clase
        self.imagen = ProcesarImagenes.rescale_image(image_path=image_path, new_width=400, new_height=480)

        self.etiqueta_imagen = Label(self, image=self.imagen)
        self.etiqueta_imagen.place(x=0, y=0)

        self.etiqueta_bienvenida = CTkLabel(self, text="Welcome back! Please login to your account...", font=("Poppins", 12), fg_color="#FFFFFF", text_color="#387782")
        self.etiqueta_bienvenida.place(x=460, y=100)

        self.etiqueta_titulo = CTkLabel(self, text="Login", font=("Poppins", 20, "bold"), fg_color="#FFFFFF")
        self.etiqueta_titulo.place(x=460, y=40)


        self.etiqueta_entrada_empleado = CTkLabel(self, text="nombre empleado: ", font=("Poppins", 12), fg_color="#FFFFFF")
        self.etiqueta_entrada_empleado.place(x=460, y=150)

        self.entrada_nombre_empleado = LtkEntryLine(self)
        self.entrada_nombre_empleado.configure(width=280, height=30)
        self.entrada_nombre_empleado.place(x=460, y=180)


        self.etiqueta_clave = CTkLabel(self, text="clave de acceso: ", font=("Poppins", 12), fg_color="#FFFFFF")
        self.etiqueta_clave.place(x=460, y=230)
        self.entrada_clave = LtkEntryLine(self)
        self.entrada_clave.configure(width=280, height=30)
        self.entrada_clave.place(x=460, y=260)

        self.boton_iniciar_sesion = LtkButtonFill(self, nombre="Iniciar Sesión", funcion=lambda :self.comprobar_acceso())
        self.boton_iniciar_sesion.configure(width=280, height=40)
        self.boton_iniciar_sesion.place(x=460,y=340)

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

        ventana = Tk()
        ventana.geometry("1200x650")
        ventana.title("Sistema de Gestión de Hotel")
        ventana.resizable(False, False)
        ventana.config(bg="#FFFFFF")
        frame_principal = FrameMenuPrincipal(ventana)
        frame_principal.pack()
        self.master.destroy()
        ventana.mainloop()



ventana = Tk()
n = Login(ventana, 820,480)
n.grid(row=0, column=0)
ventana.mainloop()
