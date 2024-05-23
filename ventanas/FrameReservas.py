from tkinter import *
from SQL.ConsultarDatosSQL import ConsultarDatosSQL
from SQL.RegistrarDatos import RegistrarDatos
from SQL.EliminarDatos import EliminarDatos
from SQL.ActualizarDatos import ActualizarDatos
from componentes_graficos.TreeviewTable import TreeviewTable
from componentes_graficos.LtkEntry import LtkEntryLine
from componentes_graficos.LtkButton import LtkButtonFill
from util.TraducirValores import convertir_hora_a_cadena


class FrameReservas(Frame):

    def __init__(self, master, **kwargs):


        super().__init__(master, **kwargs)


        self.config(bg='white', width=900, height=550)


        self.registrar_datos = RegistrarDatos()
        self.eliminar = EliminarDatos()
        self.actualizar_datos = ActualizarDatos()

        self.barra_busqueda = Frame(self, bg='white')
        self.barra_busqueda.pack(fill=X)

        self.etiqueta = Label(self.barra_busqueda, text="Reserva: ", bg='white', font=('Poppins', 14, "bold"))
        self.etiqueta.pack(side=LEFT, padx=10, pady = 20)

        self.entrada_busqueda = LtkEntryLine(self.barra_busqueda, 'Buscar')
        self.entrada_busqueda.pack(side="left",padx=10, pady=20)

        self.boton_agregar = LtkButtonFill(self.barra_busqueda, nombre="Agregar reserva", funcion=lambda: self.agregar())
        self.boton_agregar.pack(side="right", padx=20, pady=20)



        self.frame_tabla = Frame(self, bg='white')
        self.frame_tabla.pack(fill=BOTH, expand=True)

        self.consultar_datos = ConsultarDatosSQL()
        self.consultar_datos.realizar_consulta_simple('Reserva')
        datos_raw = self.consultar_datos.obtener_datos_consulta()

        # Convertir los datos a una lista de listas
        datos = [[convertir_hora_a_cadena(dato) for dato in fila] for fila in datos_raw]
        self.nombre_columnas = ['clave_reserva', 'fecha_inicio_reserva', 'fecha_finalizacion_reserva', 'estado_reserva']

        self.tabla = TreeviewTable(self.frame_tabla, self.nombre_columnas, datos)
        self.tabla.treeview.bind('<<TreeviewSelect>>', self.on_treeview_select)
        self.tabla.pack(fill=BOTH, expand=True)

        self.editar_habitacion_boton = LtkButtonFill(self, nombre="Editar reserva", funcion=lambda: self.editar())
        self.editar_habitacion_boton.disable()
        self.editar_habitacion_boton.pack(side="right", padx=20, pady=20)

        self.boton_eliminar_habitacion = LtkButtonFill(self, nombre="Eliminar reserva",
                                                       funcion=lambda: self.borrar())
        self.boton_eliminar_habitacion.disable()
        self.boton_eliminar_habitacion.pack(side="right", padx=20, pady=20)

    def on_treeview_select(self, event):
        self.editar_habitacion_boton.enable()
        self.boton_eliminar_habitacion.enable()

    def agregar(self):
        pass

    def actualizar_tabla(self):
        self.consultar_datos.realizar_consulta_simple('ServiciosAdicionales')
        datos_raw = self.consultar_datos.obtener_datos_consulta()

        # Convertir los datos a una lista de listas
        datos = [[convertir_hora_a_cadena(dato) for dato in fila] for fila in datos_raw]
        self.tabla.actualizar_datos(datos)
        self.editar_habitacion_boton.disable()
        self.boton_eliminar_habitacion.disable()

    def editar(self):
        pass

    def borrar(self):
        clave_empleado = self.tabla.obtener_datos_seleccionados()[0][0]
        self.eliminar.eliminar_registro_especifico(clave_empleado, 'ServiciosAdicionales', 'clave_servicio')
        self.actualizar_tabla()




