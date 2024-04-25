from SQL.DiccionarioExcepciones import DiccionarioExcepciones
from SQL.ConexionSQL import ConexionSQL
import pyodbc


class EliminarDatos(ConexionSQL):

    def __init__(self):
        super().__init__()

        self.nombresTablas = {
            'Cliente': ['clave_cliente', 'nombre_completo', 'apellido_paterno', 'apellido_materno'],
            'Telefono': ['clave_cliente', 'telefono'],
            'CorreoElectronico': ['clave_cliente', 'correo_electronico'],
            'Habitacion': ['numero_habitacion', 'tipo_habitacion', 'estado_habitacion', 'precio_noche'],
            'DetallesHabitacion': ['clave_detalle', 'nombre_detalle'],
            'Empleado': ['clave_empleado', 'nombre_completo', 'apellido_paterno', 'apellido_materno', 'cargo',
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



    def eliminar_registro_especifico(self, clave_eliminar, tabla, nombre_columna):

        try:
            self.iniciar_conexion()
            consulta_eliminar = f"DELETE FROM {tabla} WHERE {nombre_columna} = ?"
            self.cursor.execute(consulta_eliminar, clave_eliminar)

            self.conexion.commit()

        except pyodbc.Error as e:
            numero_error = e.args[0]
            DiccionarioExcepciones.manejar_error(numero_error, e)

        finally:
            self.cerrar_conexion()





# obj = EliminarDatos('DESKTOP-7OM9T1J', 'Hotel_Mirador', 'Louis', "panadero123")
# obj.eliminar_registro(107, 'Habitacion', 'Numero_de_Habitacion')
