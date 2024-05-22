from tkinter import *
from tkinter import messagebox
from SQL.ConsultarDatosSQL import ConsultarDatosSQL
from SQL.RegistrarDatos import RegistrarDatos
from SQL.EliminarDatos import EliminarDatos
from SQL.ActualizarDatos import ActualizarDatos
from componentes_graficos.TreeviewTable import TreeviewTable
from componentes_graficos.LtkEntry import LtkEntryLine
from componentes_graficos.LtkButton import LtkButtonFill
from util.TraducirValores import convertir_hora_a_cadena

from ventanas.Formularios.cliente_formularios.RegistrarCliente import RegistrarCliente
from ventanas.Formularios.cliente_formularios.EditarCliente import EditarCliente


class FrameClientes(Frame):

    def __init__(self, master, **kwargs):


        super().__init__(master, **kwargs)

        self.config(bg='white', width=900, height=550)


        self.registrar_datos = RegistrarDatos()
        self.eliminar = EliminarDatos()
        self.actualizar_datos = ActualizarDatos()

        self.barra_busqueda = Frame(self, bg='white')
        self.barra_busqueda.pack(fill=X)

        self.etiqueta = Label(self.barra_busqueda, text="Clientes: ", bg='white', font=('Poppins', 14, "bold"))
        self.etiqueta.pack(side=LEFT, padx=10, pady = 20)

        self.entrada_busqueda = LtkEntryLine(self.barra_busqueda, 'Buscar')
        self.entrada_busqueda.pack(side="left",padx=10, pady=20)
        self.entrada_busqueda.bind('<Return>', lambda event: self.buscar_por_clave())

        self.boton_agregar = LtkButtonFill(self.barra_busqueda, nombre="Agregar cliente", funcion=lambda: self.agregar())
        self.boton_agregar.pack(side="right", padx=20, pady=20)



        self.frame_tabla = Frame(self, bg='white')
        self.frame_tabla.pack(fill=BOTH, expand=True)

        self.consultar_datos = ConsultarDatosSQL()
        self.consultar_datos.realizar_consulta_simple('Cliente')
        datos_raw = self.consultar_datos.obtener_datos_consulta()

        # Convertir los datos a una lista de listas
        datos = [[convertir_hora_a_cadena(dato) for dato in fila] for fila in datos_raw]
        self.nombre_columnas = ['clave_cliente', 'nombre_completo', 'apellido_paterno', 'apellido_materno']

        self.tabla = TreeviewTable(self.frame_tabla, self.nombre_columnas, datos)
        self.tabla.treeview.bind('<<TreeviewSelect>>', self.on_treeview_select)
        self.tabla.pack(fill=BOTH, expand=True)

        self.editar_boton = LtkButtonFill(self, nombre="Editar cliente", funcion=lambda: self.editar())
        self.editar_boton.disable()
        self.editar_boton.pack(side="right", padx=20, pady=20)

        self.boton_eliminar = LtkButtonFill(self, nombre="Eliminar servicio",
                                                       funcion=lambda: self.borrar())
        self.boton_eliminar.disable()
        self.boton_eliminar.pack(side="right", padx=20, pady=20)

    def on_treeview_select(self, event):
        self.editar_boton.enable()
        self.boton_eliminar.enable()

    def agregar(self):
        RegistrarCliente(self.actualizar_tabla)
        self.actualizar_tabla()


    def actualizar_tabla(self):
        self.consultar_datos.realizar_consulta_simple('Cliente')
        datos_raw = self.consultar_datos.obtener_datos_consulta()

        # Convertir los datos a una lista de listas
        datos = [[convertir_hora_a_cadena(dato) for dato in fila] for fila in datos_raw]
        self.tabla.actualizar_datos(datos)

    def editar(self):
        datos_habitacion = self.tabla.obtener_datos_seleccionados()[0]  # Obtén la primera lista de la lista de listas
        EditarCliente( datos_habitacion,self.actualizar_tabla)

    def borrar(self):
        datos = self.tabla.obtener_datos_seleccionados()[0]  # Obtén la primera lista de la lista de listas

        respuesta = messagebox.askokcancel("Atencion", f"¿Seguro que quieres eliminar el cliente {datos[1]}?")

        if respuesta:

            obj = ConsultarDatosSQL()

            #Primero eliminamos las instancias de otras tablas
            obj.ejecutar_consulta_otros_medios(f"DELETE CorreoElectronico WHERE clave_correo = '{datos[0]}'")
            obj.ejecutar_consulta_otros_medios(f"DELETE Telefono WHERE clave_telefono = '{datos[0]}'")
            obj.ejecutar_consulta_otros_medios(f"DELETE Cliente WHERE clave_cliente = '{datos[0]}'")
            self.actualizar_tabla()
            messagebox.showinfo("Exito", "Se elimino el cliente")


    def buscar_por_clave(self):
        try:
            obj = ConsultarDatosSQL()
            obj.realizar_consulta_con_condicion('Cliente', f"clave_cliente = '{self.entrada_busqueda.get()}'")

            datos = obj.obtener_datos_consulta()

            if datos:
                EditarCliente(datos[0], self.actualizar_tabla)
            else:
                messagebox.showinfo("Error", "No se encontró ningún empleado con esa clave")

        except Exception as e:
            print(e)
            messagebox.showerror("Error", "Error al buscar empleado")

