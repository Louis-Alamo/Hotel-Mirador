from customtkinter import *
from componentes_graficos.LtkButton import LtkButtonFill
from componentes_graficos.LtkEntry import LtkEntryLine
from componentes_graficos.LtkComboBox import LtkComboBoxLine

class FormularioHabitacion():

    def __init__(self, callback):
        self.callback = callback


        self.ventana = CTkToplevel()
        self.ventana.title("Habitación")

        self.ventana.resizable(False, False)
        self.ventana.grab_set()
        self.ventana.protocol("WM_DELETE_WINDOW", self.on_close)

        self.ventana.grid_columnconfigure(0, weight=1)
        self.ventana.grid_columnconfigure(1, weight=1)

        self.ventana.configure(fg_color="#FFFFFF")

        self.crear_formulario()
        

    def crear_formulario(self):

        CTkLabel(self.ventana, text="Habitación", text_color="#000000", font=("Poppins", 24, "bold"), fg_color="#FFFFFF").grid(row=0, column=0, padx=10, pady=10, columnspan=2)

        self.frame_datos_habitacion= CTkFrame(self.ventana)
        self.frame_datos_habitacion.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")

        self.etiqueta_titulo = CTkLabel(self.frame_datos_habitacion, text="Datos de habitación", font=("Poppins", 14, "bold"))
        self.etiqueta_titulo.grid(row=0, column=0, padx=10, pady=10, columnspan=2)

        self.etiqueta_clave = CTkLabel(self.frame_datos_habitacion, text="Número habitación: ", font=("Poppins", 12, "bold"))
        self.etiqueta_clave.grid(row=1, column=0, padx=10, pady=10, sticky="w")

        self.campo_clave = LtkEntryLine(self.frame_datos_habitacion, texto="Número habitación")
        self.campo_clave.grid(row=1, column=1, padx=10, pady=10, columnspan=2, sticky="ew")

        self.etiqueta_precio = CTkLabel(self.frame_datos_habitacion, text="Precio por noche: ", font=("Poppins", 12, "bold"))
        self.etiqueta_precio.grid(row=2, column=0, padx=10, pady=10, sticky="w")

        self.campo_precio = LtkEntryLine(self.frame_datos_habitacion, texto="Precio por noche")
        self.campo_precio.grid(row=2, column=1, padx=10, pady=10, columnspan=2, sticky="ew")

        self.etiqueta_horario = CTkLabel(self.frame_datos_habitacion, text="Datos habitación: ", font=("Poppins", 12, "bold"))
        self.etiqueta_horario.grid(row=3, column=0, padx=10, pady=10, sticky="w")

        self.tipo_de_habitacion = LtkComboBoxLine(self.frame_datos_habitacion, ["Sencilla", "Jacuzzi", "Suite"])
        self.tipo_de_habitacion.grid(row=4, column=0, padx=10, pady=10, sticky="ew")

        self.estado_habitacion = LtkComboBoxLine(self.frame_datos_habitacion, ["Disponible", "Ocupada", "Sucia"])
        self.estado_habitacion.grid(row=4, column=1, padx=10, pady=10, sticky="ew")

        self.frame_botones = CTkFrame(self.ventana, fg_color="#FFFFFF")
        self.frame_botones.grid(row=2, column=0, padx=10, pady=10, columnspan=2, sticky="e")


        self.boton_cancelar = LtkButtonFill(self.frame_botones, nombre="Cancelar", funcion=lambda: self.aceptar())
        self.boton_cancelar.grid(row=0, column=1, padx=10, pady=10, sticky="ew")

        self.boton_aceptar = LtkButtonFill(self.frame_botones, nombre="Aceptar", funcion=lambda: self.aceptar())
        self.boton_aceptar.grid(row=0, column=2, padx=10, pady=10, sticky="ew")
    
    def ejecutar_ventana(self):
        self.ventana.mainloop()

    def aceptar(self):
        self.ventana.destroy()
    
    def cancelar(self):
        self.ventana.destroy()

    def on_close(self):
        self.callback()
        self.ventana.destroy()

