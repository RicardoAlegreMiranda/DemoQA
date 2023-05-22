import allure
from datetime import datetime
from selenium import webdriver

from Funcions import funcions
from Widgets.Paths import paths_menu
from Funcions.dateTime import obtener_fecha_hora_actual

#################################################################
############### <<Carga la configuración previa>> ###############
#################################################################

# Inicia las variables Globales necesarias para que sean accesibles
ruta = paths_menu.menu
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

@allure.severity(allure.severity_level.MINOR)
@allure.description("""Se valida que se puede desplegar el menú y que tiene los datos esperados""")
def test_menu():
    # Obtiene los XPATH
    items = ruta.list_items

    # Obtiene los textos esperados
    esperados = ruta.list_text_expected

    # Despliega cada menú y comprueba si el texto obtenido es igual al esperado
    n = 0
    for item in items:
        funciones.move_mouse_to_element(item)
        assert funciones.searchXP(item).text == esperados[n]

        # Hace una captura de pantalla con el submenú desplegado (posición 7 del listado)
        if n == 6:
            # Capturar de pantalla con fecha actual
            funciones.capturar(obtener_fecha_hora_actual())

        n += 1
