import json
import os


def comprobar_acceso(nombre_empleado, clave):

    print("Directorio de trabajo: " + os.getcwd())

    with open(r'../archivos/clave_acceso.json', 'r') as f:
        credenciales = json.load(f)

    if nombre_empleado in credenciales:
        if credenciales[nombre_empleado] == clave:
            return True

    return False