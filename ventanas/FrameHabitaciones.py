from tkinter import *
from SQL.ConsultarDatosSQL import ConsultarDatosSQL
from SQL.RegistrarDatos import RegistrarDatos
from SQL.EliminarDatos import EliminarDatos
from SQL.ActualizarDatos import ActualizarDatos
from componentes_graficos.TreeviewTable import TreeviewTable
from componentes_graficos.LtkEntry import LtkEntryLine
from componentes_graficos.LtkButton import LtkButtonFill
from util.TraducirValores import convertir_hora_a_cadena


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

        self.entrada_busqueda = LtkEntryLine(self.barra_busqueda, 'Buscar por nombre')
        self.entrada_busqueda.pack(side="left",padx=10, pady=20)

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

        self.boton_eliminar_habitacion = LtkButtonFill(self, nombre="Eliminar Empleado",
                                                       funcion=lambda: self.borrar_habitacion())
        self.boton_eliminar_habitacion.disable()
        self.boton_eliminar_habitacion.pack(side="right", padx=20, pady=20)

    def on_treeview_select(self, event):
        self.editar_habitacion_boton.enable()
        self.boton_eliminar_habitacion.enable()

    def agregar_habitacion(self):
        print("Agregar empleado")
        def agregar():
            datos = [self.numero_habitacion.get_text(), self.tipo_habitacion.get_text(), self.estado_habitacion.get_text(), self.precio_por_noche.get_text()]
            self.registrar_datos.registrar_datos(datos, 'Habitacion')
            self.ventana.destroy()
            self.actualizar_tabla()

        self.ventana = Toplevel()
        self.ventana.title("Agregar Habitacion")


        self.numero_habitacion = LtkEntryLine(self.ventana, "Numero habitacion")
        self.numero_habitacion.pack(padx=10, pady=10)

        self.tipo_habitacion = LtkEntryLine(self.ventana, "Tipo habitacion")
        self.tipo_habitacion.pack(padx=10, pady=10)

        self.estado_habitacion = LtkEntryLine(self.ventana, "Estado habitacion")
        self.estado_habitacion.pack(padx=10, pady=10)

        self.precio_por_noche = LtkEntryLine(self.ventana, "Precio por noche")
        self.precio_por_noche.pack(padx=10, pady=10)


        self.boton_agregar = LtkButtonFill(self.ventana, nombre="Agregar Habitacion", funcion=agregar)
        self.boton_agregar.pack(padx=10, pady=10)

        self.ventana.mainloop()

    def actualizar_tabla(self):
        self.consultar_datos.realizar_consulta_simple('Habitacion')
        datos_raw = self.consultar_datos.obtener_datos_consulta()

        # Convertir los datos a una lista de listas
        datos = [[convertir_hora_a_cadena(dato) for dato in fila] for fila in datos_raw]
        self.tabla.actualizar_datos(datos)

    def editar_habitacion(self):
        datos_habitacion = self.tabla.obtener_datos_seleccionados()[0]  # Obtén la primera lista de la lista de listas

        def editar():
            datos_nuevos = [
                self.numero_habitacion.get_text() if self.numero_habitacion.get_text() != "" else datos_habitacion[0],
                self.tipo_habitacion.get_text() if self.tipo_habitacion.get_text() != "" else datos_habitacion[1],
                self.estado_habitacion.get_text() if self.estado_habitacion.get_text() != "" else datos_habitacion[2],
                self.precio_por_noche.get_text() if self.precio_por_noche.get_text() != "" else datos_habitacion[3],
            ]

            print(datos_nuevos)
            # self.borrar_empleado()
            # self.registrar_datos.registrar_datos(datos_nuevos, 'Empleado')

            self.actualizar_datos.actualizar_registro_completo(datos_nuevos, 'Habitacion')

            self.ventana.destroy()
            self.actualizar_tabla()


        self.ventana = Toplevel()
        self.ventana.title("Editar Empleado")

        # Aquí llenamos los campos con los datos del empleado si se proporcionan
        self.numero_habitacion = LtkEntryLine(self.ventana, f"{datos_habitacion[0]}")
        self.numero_habitacion.disable()
        self.numero_habitacion.pack(padx=10, pady=10)

        self.tipo_habitacion = LtkEntryLine(self.ventana, f"{datos_habitacion[1]}")
        self.tipo_habitacion.pack(padx=10, pady=10)

        self.estado_habitacion = LtkEntryLine(self.ventana, f"{datos_habitacion[2]}")
        self.estado_habitacion.pack(padx=10, pady=10)

        self.precio_por_noche = LtkEntryLine(self.ventana, f"{datos_habitacion[3]}")
        self.precio_por_noche.pack(padx=10, pady=10)

        self.boton_agregar = LtkButtonFill(self.ventana, nombre="Editar habitacion", funcion=lambda: editar())
        self.boton_agregar.pack(padx=10, pady=10)

        self.ventana.mainloop()

    def borrar_habitacion(self):
        clave_empleado = self.tabla.obtener_datos_seleccionados()[0][0]
        self.eliminar_habitacion.eliminar_registro_especifico(clave_empleado, 'Habitacion', 'numero_habitacion')
        self.actualizar_tabla()



