from ventanas.Formularios.servicio_formularios.FormularioServicio import FormularioServicio
from SQL.ActualizarDatos import ActualizarDatos
from tkinter import messagebox

class EditarServicio(FormularioServicio):
        
        def __init__(self, datos_servicio, callback):
            super().__init__(callback=callback)
            self.datos_servicio = datos_servicio
            
            self.cargar_datos()
            
        def cargar_datos(self):
            self.campo_nombre_servicio.set_text(self.datos_servicio[1])
            self.campo_costo_servicio.set_text(self.datos_servicio[2])
            self.campo_clave_servicio.set_text(self.datos_servicio[0])
    
        def aceptar(self):
            
            try:
                lista = [
                    self.campo_clave_servicio.get(),
                    self.campo_nombre_servicio.get(),
                    self.campo_costo_servicio.get()
                ]
                
                obj = ActualizarDatos()
                obj.actualizar_registro_completo(lista, 'Servicio')
                
                messagebox.showinfo("Servicio Actualizado", "Servicio actualizado con exito")
                
                self.on_close()
                
            except Exception as e:
                print(e)
                messagebox.showerror("Error", "Error al actualizar servicio")