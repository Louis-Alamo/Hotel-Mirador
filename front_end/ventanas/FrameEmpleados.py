import time
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


class FrameEmpleados(Frame):

    def __init__(self, master, **kwargs):


        super().__init__(master, **kwargs)


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
        print("Agregar empleado")
        def agregar():
            datos = [self.clave_empleado.get_text(),self.nombre.get_text(), self.apellido_paterno.get_text(), self.apellido_materno.get_text(), self.cargo.get_text(), self.hora_entrada.get_text(), self.hora_salida.get_text()]
            self.registrar_datos.registrar_datos(datos, 'Empleado')
            self.ventana.destroy()
            self.actualizar_tabla()

        self.ventana = Toplevel()
        self.ventana.title("Agregar Empleado")


        self.clave_empleado = LtkEntryLine(self.ventana, "Clave Empleado")
        self.clave_empleado.pack(padx=10, pady=10)

        self.nombre = LtkEntryLine(self.ventana, "Nombre")
        self.nombre.pack(padx=10, pady=10)

        self.apellido_paterno = LtkEntryLine(self.ventana, "Apellido Paterno")
        self.apellido_paterno.pack(padx=10, pady=10)

        self.apellido_materno = LtkEntryLine(self.ventana, "Apellido Materno")
        self.apellido_materno.pack(padx=10, pady=10)

        self.cargo = LtkEntryLine(self.ventana, "Cargo")
        self.cargo.pack(padx=10, pady=10)

        self.hora_entrada = LtkEntryLine(self.ventana, "Hora de Entrada")
        self.hora_entrada.pack(padx=10, pady=10)

        self.hora_salida = LtkEntryLine(self.ventana, "Hora de Salida")
        self.hora_salida.pack(padx=10, pady=10)

        self.boton_agregar = LtkButtonFill(self.ventana, nombre="Agregar Empleado", funcion=agregar)
        self.boton_agregar.pack(padx=10, pady=10)

        self.ventana.mainloop()

    def actualizar_tabla(self):
        self.consultar_datos.realizar_consulta_simple('Empleado')
        datos_raw = self.consultar_datos.obtener_datos_consulta()

        # Convertir los datos a una lista de listas
        datos = [[convertir_hora_a_cadena(dato) for dato in fila] for fila in datos_raw]
        self.tabla.actualizar_datos(datos)

    def editar_empleado(self):
        datos_empleado = self.tabla.obtener_datos_seleccionados()[0]  # Obtén la primera lista de la lista de listas

        def editar():
            datos_nuevos = [
                self.clave_empleado.get_text() if self.clave_empleado.get_text() != "" else datos_empleado[0],
                self.nombre.get_text() if self.nombre.get_text() != "" else datos_empleado[1],
                self.apellido_paterno.get_text() if self.apellido_paterno.get_text() != "" else datos_empleado[2],
                self.apellido_materno.get_text() if self.apellido_materno.get_text() != "" else datos_empleado[3],
                self.cargo.get_text() if self.cargo.get_text() != "" else datos_empleado[4],
                self.hora_entrada.get_text() if self.hora_entrada.get_text() != "" else datos_empleado[5],
                self.hora_salida.get_text() if self.hora_salida.get_text() != "" else datos_empleado[6]
            ]

            print(datos_nuevos)
            # self.borrar_empleado()
            # self.registrar_datos.registrar_datos(datos_nuevos, 'Empleado')

            self.actualizar_datos.actualizar_registro_completo(datos_nuevos, 'Empleado')

            self.ventana.destroy()
            self.actualizar_tabla()


        self.ventana = Toplevel()
        self.ventana.title("Editar Empleado")

        # Aquí llenamos los campos con los datos del empleado si se proporcionan
        self.clave_empleado = LtkEntryLine(self.ventana, f"{datos_empleado[0]}")
        self.clave_empleado.disable()
        self.clave_empleado.pack(padx=10, pady=10)

        self.nombre = LtkEntryLine(self.ventana, f"{datos_empleado[1]}")
        self.nombre.pack(padx=10, pady=10)

        self.apellido_paterno = LtkEntryLine(self.ventana, f"{datos_empleado[2]}")
        self.apellido_paterno.pack(padx=10, pady=10)

        self.apellido_materno = LtkEntryLine(self.ventana, f"{datos_empleado[3]}")
        self.apellido_materno.pack(padx=10, pady=10)

        self.cargo = LtkEntryLine(self.ventana, f"{datos_empleado[4]}")
        self.cargo.pack(padx=10, pady=10)

        self.hora_entrada = LtkEntryLine(self.ventana, f"{datos_empleado[5]}")
        self.hora_entrada.pack(padx=10, pady=10)

        self.hora_salida = LtkEntryLine(self.ventana, f"{datos_empleado[6]}")
        self.hora_salida.pack(padx=10, pady=10)

        self.boton_agregar = LtkButtonFill(self.ventana, nombre="Editar Empleado", funcion=lambda: editar())
        self.boton_agregar.pack(padx=10, pady=10)

        self.ventana.mainloop()

    def borrar_empleado(self):
        clave_empleado = self.tabla.obtener_datos_seleccionados()[0][0]
        self.eliminar_empleado.eliminar_registro_especifico(clave_empleado, 'Empleado', 'numero_habitacion')
        self.actualizar_tabla()


