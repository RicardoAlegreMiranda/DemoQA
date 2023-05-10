import time

import allure
from datetime import datetime
from selenium import webdriver

from Funcions import funcions
from Widgets.Funcions_widgets import funcions_slider
from Widgets.Paths import paths_slider
from Funcions.dateTime import obtener_fecha_hora_actual

#################################################################
############### <<Carga la configuración previa>> ###############
#################################################################

# Inicia las variables Globales necesarias para que sean accesibles
ruta = paths_slider.slider
driver = None
funciones = None
funciones_nativas = None
funciones_slider = None


def setup_function():
    global driver, funciones, funciones_nativas, funciones_slider

    # Inicia el Driver y las funciones Globales
    driver = webdriver.Chrome()  # Driver Chrome
    funciones = funcions.Global_Funcions(driver)
    funciones.getURL(ruta.URL)

    slider = funciones.searchXP(ruta.slider)
    funciones_slider = funcions_slider.SliderFuncions(driver, slider)

# Esta es la función que da cierre a cada prueba
def teardown_function():
    print("Fin de la prueba")
    driver.close()


#################################################################
################# <<AQUÍ EMPIEZAN LAS PRUEBAS > #################
#################################################################

@allure.severity(allure.severity_level.MINOR)
@allure.description("""Se generan 3 números aleatorios del 1 al 100, se ponen en el slider y se validan, 
además valida que el valor por defecto es 25""")
def test_slider():
    # Obtiene el valor actual del slider y lo válida que por defecto debe ser 25
    valor_1 = funciones.get_attribute(ruta.slider, "value")
    assert valor_1 == "25"

    # Obtiene 3 números aleatorios del 1 al 100 para probar
    numeros_aleatorios = funciones_slider.numeros_aleatorios()

    # arrastra el slider a la posición aleatoria 1
    for numero in numeros_aleatorios:
        # Mueve el slider a la posición indicada
        funciones_slider.arrastrar_slider(numero)

        # Obtiene el valor actual del slider y lo válida que corresponde al último número aleatorio
        valor_2 = funciones.get_attribute(ruta.slider, "value")
        assert int(valor_2) == numero

    # Capturar de pantalla con fecha actual
    funciones.capturar(obtener_fecha_hora_actual())

