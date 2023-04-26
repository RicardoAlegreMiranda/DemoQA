import allure
from selenium import webdriver

from Alerts_Frame_Windows.Paths import paths_nested_frames
from Funcions import funcions
from Funcions.dateTime import obtener_fecha_hora_actual

#################################################################
############### <<Carga la configuración previa>> ###############
#################################################################

# Inicia las variables Globales necesarias para que sean accesibles
ruta = paths_nested_frames.nested
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

@allure.severity(allure.severity_level.NORMAL)
@allure.description("""Esta prueba consiste en probar la funcionalidad de los iframes anidados""")
def test_parents_iframes():

    # Encuentra los iframes
    frame_padre = funciones.searchXP(ruta.parent_frame)

    # Cambia el foco a parent frame
    driver.switch_to.frame(frame_padre)

    # Busca el frame hijo
    frame_hijo = funciones.searchXP(ruta.child_frame)

    # Guarda el texto del frame padre
    texto_padre = funciones.searchXP(ruta.text_parent).text

    # Compara el texto obtenido con el texto esperado
    assert texto_padre == ruta.text_expect_parent_frame

    # Cambia el foco a parent frame
    driver.switch_to.frame(frame_hijo)

    # Guarda el texto del frame hijo
    texto_hijo = funciones.searchXP(ruta.text_child).text

    # Compara el texto obtenido con el texto esperado
    assert texto_hijo == ruta.text_expect_child_frame

    # Capturar de pantalla con fecha actual
    funciones.capturar(obtener_fecha_hora_actual())
