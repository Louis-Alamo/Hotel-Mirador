from customtkinter import *
from componentes_graficos.LtkButton import LtkButtonFill
from componentes_graficos.LtkEntry import LtkEntryLine
from componentes_graficos.LtkComboBox import LtkComboBoxLine
class RegistrarServicio:

    def __init__(self):

        self.ventana = CTk()
        self.ventana.title("Registrar Servicio")

        self.ventana.resizable(False, False)
        self.ventana.grab_set()

        self.ventana.configure(fg_color="#FFFFFF")

        self.crear_formulario()

        self.ventana.mainloop()

    def crear_formulario(self):

        CTkLabel(self.ventana, text="Servicio", text_color="#000000", font=("Poppins", 24, "bold"), fg_color="#FFFFFF").grid(row=0, column=0, padx=10, pady=10, columnspan=2)

        self.frame_datos_servicio = CTkFrame(self.ventana)
        self.frame_datos_servicio.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")

        self.etiqueta_titulo = CTkLabel(self.frame_datos_servicio, text="\tDatos Servicio", font=("Poppins", 14, "bold"))
        self.etiqueta_titulo.grid(row=0, column=0, padx=10, pady=10, columnspan=2)

        self.etiqueta_ID = CTkLabel(self.frame_datos_servicio, text="ID del Servicio: ", font=("Poppins", 12, "bold"))
        self.etiqueta_ID.grid(row=2, column=0, padx=10, pady=10, sticky="w")

        self.campo_ID = LtkEntryLine(self.frame_datos_servicio, texto="ID del Servicio")
        self.campo_ID.grid(row=2, column=1, padx=10, pady=10, columnspan=2, sticky="ew")

        self.etiqeuta_nombre_servicio = CTkLabel(self.frame_datos_servicio, text="Nombre Servicio: ",  font=("Poppins", 12, "bold"))
        self.etiqeuta_nombre_servicio.grid(row=3, column=0, padx=10, pady=10, sticky="w")

        self.campo_nombre_servicio = LtkEntryLine(self.frame_datos_servicio, texto="Nombre Servicio")
        self.campo_nombre_servicio.grid(row=3, column=1, padx=10, pady=10, columnspan=2, sticky="ew")

        self.etiqueta_descripcion = CTkLabel(self.frame_datos_servicio, text="Descripción: ", font=("Poppins", 12, "bold"))
        self.etiqueta_descripcion.grid(row=4, column=0, padx=10, pady=10, sticky="w")

        self.campo_descripcion = LtkEntryLine(self.frame_datos_servicio, texto="Descripción")
        self.campo_descripcion.disable()
        self.campo_descripcion.grid(row=4, column=1, padx=10, pady=10, columnspan=2, sticky="ew")

        self.etiqueta_costo = CTkLabel(self.frame_datos_servicio, text="Costo del Servicio: ", font=("Poppins", 12, "bold"))
        self.etiqueta_costo.grid(row=5, column=0, padx=10, pady=10, sticky="w")

        self.campo_costo = LtkEntryLine(self.frame_datos_servicio, texto="Costo del Servicio")
        self.campo_costo.disable()
        self.campo_costo.grid(row=5, column=1, padx=10, pady=10, columnspan=2, sticky="ew")

        self.etiqueta_disponibilidad = CTkLabel(self.frame_datos_servicio, text="Disponibilidad del Servicio: ",
                                       font=("Poppins", 12, "bold"))
        self.etiqueta_disponibilidad.grid(row=6, column=0, padx=10, pady=10, sticky="w")

        self.cargo_disponibilidad = LtkComboBoxLine(self.frame_datos_servicio, ["Disponible", "Ocupada"])
        self.cargo_disponibilidad.grid(row=6, column=1, padx=10, pady=10, columnspan=2, sticky="ew")


        self.frame_botones = CTkFrame(self.ventana, fg_color="#FFFFFF")
        self.frame_botones.grid(row=2, column=0, padx=10, pady=10, columnspan=2, sticky="e")


        self.boton_cancelar = LtkButtonFill(self.frame_botones, nombre="Cancelar", funcion=lambda: self.aceptar())
        self.boton_cancelar.grid(row=0, column=1, padx=10, pady=10, sticky="ew")

        self.boton_aceptar = LtkButtonFill(self.frame_botones, nombre="Aceptar", funcion=lambda: self.aceptar())
        self.boton_aceptar.grid(row=0, column=2, padx=10, pady=10, sticky="ew")


    def aceptar(self):
        pass


RegistrarServicio()

