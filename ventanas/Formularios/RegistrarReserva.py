from customtkinter import *
from componentes_graficos.LtkButton import LtkButtonFill
from componentes_graficos.LtkEntry import LtkEntryLine
from componentes_graficos.LtkComboBox import LtkComboBoxLine
from tkinter import ttk
class RegistrarReserva:

    def __init__(self):

        self.lista_servicios = [["Carlos", "pendejo"]]

        self.ventana = CTk()
        self.ventana.title("Registrar reserva")

        #self.ventana.resizable(False, False)
        self.ventana.grab_set()
        self.ventana.columnconfigure(0, weight=1)
        self.ventana.columnconfigure(1, weight=1)

        self.ventana.configure(fg_color="#FFFFFF")

        self.crear_formulario()

        self.ventana.mainloop()

    def crear_formulario(self):

        CTkLabel(self.ventana, text="Empleado", text_color="#000000", font=("Poppins", 24, "bold"), fg_color="#FFFFFF").grid(row=0, column=0, padx=10, pady=10, columnspan=2)

        self.frame_datos_personales = CTkFrame(self.ventana)
        self.frame_datos_personales.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")


        self.frame_datos_personales.columnconfigure(0, weight=1)
        self.frame_datos_personales.columnconfigure(1, weight=1)
        self.frame_datos_personales.columnconfigure(2, weight=1)


        self.etiqueta_titulo = CTkLabel(self.frame_datos_personales, text="Datos de reserva", font=("Poppins", 14, "bold"))
        self.etiqueta_titulo.grid(row=0, column=0, padx=10, pady=10, columnspan=2)

        self.etiqueta_clave_empleado = CTkLabel(self.frame_datos_personales, text="Clave empleado: ",  font=("Poppins", 12, "bold"))
        self.etiqueta_clave_empleado.grid(row=1, column=0, padx=10, pady=10, sticky="ew")

        self.clave_empleado_entry = LtkEntryLine(self.frame_datos_personales, texto="")
        self.clave_empleado_entry.grid(row=1, column=1, padx=10, pady=10, sticky="ew")

        self.boton_buscar_empleado = LtkButtonFill(self.frame_datos_personales, nombre="Buscar", funcion=lambda: self.aceptar())
        self.boton_buscar_empleado.grid(row=1, column=2, padx=10, pady=10, sticky="ew")


        self.etiqeuta_habitacion = CTkLabel(self.frame_datos_personales, text="Habitación: ",  font=("Poppins", 12, "bold"))
        self.etiqeuta_habitacion.grid(row=2, column=0, padx=10, pady=10, sticky="ew")

        self.habitacion_entry = LtkEntryLine(self.frame_datos_personales, texto="")
        self.habitacion_entry.grid(row=2, column=1, padx=10, pady=10, sticky="ew")

        self.boton_buscar_habitacion = LtkButtonFill(self.frame_datos_personales, nombre="Buscar", funcion=lambda: self.aceptar())
        self.boton_buscar_habitacion.grid(row=2, column=2, padx=10, pady=10, sticky="ew")


        self.boton_agregar_servicios = LtkButtonFill(self.frame_datos_personales, nombre="Agregar servicios adicionales", funcion=lambda: self.agregar_servicios_adicionales())
        self.boton_agregar_servicios.grid(row=3, column=0, padx=10, pady=10, columnspan=3, sticky="ew")

        self.etiqueta_fecha_inicio = CTkLabel(self.frame_datos_personales, text="Fechas de reservas",  font=("Poppins", 12, "bold"))
        self.etiqueta_fecha_inicio.grid(row=4, column=0, padx=10, pady=10, sticky="ew")

        self.fecha_inicio = LtkEntryLine(self.frame_datos_personales, texto="Formato: dd/mm/aaaa")
        self.fecha_inicio.grid(row=5, column=0, padx=10, pady=10, sticky="ew")

        self.fecha_fin = LtkEntryLine(self.frame_datos_personales, texto="Formato: dd/mm/aaaa")
        self.fecha_fin.grid(row=5, column=2, padx=10, pady=10, sticky="ew")




        self.frame_botones = CTkFrame(self.ventana, fg_color="#FFFFFF")
        self.frame_botones.grid(row=2, column=0, padx=10, pady=10, columnspan=2, sticky="e")


        self.boton_cancelar = LtkButtonFill(self.frame_botones, nombre="Cancelar", funcion=lambda: self.aceptar())
        self.boton_cancelar.grid(row=0, column=1, padx=10, pady=10, sticky="ew")

        self.boton_aceptar = LtkButtonFill(self.frame_botones, nombre="Aceptar", funcion=lambda: self.aceptar())
        self.boton_aceptar.grid(row=0, column=2, padx=10, pady=10, sticky="ew")


    def aceptar(self):
        pass


    def agregar_servicios_adicionales(self):

        ventana_servicios  = CTkToplevel()
        ventana_servicios.title("Servicios adicionales")
        ventana_servicios.configure(fg_color="#FFFFFF")
        ventana_servicios.grab_set()
        ventana_servicios.columnconfigure(0, weight=1)

        self.frame_botones = CTkFrame(ventana_servicios, fg_color="#FFFFFF")
        self.frame_botones.pack()

        self.entr_clave_servicio = LtkEntryLine(self.frame_botones, texto="Clave servicio")
        self.entr_clave_servicio.pack(side="left", padx=10, pady=10)

        self.boton_buscar_servicio = LtkButtonFill(self.frame_botones, nombre="Buscar", funcion=lambda: self.buscar_servicio())
        self.boton_buscar_servicio.pack(side="left", padx=10, pady=10)

        self.tabla = ttk.Treeview(ventana_servicios)
        self.tabla["columns"] = ["Nombre", "Precio"]
        self.tabla.heading("#0", text="Nombre")
        self.tabla.heading("Nombre", text="Nombre")
        self.tabla.heading("Precio", text="Precio")

        self.tabla.column("#0", width=0, stretch=False)
        self.tabla.column("Nombre", stretch=True)
        self.tabla.column("Precio", stretch=True)

        self.tabla.pack(expand=True, fill="both")

        self.eliminar_servicio = LtkButtonFill(self.frame_botones, nombre="Eliminar servicio", funcion=lambda: self.eliminar_servicio())
        self.eliminar_servicio.pack(side="left", padx=10, pady=10)

        self.actualizar_tabla()
        ventana_servicios.mainloop()

    def actualizar_tabla(self):

        for servicio in self.lista_servicios:
            self.tabla.insert("", "end", values=(servicio[0], servicio[1]))

    def buscar_empleado(self):
        pass

    def buscar_servicio(self):
        pass

    def buscar_habitacion(self):
        pass


    def eliminar_servicio(self):
        pass


RegistrarReserva()
