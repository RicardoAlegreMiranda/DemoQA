import datetime
import random
import calendar

from Widgets.Paths.paths_date_picker import DatePicker

# Este método genera una fecha aleatoria (día, mes, año, hora y minuto)
def genera_fecha_aleatoria():
    # Generar un año aleatorio entre 1900 y el año actual
    year = random.randint(1900, datetime.datetime.now().year)

    # Generar un mes aleatorio
    month = random.randint(1, 12)

    # Generar un día aleatorio, teniendo en cuenta el mes y el año
    last_day = 31 if month in [1, 3, 5, 7, 8, 10, 12] else 30 if month in [4, 6, 9, 11] else 29 if year % 4 == 0 \
                                                            and (year % 100 != 0 or year % 400 == 0) else 28
    day = random.randint(1, last_day)

    # Generar una hora aleatoria en intervalos de 15 minutos
    hour = random.randint(1, 24)  # formato de 24 horas
    minute = random.randint(0, 3) * 15  # intervalos de 15 minutos

    # Crear un objeto datetime con los valores generados
    fecha = datetime.datetime(year=year, month=month, day=day, hour=hour, minute=minute)
    return fecha

# Genera un XPATH válido para el día
def obtener_xpath_dia(fecha_objeto):

    # Obtener el día de la semana actual
    dia_semana = fecha_objeto.strftime('%A')
    # Obtener el mes actual
    mes = fecha_objeto.strftime('%B')
    # Obtener el día con el formato adecuado
    dia_mes = str(fecha_objeto.day) + (
        'th' if 11 <= fecha_objeto.day <= 13 else {1: 'st', 2: 'nd', 3: 'rd'}.get(fecha_objeto.day % 10, 'th'))
    if dia_mes.startswith('0'):
        dia_mes = dia_mes[1:]
    # Obtener el año
    anio = fecha_objeto.strftime('%Y')
    # EL xpath debe tener un formato similar a este //div[contains(@aria-label,'Choose Sunday, May 3rd, 1987')]
    xpath = f"//div[contains(@aria-label,'Choose {dia_semana}, {mes} {dia_mes}, {anio}')]"
    return xpath


# Este método devuelve el mes en formato nombre en lugar de número
def obtener_mes(mes_numero):
    nombre_mes = calendar.month_name[mes_numero]
    return nombre_mes

# Método para obtener la hora en el formato esperado al enviar el objeto datetime
def obtener_hora(objeto_fecha):
    hora_aleatoria = objeto_fecha.hour
    minuto_aleatorio = objeto_fecha.minute
    hora_aleatoria_str = "{:02d}".format(hora_aleatoria)
    minuto_aleatorio_str = "{:02d}".format(minuto_aleatorio)
    hora_minuto = hora_aleatoria_str + ':' + minuto_aleatorio_str

    # Devuelvo la hora en el formato correcto
    return hora_minuto
