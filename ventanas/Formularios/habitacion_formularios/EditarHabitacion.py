from ventanas.Formularios.habitacion_formularios.FormularioHabitacion import FormularioHabitacion
from SQL.ActualizarDatos import ActualizarDatos
from tkinter import messagebox



class EditarHabitacion(FormularioHabitacion):

    def __init__(self, lista_datos, callback):
        super().__init__(callback=callback)
        self.lista_datos = lista_datos
        print(self.lista_datos)
        self.cargar_datos()
        
        

    def aceptar(self):
        try:
            obj = ActualizarDatos()
            lista = [
                self.campo_clave.get_text(),
                self.tipo_de_habitacion.get(),
                self.estado_habitacion.get(),
                float(self.campo_precio.get_text())
            ]
            
            obj.actualizar_registro_completo(lista, 'Habitacion')
            messagebox.showinfo("Actualización exitosa", "Habitación actualizada correctamente")
            self.on_close()
            
                    
        except ValueError:
            messagebox.showerror("Error", "Error al actualizar la habitación: El precio debe ser un número")
        
        except Exception as e:
            messagebox.showerror("Error", f"Error al actualizar la habitación: {e}")
    

    
    def cargar_datos(self):
        print(self.lista_datos)
        self.campo_clave.set_text(self.lista_datos[0])
        self.tipo_de_habitacion.set(self.lista_datos[1])
        self.estado_habitacion.set(self.lista_datos[2])
        self.campo_precio.set_text(str(self.lista_datos[3]))
