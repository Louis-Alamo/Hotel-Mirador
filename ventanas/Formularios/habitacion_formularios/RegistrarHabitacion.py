from ventanas.Formularios.habitacion_formularios.FormularioHabitacion import RegistrarHabitacion
from SQL.RegistrarDatos import RegistrarDatos

from tkinter import messagebox
class RegistrarHabitacion(RegistrarHabitacion):

    def __init__(self):
        super().__init__()



    def aceptar(self):
        obj = RegistrarDatos()
        lista = [
            self.campo_clave.get_text(),
            self.tipo_de_habitacion.get(),
            self.estado_habitacion.get(),
            float(self.campo_precio.get_text())
        ]
        
        try:
            
            obj.registrar_datos(lista, 'Habitacion')
            messagebox.showinfo("Registro exitoso", "Habitación registrada correctamente")
            self.aceptar()
            
        except Exception as e:
            messagebox.showerror("Error", f"Error al registrar la habitación: {e}")
        
        
    
        
    def validar_datos(self):
        return self.campo_clave.get_text() != "" and self.campo_precio.get_text() != ""
    
    def validar_clave(self):
        return self.campo_clave.get_text()[0] == "H" 