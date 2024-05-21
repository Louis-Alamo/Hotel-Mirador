import datetime
from tkinter import *
from SQL.ConsultarDatosSQL import ConsultarDatosSQL
from SQL.RegistrarDatos import RegistrarDatos
from SQL.EliminarDatos import EliminarDatos
from SQL.ActualizarDatos import ActualizarDatos
from componentes_graficos.TreeviewTable import TreeviewTable
from componentes_graficos.LtkEntry import LtkEntryLine
from componentes_graficos.LtkButton import LtkButtonFill
from util.TraducirValores import convertir_hora_a_cadena
from Excepciones.NullValueException import NullValueException

from ventanas.Formularios.habitacion_formularios.RegistrarHabitacion import RegistrarHabitacion
from ventanas.Formularios.habitacion_formularios.EditarHabitacion import EditarHabitacion

class FrameHabitacion(Frame):

    def __init__(self, master, **kwargs):


        super().__init__(master, **kwargs)


        self.config(bg='white', width=900, height=550)


        self.registrar_datos = RegistrarDatos()
        self.eliminar_habitacion = EliminarDatos()
        self.actualizar_datos = ActualizarDatos()

        self.barra_busqueda = Frame(self, bg='white')
        self.barra_busqueda.pack(fill=X)

        self.etiqueta = Label(self.barra_busqueda, text="Habitacion: ", bg='white', font=('Poppins', 14, "bold"))
        self.etiqueta.pack(side=LEFT, padx=10, pady = 20)

        self.entrada_busqueda = LtkEntryLine(self.barra_busqueda, 'Buscar por clave')
        self.entrada_busqueda.pack(side="left",padx=10, pady=20)
        self.entrada_busqueda.bind('<Return>', lambda event: self.buscar_por_clave())


        self.boton_agregar = LtkButtonFill(self.barra_busqueda, nombre="Agregar habitacion", funcion=lambda: self.agregar_habitacion())
        self.boton_agregar.pack(side="right", padx=20, pady=20)



        self.frame_tabla = Frame(self, bg='white')
        self.frame_tabla.pack(fill=BOTH, expand=True)

        self.consultar_datos = ConsultarDatosSQL()
        self.consultar_datos.realizar_consulta_simple('Habitacion')
        datos_raw = self.consultar_datos.obtener_datos_consulta()

        # Convertir los datos a una lista de listas
        datos = [[convertir_hora_a_cadena(dato) for dato in fila] for fila in datos_raw]
        self.nombre_columnas = ['numero_habitacion', 'tipo_habitacion', 'estado_habitacion', 'precio_noche']

        self.tabla = TreeviewTable(self.frame_tabla, self.nombre_columnas, datos)
        self.tabla.treeview.bind('<<TreeviewSelect>>', self.on_treeview_select)
        self.tabla.pack(fill=BOTH, expand=True)

        self.editar_habitacion_boton = LtkButtonFill(self, nombre="Editar Empleado", funcion=lambda: self.editar_habitacion())
        self.editar_habitacion_boton.disable()
        self.editar_habitacion_boton.pack(side="right", padx=20, pady=20)

        self.boton_eliminar_habitacion = LtkButtonFill(self, nombre="Eliminar Empleado",funcion=lambda: self.borrar_habitacion())
        self.boton_eliminar_habitacion.disable()
        self.boton_eliminar_habitacion.pack(side="right", padx=20, pady=20)



    def on_treeview_select(self, event):
        self.editar_habitacion_boton.enable()
        self.boton_eliminar_habitacion.enable()

    def agregar_habitacion(self):
        RegistrarHabitacion(self.actualizar_tabla)
        self.actualizar_tabla()
        
    def on_cerrar_ventana_emergente(self):
        self.actualizar_tabla()

    def actualizar_tabla(self):
        self.consultar_datos.realizar_consulta_simple('Habitacion')
        datos_raw = self.consultar_datos.obtener_datos_consulta()

        # Convertir los datos a una lista de listas
        datos = [[convertir_hora_a_cadena(dato) for dato in fila] for fila in datos_raw]
        self.tabla.actualizar_datos(datos)

    def editar_habitacion(self):
        try:
            datos_habitacion = self.tabla.obtener_datos_seleccionados()[0]  # Obtén la primera lista de la lista de listas
            EditarHabitacion(datos_habitacion, self.actualizar_tabla)
            self.actualizar_tabla()
        except NullValueException as e:
            print(f"Error al editar la habitación: {e}")



    def borrar_habitacion(self):
        try:
            clave_empleado = self.tabla.obtener_datos_seleccionados()[0][0]
            self.eliminar_habitacion.eliminar_registro_especifico(clave_empleado, 'Habitacion', 'numero_habitacion')
            self.actualizar_tabla()
        except Exception as e:
            print(f"Error al borrar la habitación: {e}")

    def buscar_por_clave(self):
        try:
            obj = ConsultarDatosSQL()
            obj.realizar_consulta_con_condicion('Habitacion', f"numero_habitacion = '{self.entrada_busqueda.get()}'")
            datos = obj.obtener_datos_consulta()
            datos_lista = [[dato if not isinstance(dato, datetime.time) else dato.strftime('%H:%M') for dato in fila] for
                           fila in datos]

            datos_lista = datos_lista[0]
            print(datos_lista)

            EditarHabitacion(datos_lista, self.actualizar_tabla)

        except Exception as e:
            print(f"Error al buscar la habitación: {e}")




