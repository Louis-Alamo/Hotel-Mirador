from ventanas.Formularios.empleado_formularios.FormularioEmpleado import FormularioEmpleado
from SQL.RegistrarDatos import RegistrarDatos
from SQL.ConsultarDatosSQL import ConsultarDatosSQL
from tkinter import messagebox

from Excepciones.DataException import ClaveInvalidaException


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
            

        except ClaveInvalidaException as e:
            messagebox.showerror("Error", "Error al registrar empleado, clave ya existe")

        except ValueError as e:
            messagebox.showerror("Error", "Error al registrar empleado, valor inválido ingresado")

        except TypeError as e:
            messagebox.showerror("Error", "Error al registrar empleado, tipo de dato incorrecto ingresado")

        except Exception as e:
            print(e)
            messagebox.showerror("Error", "Error al registrar empleado")


    def comprobar_clave_primaria(self):
        obj = ConsultarDatosSQL()
        obj.realizar_consulta_simple('Empleado')
        datos = obj.obtener_datos_consulta()

        for dato in datos:
            if dato[0] == self.campo_clave_empleado.get():
                raise ClaveInvalidaException("La clave ya existe en la base de datos")

