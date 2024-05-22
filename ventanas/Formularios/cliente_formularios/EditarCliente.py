from ventanas.Formularios.cliente_formularios.FormularioCliente import FormularioCliente
from SQL.ConsultarDatosSQL import ConsultarDatosSQL
from SQL.ActualizarDatos import ActualizarDatos
from SQL.EliminarDatos import EliminarDatos
from tkinter import messagebox


class EditarCliente(FormularioCliente):

    def __init__(self, datos_cliente, callback):
        super().__init__(callback=callback)
        self.datos_cliente = datos_cliente


        obj = ConsultarDatosSQL()
        obj.realizar_consulta_con_condicion('Telefono', f"clave_telefono = '{self.datos_cliente[0]}'")
        lista_telefono = obj.obtener_datos_consulta()

        obj.realizar_consulta_con_condicion('CorreoElectronico', f"clave_correo = '{self.datos_cliente[0]}'")
        lista_correo = obj.obtener_datos_consulta()

        self.cargar_datos(lista_telefono, lista_correo)
        
    def cargar_datos(self, lista_telefono, lista_correo):
        self.campo_nombre_completo.set_text(self.datos_cliente[1])
        self.campo_apellido_paterno.set_text(self.datos_cliente[2])
        self.campo_apellido_materno.set_text(self.datos_cliente[3])
        self.campo_clave_cliente.set_text(self.datos_cliente[0])

        self.campo_telefono1.set_text(lista_telefono[0][1])
        self.campo_correo1.set_text(lista_correo[0][1])
        
        if len(lista_telefono) > 1:
            self.campo_telefono2.set_text(lista_telefono[1][1])
        
        if len(lista_correo) > 1:
            self.campo_correo2.set_text(lista_correo[1][1])

    def aceptar(self):
        
        try:
            lista_cliente = [
                self.campo_clave_cliente.get(),
                self.campo_nombre_completo.get(),
                self.campo_apellido_paterno.get(),
                self.campo_apellido_materno.get()
            ]
            
            lista_telefono = [
                self.campo_clave_cliente.get(),
                self.campo_telefono1.get()
            ]
            
            lista_correo = [
                self.campo_clave_cliente.get(),
                self.campo_correo1.get()
            ]
            
            obj = ActualizarDatos()
            obj.actualizar_registro_completo(lista_cliente, 'Cliente')
            obj.actualizar_registro_completo(lista_telefono, 'Telefono')
            obj.actualizar_registro_completo(lista_correo, 'CorreoElectronico')

            if self.campo_telefono2.get() != "":
                obj = EliminarDatos()
                obj.eliminar_registro_especifico(self.campo_clave_cliente.get(), 'Telefono', 'clave_telefono')

            if self.campo_correo2.get() != "":
                obj = EliminarDatos()
                obj.eliminar_registro_especifico(self.campo_clave_cliente.get(), 'CorreoElectronico', 'clave_correo')

            messagebox.showinfo("Cliente Actualizado", "Cliente actualizado con exito")
            self.on_close()
        
        except Exception as e:
            print(e)
            return
    
