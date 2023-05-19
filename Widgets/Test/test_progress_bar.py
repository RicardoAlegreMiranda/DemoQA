import time

import allure
from datetime import datetime
import random
from selenium import webdriver

from Funcions import funcions
from Widgets.Paths import paths_progress_bar
from Widgets.Funcions_widgets import funcions_progress_bar
from Funcions.dateTime import obtener_fecha_hora_actual

#################################################################
############### <<Carga la configuración previa>> ###############
#################################################################

# Inicia las variables Globales necesarias para que sean accesibles
ruta = paths_progress_bar.ProgressBar
driver = None
funciones = None
funciones_nativas = None

# Datos para la prueba
porcentaje_uno = 100

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

"""A tener en cuenta que hay un retardo de 1 segundo al pulsar el botón para detener el progress bar, 
por lo cual me es imposible para el progress bar en el momento exacto que necesito para la prueba,
por eso para el assert permito una tolerancia de 6 puntos entre el dato aleatorio y el dato obtenido del progressbar"""


@allure.severity(allure.severity_level.TRIVIAL)
@allure.description("""Valida que el progress bar llega al 100 y a un número generado aleatoriamente""")
def test_progress_bar():
    # Progress bar al 100%
    prueba_uno = funcions_progress_bar.start_stop(driver, porcentaje_uno)

    # Valida el valor del progress bar
    assert prueba_uno == porcentaje_uno

    # Genera un número aleatorio del 1 al 99 para la segunda prueba:
    porcentaje_dos = random.randint(1, 99)
    print("Número aleatorio para prueba 2 es :", porcentaje_dos)
    # Ejecuta el progress bar a un porcentaje aleatorio del 1 al 99
    prueba_dos = funcions_progress_bar.start_stop(driver, porcentaje_dos)

    # Válida el valor del progress bar no tenga una diferencia mayor a 6 puntos
    assert (prueba_dos - porcentaje_dos) < 6
