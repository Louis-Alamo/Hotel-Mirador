from ventanas.Formularios.cliente_formularios.FormularioCliente import FormularioCliente
from SQL.RegistrarDatos import RegistrarDatos
from tkinter import messagebox 
class RegistrarCliente(FormularioCliente):

    def __init__(self, callback):
        super().__init__(callback=callback)

        self.ventana.title("Registrar Cliente")

        self.ejecutar_ventana()
        
    
    def aceptar(self):
        
        try: 
            lista_cliente = [
                self.campo_nombre_completo.get(),
                self.campo_apellido_paterno.get(),
                self.campo_apellido_materno.get(),
                self.campo_clave_cliente.get()
            ]
            
            lista_telefono = [
                self.campo_clave_cliente.get(),
                self.campo_telefono.get()
            ]
            
            lista_correo = [
                self.campo_clave_cliente.get(),
                self.campo_correo.get()
            ]
            
            obj = RegistrarDatos()
            
            obj.registrar_datos(lista_cliente, 'Cliente')
            obj.registrar_datos(lista_telefono, 'Telefono')
            obj.registrar_datos(lista_correo, 'CorreoElectronico')
            
            if self.campo_correo2.get() != "":
                lista_correo2 = [
                    self.campo_clave_cliente.get(),
                    self.campo_correo2.get()
                ]
                
                obj.registrar_datos(lista_correo2, 'CorreoElectronico')
            
            if self.campo_telefono2.get() != "":
                lista_telefono2 = [
                    self.campo_clave_cliente.get(),
                    self.campo_telefono2.get()
                ]
                
                obj.registrar_datos(lista_telefono2, 'Telefono')
            messagebox.showinfo("Cliente Registrado", "Cliente registrado con exito")
            
            self.on_close()
            
        except Exception as e:
            messagebox.showerror("Error", "Error al registrar cliente")
            print(e)
            