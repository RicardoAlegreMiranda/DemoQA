import time

import allure
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.support.ui import Select

from Widgets.Paths import paths_date_picker
from Widgets.Funcions_widgets.funcions_date_picker import *
from Funcions import funcions
from Funcions.dateTime import obtener_fecha_hora_actual

#################################################################
############### <<Carga la configuración previa>> ###############
#################################################################

# Inicia las variables Globales necesarias para que sean accesibles
ruta = paths_date_picker.DatePicker
driver = None
funciones = None
funciones_nativas = None


def setup_function():
    global driver, funciones, funciones_nativas

    # Inicia el Driver y las funciones Globales
    driver = webdriver.Chrome()  # Driver Chrome
    funciones = funcions.Global_Funcions(driver)
    funciones.getURL(ruta.URL)


# Esta es la función que da cierre a cada prueba
def teardown_function():
    print("Fin de la prueba")
    driver.close()


#################################################################
################# <<AQUÍ EMPIEZAN LAS PRUEBAS > #################
#################################################################

@allure.severity(allure.severity_level.CRITICAL)
@allure.description("""Se validan el select time, se genera una fecha aleatoria y se introduce en el datepicker""")
def test_select_time():

    fecha_aleatoria = genera_fecha_aleatoria()
    print("la fecha es ", str(fecha_aleatoria))

    # Despliega el datepicker
    funciones.Click(ruta.date_picker)

    # Uso el objeto "fecha_objeto" con la propiedad Select para seleccionar el mes
    SelectMes = funciones.searchXP(ruta.month)
    SelectorMes = Select(SelectMes)
    SelectorMes.select_by_value(str((fecha_aleatoria.month - 1)))

    # Selecciono el año del desplegable
    SelectAno = funciones.searchXP(ruta.year)
    SelectorAno = Select(SelectAno)
    SelectorAno.select_by_visible_text(str(fecha_aleatoria.year))

    # Obtiene el xpath del día correcto
    dia_xpath = obtener_xpath_dia(fecha_aleatoria)
    funciones.Click(dia_xpath)

    # Obtiene la fecha escrita de la web
    fecha_escrita = funciones.get_attribute(ruta.date, "value")

    # Convierte la fecha de la web al mismo formato que un objeto fecha
    # (se llama 2 veces a datetime para evitar errores por la clase nativa llamada datetime)
    fecha_escrita_2 = datetime.datetime.strptime(str(fecha_escrita), "%m/%d/%Y")

    # Válida la fecha encontrada contra la fecha generada
    assert fecha_escrita_2 == fecha_aleatoria

    # Capturar de pantalla con fecha actual con los acordeones desplegados
    funciones.capturar(obtener_fecha_hora_actual())