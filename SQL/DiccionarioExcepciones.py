class DiccionarioExcepciones:
    Excepciones = {
        '42S22': "Nombre de columna inválida o inexistente. ",
        '42S02': "El nombre de la tabla no encontrada",
        '23000': "Violación de restricción de clave única",

        '28000': "Acceso denegado. ",
        '22003': "Valor numérico fuera de rango. "
    }

    @staticmethod
    def manejar_error(numero_excepcion, excepcion):
        mensaje_error = DiccionarioExcepciones.Excepciones.get(numero_excepcion)

        if mensaje_error:
            print(f"Excepcion: Numero: {numero_excepcion}, mensaje: {mensaje_error}")

        else:
            print(f"Excepción SQL no reconocida con numero -{numero_excepcion}-: {excepcion}")

#'42000': "Sintaxis SQL incorrecta.",