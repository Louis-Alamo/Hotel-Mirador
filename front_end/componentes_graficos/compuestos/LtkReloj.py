from customtkinter import  CTkFrame
from util.ProcesarImagenes import rescale_image
from tkinter import Label
import time

class LtkReloj(CTkFrame):

    def __init__(self, master, **kwargs):

        super().__init__(master,**kwargs)

        self.configure(fg_color="#FFFFFF")

        self.imagen = rescale_image("../../../imagenes/iconos/reloj.png", 50, 50)
        self.etiqueta_reloj = Label(self,bg="#FFFFFF", image=self.imagen )
        self.etiqueta_reloj.pack(padx=10, side="left")

        self.etiqueta_hora = Label(self, text="", font=("Poppins", 14, "bold"), fg="#000000", bg="#FFFFFF", )
        self.etiqueta_hora.pack(padx=10, side="right")



    def actualizar_hora(self):
        # Obtener la hora actual
        hora_actual = time.strftime("%H:%M:%S")

        # Actualizar la etiqueta de la hora
        self.etiqueta_hora.config(text=hora_actual)

        # Llamar a esta función de nuevo después de 1 segundo
        self.after(1000, self.actualizar_hora)


