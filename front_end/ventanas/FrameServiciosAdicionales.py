from tkinter import *
from SQL.ConsultarDatosSQL import ConsultarDatosSQL
from SQL.RegistrarDatos import RegistrarDatos
from SQL.EliminarDatos import EliminarDatos
from SQL.ActualizarDatos import ActualizarDatos
from front_end.componentes_graficos.compuestos.TreeviewTable import TreeviewTable
from front_end.componentes_graficos.individuales.LtkEntry.LtkEntryLine import LtkEntryLine
from front_end.componentes_graficos.individuales.LtkButton.LtkButtonFill import LtkButtonFill
from front_end.componentes_graficos.individuales.LtkButton.LtkButtonImage import LtkButtonImage
from util.TraducirValores import convertir_hora_a_cadena


class FrameServiciosAdicionales(Frame):

    def __init__(self, master, **kwargs):


        super().__init__(master, **kwargs)


        self.config(bg='white', width=900, height=550)


        self.registrar_datos = RegistrarDatos()
        self.eliminar = EliminarDatos()
        self.actualizar_datos = ActualizarDatos()

        self.barra_busqueda = Frame(self, bg='white')
        self.barra_busqueda.pack(fill=X)

        self.etiqueta = Label(self.barra_busqueda, text="Servicios adicionales: ", bg='white', font=('Poppins', 14, "bold"))
        self.etiqueta.pack(side=LEFT, padx=10, pady = 20)

        self.entrada_busqueda = LtkEntryLine(self.barra_busqueda, 'Buscar por nombre')
        self.entrada_busqueda.pack(side="left",padx=10, pady=20)

        self.boton_agregar = LtkButtonFill(self.barra_busqueda, nombre="Agregar servicio", funcion=lambda: self.agregar())
        self.boton_agregar.pack(side="right", padx=20, pady=20)



        self.frame_tabla = Frame(self, bg='white')
        self.frame_tabla.pack(fill=BOTH, expand=True)

        self.consultar_datos = ConsultarDatosSQL()
        self.consultar_datos.realizar_consulta_simple('ServiciosAdicionales')
        datos_raw = self.consultar_datos.obtener_datos_consulta()

        # Convertir los datos a una lista de listas
        datos = [[convertir_hora_a_cadena(dato) for dato in fila] for fila in datos_raw]
        self.nombre_columnas = ['clave_servicio', 'nombre_servicio', 'descripcion', 'costo_adicional',
                                     'Disponibilidad']

        self.tabla = TreeviewTable(self.frame_tabla, self.nombre_columnas, datos)
        self.tabla.treeview.bind('<<TreeviewSelect>>', self.on_treeview_select)
        self.tabla.pack(fill=BOTH, expand=True)

        self.editar_habitacion_boton = LtkButtonFill(self, nombre="Editar servicio", funcion=lambda: self.editar())
        self.editar_habitacion_boton.disable()
        self.editar_habitacion_boton.pack(side="right", padx=20, pady=20)

        self.boton_eliminar_habitacion = LtkButtonFill(self, nombre="Eliminar servicio",
                                                       funcion=lambda: self.borrar())
        self.boton_eliminar_habitacion.disable()
        self.boton_eliminar_habitacion.pack(side="right", padx=20, pady=20)

    def on_treeview_select(self, event):
        self.editar_habitacion_boton.enable()
        self.boton_eliminar_habitacion.enable()

    def agregar(self):
        def agregar():
            datos = [self.clave_servicio.get_text(), self.nombre_servicio.get_text(), self.descripcion.get_text(),self.costo.get_text(), self.disponibilidad.get_text()]
            self.registrar_datos.registrar_datos(datos, 'ServiciosAdicionales')
            self.ventana.destroy()
            self.actualizar_tabla()

        self.ventana = Toplevel()
        self.ventana.title("Agregar Servicio")


        self.clave_servicio = LtkEntryLine(self.ventana, "Clave")
        self.clave_servicio.pack(padx=10, pady=10)

        self.nombre_servicio = LtkEntryLine(self.ventana, "Nombre servicio")
        self.nombre_servicio.pack(padx=10, pady=10)

        self.descripcion = LtkEntryLine(self.ventana, "Descripcion")
        self.descripcion.pack(padx=10, pady=10)

        self.costo = LtkEntryLine(self.ventana, "Costo")
        self.costo.pack(padx=10, pady=10)

        self.disponibilidad = LtkEntryLine(self.ventana, "Disponibilidad")
        self.disponibilidad.pack(padx=10, pady=10)

        self.boton_agregar = LtkButtonFill(self.ventana, nombre="Agregar servicio", funcion=agregar)
        self.boton_agregar.pack(padx=10, pady=10)

        self.ventana.mainloop()

    def actualizar_tabla(self):
        self.consultar_datos.realizar_consulta_simple('ServiciosAdicionales')
        datos_raw = self.consultar_datos.obtener_datos_consulta()

        # Convertir los datos a una lista de listas
        datos = [[convertir_hora_a_cadena(dato) for dato in fila] for fila in datos_raw]
        self.tabla.actualizar_datos(datos)

    def editar(self):
        datos_habitacion = self.tabla.obtener_datos_seleccionados()[0]  # Obtén la primera lista de la lista de listas

        def editar():
            datos_nuevos = [
                self.clave_servicio.get_text() if self.clave_servicio.get_text() != "" else datos_habitacion[0],
                self.nombre_servicio.get_text() if self.nombre_servicio.get_text() != "" else datos_habitacion[1],
                self.descripcion.get_text() if self.descripcion.get_text() != "" else datos_habitacion[2],
                self.costo_adicional.get_text() if self.costo_adicional.get_text() != "" else datos_habitacion[3],
                self.disponibilidad.get_text() if self.disponibilidad.get_text() != "" else datos_habitacion[4]

            ]

            self.actualizar_datos.actualizar_registro_completo(datos_nuevos, 'ServiciosAdicionales')

            self.ventana.destroy()
            self.actualizar_tabla()


        self.ventana = Toplevel()
        self.ventana.title("Editar Empleado")

        # Aquí llenamos los campos con los datos del empleado si se proporcionan
        self.clave_servicio = LtkEntryLine(self.ventana, f"{datos_habitacion[0]}")
        self.clave_servicio.disable()
        self.clave_servicio.pack(padx=10, pady=10)

        self.nombre_servicio = LtkEntryLine(self.ventana, f"{datos_habitacion[1]}")
        self.nombre_servicio.pack(padx=10, pady=10)

        self.descripcion = LtkEntryLine(self.ventana, f"{datos_habitacion[2]}")
        self.descripcion.pack(padx=10, pady=10)

        self.costo_adicional = LtkEntryLine(self.ventana, f"{datos_habitacion[3]}")
        self.costo_adicional.pack(padx=10, pady=10)

        self.disponibilidad = LtkEntryLine(self.ventana, f"{datos_habitacion[4]}")
        self.disponibilidad.pack(padx=10, pady=10)

        self.boton_agregar = LtkButtonFill(self.ventana, nombre="Editar servicio", funcion=lambda: editar())
        self.boton_agregar.pack(padx=10, pady=10)

        self.ventana.mainloop()

    def borrar(self):
        clave_empleado = self.tabla.obtener_datos_seleccionados()[0][0]
        self.eliminar.eliminar_registro_especifico(clave_empleado, 'ServiciosAdicionales', 'clave_servicio')
        self.actualizar_tabla()




