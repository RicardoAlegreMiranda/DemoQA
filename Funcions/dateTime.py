from datetime import datetime


def obtener_fecha_hora_actual():
    # Obtener la fecha y hora actual
    fecha_hora_actual = datetime.now()

    # Formatear la fecha y hora como una cadena de texto
    fecha_hora_actual_str = fecha_hora_actual.strftime("%Y-%m-%d %H:%M:%S")

    return fecha_hora_actual_str