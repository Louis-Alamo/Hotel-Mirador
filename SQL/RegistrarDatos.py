import pyodbc

from SQL.DiccionarioExcepciones import DiccionarioExcepciones
from SQL.ConexionSQL import ConexionSQL
class RegistrarDatos(ConexionSQL):

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

    def registrar_datos(self, datos, nombre_tabla):
        try:
            self.iniciar_conexion()

            if nombre_tabla in self.nombresTablas:
                columnas = self.nombresTablas[nombre_tabla]

                consulta_insercion = f"INSERT INTO {nombre_tabla} ({', '.join(columnas)}) VALUES ({', '.join(['?'] * len(columnas))})"

                self.cursor.execute(consulta_insercion, datos)

                self.conexion.commit()

            else:
                print("Tabla no encontrada")

        except pyodbc.Error as e:
            numero_error = e.args[0]
            print(numero_error)
            DiccionarioExcepciones.manejar_error(numero_error, e)

        finally:
            self.cerrar_conexion()


# obj = RegistrarDatos('DESKTOP-F7JSFO9', 'Hotel_Mirador', 'Louis', "panadero123")
# datos = [107, 'Doble', 'Disponible', 100, 'Vista al cielo', 'Wifi, TV, Minibar', '30m, Cama doble', 'Balcon privado']
# obj.registrar_datos(datos, 'Habitacion')