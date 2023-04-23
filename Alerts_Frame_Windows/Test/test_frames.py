from selenium import webdriver

from Alerts_Frame_Windows.Paths import paths_frames
from Funcions import funcions
from Funcions.dateTime import obtener_fecha_hora_actual

#################################################################
############### <<Carga la configuración previa>> ###############
#################################################################

# Inicia las variables Globales necesarias para que sean accesibles
ruta = paths_frames.frames  # Método para obtener los XPATH del formulario Web (llamado TextBox)
driver = None
funciones = None

def setup_function():
    global driver, funciones

    # Inicia el Driver y las funciones Globales
    driver = webdriver.Chrome()  # Driver Chrome
    funciones = funcions.Global_Funcions(driver)
    driver.get(ruta.URL)

# Esta es la función que da cierre a cada prueba
def teardown_function():
    print("Fin de la prueba")
    driver.close()

def test_frames():
    # Guarda los iFrames en variables
    iframe_big = funciones.searchXP(ruta.frame_big_1)
    iframe_little = funciones.searchXP(ruta.frame_little)

    # Cambia al iFrame
    driver.switch_to.frame(iframe_big)

    # Obtiene el texto del iFrame
    text_big = funciones.searchXP(ruta.texto_big).text

    # Compara el texto del iframe con el texto esperado
    assert text_big == ruta.text_big_expected

    # Vuelve a la web (sale del iFrame actual)
    driver.switch_to.default_content()

    # Cambia al iFrame secundario
    driver.switch_to.frame(iframe_little)

    # Obtiene el texto del iFrame
    text_little = funciones.searchXP(ruta.texto_little).text
    assert text_little == ruta.text_big_expected

    # Vuelve a la web (sale del iFrame actual)
    driver.switch_to.default_content()

    # Cambia el ancho y el alto del iframe
    driver.execute_script("arguments[0].style.width='500px'; arguments[0].style.height='350px';", iframe_little)

    # Capturar de pantalla con fecha actual
    funciones.capturar(obtener_fecha_hora_actual())
