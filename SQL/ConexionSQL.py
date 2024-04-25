import pyodbc
from SQL.DiccionarioExcepciones import DiccionarioExcepciones
import os
import json

class ConexionSQL:

    def __init__(self):

        dir_path = os.path.dirname(os.path.realpath(__file__))

        # Construir la ruta al archivo JSON
        json_path = os.path.join(dir_path, '../archivos/DatosBD.json')

        with open(json_path, 'r') as f:
            self.credenciales = json.load(f)

        self.servidor = self.credenciales["SERVER"]
        self.bd = self.credenciales["DATABASE"]
        self.usuario = self.credenciales["USER"]
        self.contrasena = self.credenciales["PASSWORD"]
        self.conexion = None
        self.cursor = None

    def iniciar_conexion(self):
        try:
            self.conexion = pyodbc.connect(
                'DRIVER={ODBC Driver 17 for SQL server}; SERVER=' + self.servidor + ';DATABASE=' + self.bd +
                ';UID=' + self.usuario + ';PWD=' + self.contrasena + '')
            self.cursor = self.conexion.cursor()
            print("Conexion exitosa")

        except pyodbc.Error as e:
            DiccionarioExcepciones.manejar_error(e.args[0], e)

    def cerrar_conexion(self):
        try:

            if self.cursor:
                self.cursor.close()

            if self.conexion:
                self.conexion.close()
            print("Se cerro correctamente la base de datos")

        except pyodbc.Error as e:
            DiccionarioExcepciones.manejar_error(e.args[0], e)



# obj = ConexionSQL()
# obj.iniciar_conexion()