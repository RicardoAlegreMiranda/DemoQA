import allure
from selenium import webdriver

from Widgets.Paths.paths_auto_complete import AutoComplete
from Widgets.Funcions_widgets.funcions_auto_complete import FuncionsAutoComplete
from Funcions import funcions
from Funcions.dateTime import obtener_fecha_hora_actual

#################################################################
############### <<Carga la configuración previa>> ###############
#################################################################

# Inicia las variables Globales necesarias para que sean accesibles
ruta = AutoComplete
driver = None
funciones = None
funciones_nativas = None


def setup_function():
    global driver, funciones, funciones_nativas

    # Inicia el Driver y las funciones Globales
    driver = webdriver.Chrome()  # Driver Chrome
    funciones = funcions.Global_Funcions(driver)
    funciones_nativas = FuncionsAutoComplete
    funciones.getURL(ruta.URL)


# Esta es la función que da cierre a cada prueba
def teardown_function():
    print("Fin de la prueba")
    driver.close()


#################################################################
################# <<AQUÍ EMPIEZAN LAS PRUEBAS > #################
#################################################################

@allure.severity(allure.severity_level.NORMAL)
@allure.description("""Se validan los autocompletar""")
def test_auto_complete():
    # Obtiene una lista de colores aleatorios
    colores = funciones_nativas.random_colors()

    # Escribe los colores aleatorios en el campo multiple y después pulsa enter
    for color in colores:
        funciones.writeXP(ruta.text_box_multiple, color)
        funciones.key_enter(ruta.text_box_multiple)

    # Busca los nombres escritos por el nombre de clase y los guarda en una lista
    colores_encontrados = funciones.search_elements_by_class_name(ruta.name_class_complete)

    # Compara los colores encontrados en la web con los obtenidos por el método
    for color_encontrado in colores_encontrados:
        print(color_encontrado.text)
        assert color_encontrado.text in colores

    # Obtiene un color al azar
    color = funciones_nativas.one_color()

    # Escribe el color en el campo de texto individual y pulsa enter
    funciones.writeXP(ruta.text_box_single, color)
    funciones.key_enter(ruta.text_box_single)

    # Busca el color escrito
    color_encontrado_single = funciones.getText(ruta.name_class_complete_single)

    # Lo compara con el color esperado
    assert color_encontrado_single == color

    # Capturar de pantalla con fecha actual con los acordeones desplegados
    funciones.capturar(obtener_fecha_hora_actual())
