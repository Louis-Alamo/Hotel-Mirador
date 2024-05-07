from customtkinter import  CTkFrame
from util.ProcesarImagenes import rescale_image
from tkinter import Label
import time
import os

class LtkReloj(CTkFrame):

    def __init__(self, master, **kwargs):

        super().__init__(master,**kwargs)

        self.configure(fg_color="#FFFFFF")

        dir_path = os.path.dirname(os.path.realpath(__file__))
        path = os.path.join(dir_path, '..\\imagenes\\iconos\\reloj.png')

        self.imagen = rescale_image(path, 30, 30)
        self.etiqueta_reloj = Label(self,bg="#FFFFFF", image=self.imagen )
        self.etiqueta_reloj.pack(padx=10, side="left")

        self.etiqueta_hora = Label(self, text="", font=("Poppins", 12, "bold"), fg="#000000", bg="#FFFFFF", )
        self.etiqueta_hora.pack(padx=10, side="right")

        self.actualizar_hora()

    def actualizar_hora(self):
        # Obtener la hora actual
        hora_actual = time.strftime("%H:%M:%S")

        # Actualizar la etiqueta de la hora
        self.etiqueta_hora.config(text=hora_actual)

        # Llamar a esta función de nuevo después de 1 segundo
        self.after(1000, self.actualizar_hora)


