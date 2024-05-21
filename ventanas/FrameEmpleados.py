from tkinter import *
from SQL.ConsultarDatosSQL import ConsultarDatosSQL
from SQL.RegistrarDatos import RegistrarDatos
from SQL.EliminarDatos import EliminarDatos
from SQL.ActualizarDatos import ActualizarDatos
from componentes_graficos.TreeviewTable import TreeviewTable
from componentes_graficos.LtkEntry import LtkEntryLine
from componentes_graficos.LtkButton import LtkButtonFill
from util.TraducirValores import convertir_hora_a_cadena
from ventanas.Formularios.empleado_formularios.RegistrarEmpleado import RegistrarEmpleado
from ventanas.Formularios.empleado_formularios.EditarEmpleado import EditarEmpleado
import os


class FrameEmpleados(Frame):

    def __init__(self, master, **kwargs):


        super().__init__(master, **kwargs)

        dir_path = os.path.dirname(os.path.abspath(__file__))
        print("Path de login: ", dir_path)


        self.config(bg='white', width=900, height=550)


        self.registrar_datos = RegistrarDatos()
        self.eliminar_empleado = EliminarDatos()
        self.actualizar_datos = ActualizarDatos()

        self.barra_busqueda = Frame(self, bg='white')
        self.barra_busqueda.pack(fill=X)

        self.etiqueta = Label(self.barra_busqueda, text="Empleados:", bg='white', font=('Poppins', 14, "bold"))
        self.etiqueta.pack(side=LEFT, padx=10, pady = 20)

        self.entrada_busqueda = LtkEntryLine(self.barra_busqueda, 'Buscar por nombre')
        self.entrada_busqueda.pack(side="left",padx=10, pady=20)

        self.boton_agregar = LtkButtonFill(self.barra_busqueda, nombre="Agregar Empleado",  funcion=lambda:self.agregar_empleado())
        self.boton_agregar.pack(side="right", padx=20, pady=20)



        self.frame_tabla = Frame(self, bg='white')
        self.frame_tabla.pack(fill=BOTH, expand=True)

        self.consultar_datos = ConsultarDatosSQL()
        self.consultar_datos.realizar_consulta_simple('Empleado')
        datos_raw = self.consultar_datos.obtener_datos_consulta()

        # Convertir los datos a una lista de listas
        datos = [[convertir_hora_a_cadena(dato) for dato in fila] for fila in datos_raw]
        self.nombre_columnas = ['numero_habitacion', 'nombre_completo', 'apellido_paterno', 'apellido_materno', 'cargo',
                                'hora_entrada', 'hora_salida']

        self.tabla = TreeviewTable(self.frame_tabla, self.nombre_columnas, datos)
        self.tabla.treeview.bind('<<TreeviewSelect>>', self.on_treeview_select)
        self.tabla.pack(fill=BOTH, expand=True)

        self.editar_empleado_boton = LtkButtonFill(self, nombre="Editar Empleado",  funcion=lambda: self.editar_empleado())
        self.editar_empleado_boton.disable()
        self.editar_empleado_boton.pack(side="right", padx=20, pady=20)

        self.boton_eliminar_empleado = LtkButtonFill(self, nombre="Eliminar Empleado",
                                                     funcion=lambda: self.borrar_empleado())
        self.boton_eliminar_empleado.disable()
        self.boton_eliminar_empleado.pack(side="right", padx=20, pady=20)

    def on_treeview_select(self, event):
        self.editar_empleado_boton.enable()
        self.boton_eliminar_empleado.enable()

    def agregar_empleado(self):
        registrar_empleado = RegistrarEmpleado(self.actualizar_tabla)

    def actualizar_tabla(self):
        self.consultar_datos.realizar_consulta_simple('Empleado')
        datos_raw = self.consultar_datos.obtener_datos_consulta()

        # Convertir los datos a una lista de listas
        datos = [[convertir_hora_a_cadena(dato) for dato in fila] for fila in datos_raw]
        self.tabla.actualizar_datos(datos)

    def editar_empleado(self):
        datos_empleado = self.tabla.obtener_datos_seleccionados()[0]  # Obtén la primera lista de la lista de listas
        editar_empleado = EditarEmpleado(datos_empleado, self.actualizar_tabla)
  

    def borrar_empleado(self):
        clave_empleado = self.tabla.obtener_datos_seleccionados()[0][0]
        self.eliminar_empleado.eliminar_registro_especifico(clave_empleado, 'Empleado', 'clave_empleado')
        self.actualizar_tabla()


