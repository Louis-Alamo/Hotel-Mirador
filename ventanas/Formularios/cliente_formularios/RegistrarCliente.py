from ventanas.Formularios.cliente_formularios.FormularioCliente import FormularioCliente
from SQL.RegistrarDatos import RegistrarDatos
from tkinter import messagebox 
class RegistrarCliente(FormularioCliente):

    def __init__(self, callback):
        super().__init__(callback=callback)

        self.ventana.title("Registrar Cliente")


        
    
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
            
            obj = RegistrarDatos()
            
            obj.registrar_datos(lista_cliente, 'Cliente')
            obj.registrar_datos(lista_telefono, 'Telefono')
            obj.registrar_datos(lista_correo, 'CorreoElectronico')

            if self.campo_telefono2.get() != "":
                obj.registrar_datos([self.campo_clave_cliente.get(), self.campo_telefono2.get()], 'Telefono')

            if self.campo_correo2.get() != "":
                obj.registrar_datos([self.campo_clave_cliente.get(), self.campo_correo2.get()], 'CorreoElectronico')


            messagebox.showinfo("Cliente Registrado", "Cliente registrado con exito")
            
            self.on_close()
            
        except Exception as e:
            messagebox.showerror("Error", "Error al registrar cliente")
            print(e)
            