from SQL.ConexionSQL import ConexionSQL
import pyodbc
from SQL.DiccionarioExcepciones import DiccionarioExcepciones

class ActualizarDatos(ConexionSQL):

    def __init__(self):
        super().__init__()
        self.nombresTablas = {
            'Cliente': ['clave_cliente', 'nombre_completo', 'apellido_paterno', 'apellido_materno'],
            'Telefono': ['clave_cliente', 'telefono'],
            'CorreoElectronico': ['clave_cliente', 'correo_electronico'],
            'Habitacion': ['numero_habitacion', 'tipo_habitacion', 'estado_habitacion', 'precio_noche'],
            'DetallesHabitacion': ['clave_detalle', 'nombre_detalle'],
            'Empleado': ['numero_habitacion', 'nombre_completo', 'apellido_paterno', 'apellido_materno', 'cargo',
                         'hora_entrada', 'hora_salida'],
            'ServiciosAdicionales': ['clave_servicio', 'nombre_servicio', 'descripcion', 'costo_adicional',
                                     'Disponibilidad'],
            'ClienteReserva': ['clave_cliente', 'clave_reserva'],
            'Reserva': ['clave_reserva', 'fecha_inicio_reserva', 'fecha_finalizacion_reserva', 'estado_reserva',
                        'numero_habitacion'],
            'Pagos': ['clave_pago', 'detalles_transaccion', 'Fecha_de_pago', 'hora_pago', 'metodo_pago'],
            'ReservaPagos': ['clave_reserva', 'clave_pago'],
            'ReservaServicios': ['clave_reserva', 'clave_servicio'],
            'ReservaHabitacion': ['clave_reserva', 'clave_habitacion']
        }


    def actualizar_registro(self, dato_actualizar, nombre_tabla, nombre_columna, nombre_columna_clave, valor_clave):
        try:
            self.iniciar_conexion()

            consulta_actualizar = f"UPDATE {nombre_tabla} SET {nombre_columna} = ? WHERE {nombre_columna_clave} = ?"
            self.cursor.execute(consulta_actualizar, dato_actualizar, valor_clave)
            self.cursor.commit()

        except pyodbc.Error as e:
            numero_error = e.args[0]
            DiccionarioExcepciones.manejar_error(numero_error, e)

        finally:
            self.cerrar_conexion()

    def actualizar_registro_completo(self, datos, nombre_tabla):
        try:
            self.iniciar_conexion()

            if nombre_tabla in self.nombresTablas:
                columnas = self.nombresTablas[nombre_tabla]

                # Ignoramos la primera columna (la clave) en la lista de columnas a actualizar
                consulta_actualizacion = f"UPDATE {nombre_tabla} SET {', '.join([f'{columna} = ?' for columna in columnas[1:]])} WHERE {columnas[0]} = ?"

                # Pasamos los datos a la consulta, ignorando el primer dato (la clave)
                self.cursor.execute(consulta_actualizacion, *(datos[1:] + [datos[0]]))

                self.conexion.commit()

            else:
                print("Tabla no encontrada")

        except pyodbc.Error as e:
            numero_error = e.args[0]
            print(numero_error)
            DiccionarioExcepciones.manejar_error(numero_error, e)

        finally:
            self.cerrar_conexion()


# obj = ActualizarDatos('DESKTOP-7OM9T1J','Hotel_Mirador','Louis',"panadero123")
# obj.actualizar_registro('suit', 'Habitacion', 'Tipo_de_habitacion', 'Numero_de_habitacion', 101)



