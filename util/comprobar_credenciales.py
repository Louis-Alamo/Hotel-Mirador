import json
import os


def comprobar_acceso(nombre_empleado, clave):
    # Obtener la ruta absoluta del directorio actual
    dir_path = os.path.dirname(os.path.realpath(__file__))

    # Construir la ruta al archivo JSON
    json_path = os.path.join(dir_path, '../archivos/clave_acceso.json')

    with open(json_path, 'r') as f:
        credenciales = json.load(f)

    if nombre_empleado in credenciales:
        if credenciales[nombre_empleado] == clave:
            return True

    return False
