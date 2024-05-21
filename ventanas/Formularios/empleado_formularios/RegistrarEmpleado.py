from ventanas.Formularios.empleado_formularios.FormularioEmpleado import FormularioEmpleado
from SQL.RegistrarDatos import RegistrarDatos
from tkinter import messagebox


class RegistrarEmpleado(FormularioEmpleado):

    def __init__(self, callback):
        super().__init__(callback)
        
    
    
    def aceptar(self):
        obj = RegistrarDatos()
        
        try:
            
            lista = [
                self.campo_clave_empleado.get(),
                self.campo_nombre_completo.get(),
                self.campo_apellido_paterno.get(),
                self.campo_apellido_materno.get(),
                self.cargo_empleado.get(),
                self.horario_entrada.get(),
                self.horario_salida.get()
                
            ]
            obj.registrar_datos(lista, 'Empleado')
            messagebox.showinfo("Empleado Registrado", "Empleado registrado con exito")
            self.on_close()
            
            
        except Exception as e:
            print(e)
            messagebox.showerror("Error", "Error al registrar empleado")