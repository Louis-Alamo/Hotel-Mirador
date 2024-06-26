from SQL.DiccionarioExcepciones import DiccionarioExcepciones
from SQL.ConexionSQL import ConexionSQL
import pyodbc


class ConsultarDatosSQL(ConexionSQL):

    def __init__(self):
        super().__init__()

        self.datos_consulta = None

    def realizar_consulta_simple(self, NombreTabla):
        self.ejecutar_consulta(f"SELECT * FROM {NombreTabla}")

    def realizar_consulta_con_condicion(self, NombreTabla, condicion):
        self.ejecutar_consulta(f"SELECT * FROM {NombreTabla} WHERE {condicion}")

    def ejecutar_consulta(self, query):
        try:
            self.iniciar_conexion()
            self.cursor.execute(query)
            self.datos_consulta = self.cursor.fetchall()
            #self._mostrar_consulta(self.datos_consulta)

        except pyodbc.Error as e:
            numero_error = e.args[0]
            DiccionarioExcepciones.manejar_error(numero_error, e)

        finally:
            self.cerrar_conexion()

    def ejecutar_consulta_otros_medios(self, query):
        try:
            self.iniciar_conexion()
            self.cursor.execute(query)
            self.cursor.commit()

        except pyodbc.Error as e:
            numero_error = e.args[0]
            DiccionarioExcepciones.manejar_error(numero_error, e)

        finally:
            self.cerrar_conexion()

    def _mostrar_consulta(self, arreglo):

        while arreglo:
            print(arreglo)
            arreglo = self.cursor.fetchone()

    def obtener_datos_consulta(self):
        return self.datos_consulta

