import allure
from selenium import webdriver

from Alerts_Frame_Windows.Paths import paths_modals
from Funcions import funcions
from Funcions.dateTime import obtener_fecha_hora_actual

#################################################################
############### <<Carga la configuración previa>> ###############
#################################################################

# Inicia las variables Globales necesarias para que sean accesibles
ruta = paths_modals.modal
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
@allure.description("""Esta prueba consiste en probar la funcionalidad de ambos modals""")
def test_modals():

    # Pulsa en el botón para abrir el modal pequeño
    funciones.Click(ruta.button_small)

    # Obtiene el texto contenido en el modal pequeño
    text_small_modal = funciones.getText(ruta.text_small)

    # Comprueba que el texto sea igual al esperado
    assert text_small_modal == ruta.text_expected

    # Capturar de pantalla con fecha actual
    funciones.capturar(obtener_fecha_hora_actual())

    # Cierra el modal pequeño
    funciones.Click(ruta.close_small)

    # Abre el modal grande
    funciones.Click(ruta.button_big)

    # Obtiene el texto contenido en el modal grande
    text_big_modal = funciones.getText(ruta.text_big)

    # Comprueba que el texto sea igual al esperado
    assert text_big_modal == ruta.text_expected_big

    # Capturar de pantalla con fecha actual
    funciones.capturar(obtener_fecha_hora_actual())

    # Cierra el modal grande
    funciones.Click(ruta.close_big)
