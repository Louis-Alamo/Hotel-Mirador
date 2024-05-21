from ventanas.Formularios.empleado_formularios.FormularioEmpleado import FormularioEmpleado
from SQL.ActualizarDatos import ActualizarDatos
from tkinter import messagebox

class EditarEmpleado(FormularioEmpleado):
    
        def __init__(self, datos_empleado, callback):
            super().__init__(callback=callback)
            self.datos_empleado = datos_empleado
            
            self.cargar_datos()
            
        def cargar_datos(self):
            self.campo_nombre_completo.set_text(self.datos_empleado[1])
            self.campo_apellido_paterno.set_text(self.datos_empleado[2])
            self.campo_apellido_materno.set_text(self.datos_empleado[3])
            self.campo_clave_empleado.set_text(self.datos_empleado[0])
            self.cargo_empleado.set_text(self.datos_empleado[4])
            self.hora_entrada.set_text(self.datos_empleado[5])
            self.hora_salida.set_text(self.datos_empleado[6])
    
        def aceptar(self):
            
            try:
                lista = [
                    self.campo_nombre_completo.get(),
                    self.campo_apellido_paterno.get(),
                    self.campo_apellido_materno.get(),
                    self.campo_clave_empleado.get(),
                    self.cargo_empleado.get(),
                    self.horario_entrada.get(),
                    self.horario_salida.get()
                ]
                
                obj = ActualizarDatos()
                obj.actualizar_registro_completo(lista, 'Empleado')
                
                messagebox.showinfo("Empleado Actualizado", "Empleado actualizado con exito")
                
                self.on_close()
                
            except Exception as e:
                print(e)
                messagebox.showerror("Error", "Error al actualizar empleado")