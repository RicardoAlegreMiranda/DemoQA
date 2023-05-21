import time

import allure
from datetime import datetime
from selenium import webdriver

from Funcions import funcions
from Widgets.Funcions_widgets import funcions_tools_tips
from Widgets.Paths import paths_tools_tips
from Funcions.dateTime import obtener_fecha_hora_actual

#################################################################
############### <<Carga la configuración previa>> ###############
#################################################################

# Inicia las variables Globales necesarias para que sean accesibles
ruta = paths_tools_tips.ToolsTips
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
@allure.description("""Se valida que se muestra  el mensaje esperado al pasar por encima el ratón de los 
elementos web correspondientes""")
def test_slider():

    # Obtiene los Xpath a de los elementos
    lista = ruta.list_elements

    # Obtiene los textos esperados para cada elemento
    lista_texto_esperado = ruta.lists_expected_text

    # Bucle para obtener el texto de cada elemento y compararlo con el texto esperado
    n = 0
    for xpath in lista:
        # Busca el elemento web
        elemento = funciones.searchXP(xpath)

        # Obtiene el texto del elemento web con la función propia
        texto = funcions_tools_tips.obtener_texto_elemento(driver, elemento)

        # Imprime el texto obtenido, lo compara con el texto esperado y obtiene una captura de pantalla
        print(texto)
        assert texto == lista_texto_esperado[n]
        n += 1
        # Capturar de pantalla con fecha actual
        funciones.capturar(obtener_fecha_hora_actual())
