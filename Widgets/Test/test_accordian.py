import time

import allure
from selenium import webdriver

from Widgets.Paths.paths_accordian import accordian
from Funcions import funcions
from Funcions.dateTime import obtener_fecha_hora_actual

#################################################################
############### <<Carga la configuración previa>> ###############
#################################################################

# Inicia las variables Globales necesarias para que sean accesibles
ruta = accordian
driver = None
funciones = None

def setup_function():
    global driver, funciones

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

@allure.severity(allure.severity_level.TRIVIAL)
@allure.description("""Esta prueba consiste en probar los acordones y que muestran/ocultan el texto al pulsar 
sobre ellos""")
def test_accordion():

    # Obtiene el texto del acordeon
    obtained_text_one = funciones.getText(ruta.text_one)

    # Comparar el valor obtenido con el esperado y comprueba que el acordeon está desplegado
    assert obtained_text_one == ruta.text_expected_one
    assert funciones.clase(ruta.accordian_one_class) == "collapse show"

    # Hace click en el acordeon 2
    funciones.Click(ruta.section_two)
    time.sleep(.5)
    # Obtiene el texto del acordeon 2a
    obtained_text_two_a = funciones.getText(ruta.text_two_a)

    # Comparar el valor obtenido con el esperado y comprueba que el acordeon está desplegado
    assert obtained_text_two_a == ruta.text_expected_two_a
    assert funciones.clase(ruta.accordian_two_class) == "collapse show"

    # Hace click en el acordeon 3
    funciones.Click(ruta.section_tree)
    time.sleep(.5)
    # Obtiene el texto del acordeon
    obtained_text_tree = funciones.getText(ruta.text_tree)

    # Comparar el valor obtenido con el esperado y comprueba que el acordeon está desplegado
    assert obtained_text_tree == ruta.text_expected_tree
    assert funciones.clase(ruta.accordian_tree_class) == "collapse show"

    # Capturar de pantalla con fecha actual con los acordeones desplegados
    funciones.capturar(obtener_fecha_hora_actual())

    # Colapsa el acordeon 3
    funciones.Click(ruta.section_tree)
    time.sleep(.5)

    # Comprueba que se ha colapsado correctamente
    assert funciones.clase(ruta.accordian_tree_class) == "collapse"

    # Capturar de pantalla con fecha actual con los acordeones desplegados
    funciones.capturar(obtener_fecha_hora_actual())
