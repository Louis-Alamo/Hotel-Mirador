import datetime


def convertir_hora_a_cadena(hora):
    if isinstance(hora, datetime.time):
        return hora.strftime('%H:%M')
    return hora