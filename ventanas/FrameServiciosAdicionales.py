import datetime
from tkinter import *
from SQL.ConsultarDatosSQL import ConsultarDatosSQL
from SQL.RegistrarDatos import RegistrarDatos
from SQL.EliminarDatos import EliminarDatos
from SQL.ActualizarDatos import ActualizarDatos
from componentes_graficos.TreeviewTable import TreeviewTable
from componentes_graficos.LtkEntry import LtkEntryLine
from componentes_graficos.LtkButton import LtkButtonFill
from ventanas.Formularios.servicio_formularios.RegistrarServicio import RegistrarServicio
from ventanas.Formularios.servicio_formularios.EditarServicio import EditarServicio
from util.TraducirValores import convertir_hora_a_cadena
from tkinter import messagebox

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
        self.entrada_busqueda.bind('<Return>', lambda event: self.buscar_por_clave())


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
        registrar_servicio = RegistrarServicio(self.actualizar_tabla)
        self.actualizar_tabla()
        self.editar_habitacion_boton.disable()
        self.boton_eliminar_habitacion.disable()

    def actualizar_tabla(self):
        self.consultar_datos.realizar_consulta_simple('ServiciosAdicionales')
        datos_raw = self.consultar_datos.obtener_datos_consulta()

        # Convertir los datos a una lista de listas
        datos = [[convertir_hora_a_cadena(dato) for dato in fila] for fila in datos_raw]
        self.tabla.actualizar_datos(datos)
        self.editar_habitacion_boton.disable()
        self.boton_eliminar_habitacion.disable()

    def editar(self):
        datos_habitacion = self.tabla.obtener_datos_seleccionados()[0]  # Obtén la primera lista de la lista de listas

        try:

            editar_habitacion = EditarServicio(datos_habitacion, self.actualizar_tabla)
            self.actualizar_tabla()
            self.editar_habitacion_boton.disable()
            self.boton_eliminar_habitacion.disable()

        except Exception as e:
            messagebox.showinfo("Atencion", "No se ha seleccionado ningún servicio adicional")

    def borrar(self):
        clave_empleado = self.tabla.obtener_datos_seleccionados()[0][0]

        try:
            self.eliminar.eliminar_registro_especifico(clave_empleado, 'ServiciosAdicionales', 'clave_servicio')
            self.actualizar_tabla()
            self.editar_habitacion_boton.disable()
            self.boton_eliminar_habitacion.disable()

        except Exception as e:
            messagebox.showinfo("Atencion", "No se ha seleccionado ningún servicio adicional")


    def buscar_por_clave(self):
        obj = ConsultarDatosSQL()
        obj.realizar_consulta_con_condicion('ServiciosAdicionales', f"clave_servicio = '{self.entrada_busqueda.get()}'")
        datos = obj.obtener_datos_consulta()
        datos_lista = [[dato if not isinstance(dato, datetime.time) else dato.strftime('%H:%M') for dato in fila] for
                       fila in datos]

        datos_lista = datos_lista[0]
        print(datos_lista)

        EditarServicio(datos_lista, self.actualizar_tabla)
        self.editar_habitacion_boton.disable()
        self.boton_eliminar_habitacion.disable()
