from ventanas.Formularios.servicio_formularios.FormularioServicio import FormularioServicio
from SQL.RegistrarDatos import RegistrarDatos
from tkinter import messagebox

class RegistrarServicio(FormularioServicio):
    
    def __init__(self, callback):
        super().__init__(callback)
        
    
    
    def aceptar(self):
        obj = RegistrarDatos()
        
        try:
            
            lista = [
                self.campo_ID.get(),
                self.campo_nombre_servicio.get(),
                self.campo_descripcion.get(),
                self.campo_costo.get(),
                self.cargo_disponibilidad.get()
                
            ]
            
            obj.registrar_datos(lista, 'Servicio')
            messagebox.showinfo("Servicio Registrado", "Servicio registrado con exito")
            self.on_close()
            
            
        except Exception as e:
            print(e)
            messagebox.showerror("Error", "Error al registrar servicio")