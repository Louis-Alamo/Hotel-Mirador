from customtkinter import  CTkFrame
from util.ProcesarImagenes import rescale_image
from tkinter import Label
import time
import os

class LtkFecha(CTkFrame):

    def __init__(self, master, **kwargs):

        super().__init__(master,**kwargs)

        self.configure(fg_color="#FFFFFF")

        dir_path = os.path.dirname(os.path.realpath(__file__))
        path = os.path.join(dir_path, '../../../imagenes/iconos/calendario.png')


        self.imagen = rescale_image(path, 30, 30)  # Reemplaza con la ruta a tu imagen
        self.etiqueta_fecha = Label(self, bg="#FFFFFF", image=self.imagen)
        self.etiqueta_fecha.pack(padx=10, side="left")

        self.etiqueta_fecha_texto = Label(self, text="", font=("Poppins", 12, "bold"), fg="#000000", bg="#FFFFFF", )
        self.etiqueta_fecha_texto.pack(padx=10, side="right")

        # Iniciar la actualización de la fecha
        self.actualizar_fecha()

    def actualizar_fecha(self):
        # Obtener la fecha actual
        fecha_actual = time.strftime("%d/%m/%Y")

        # Actualizar la etiqueta de la fecha
        self.etiqueta_fecha_texto.config(text=fecha_actual)

        # Llamar a esta función de nuevo después de 1 día
        self.after(86400000, self.actualizar_fecha)  # 86400000 milisegundos equivalen a 1 día

