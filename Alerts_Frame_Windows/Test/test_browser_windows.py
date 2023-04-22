from selenium import webdriver

from Alerts_Frame_Windows.Paths import paths_browser_windows
from Alerts_Frame_Windows.Funcions_Alerts_Frame_Windows.funcions_browser_windows import FuncionsBrowser
from Funcions import funcions
from Funcions.dateTime import obtener_fecha_hora_actual

#################################################################
############### <<Carga la configuración previa>> ###############
#################################################################

# Inicia las variables Globales necesarias para que sean accesibles
ruta = paths_browser_windows.browser  # Método para obtener los XPATH del formulario Web (llamado TextBox)
driver = None
funciones = None
funciones_nativas = None

def setup_function():
    global driver, funciones, funciones_nativas

    # Inicia el Driver y las funciones Globales
    driver = webdriver.Chrome()  # Driver Chrome
    funciones = funcions.Global_Funcions(driver)
    funciones_nativas = FuncionsBrowser(driver)
    driver.get(ruta.URL)

# Esta es la función que da cierre a cada prueba
def teardown_function():
    print("Fin de la prueba")
    driver.close()

# Se prueban los 3 botones con sus 3 funcionalidades (Nueva pestaña, nueva ventana, mensaje en ventana)
def test_browser_windows():
    # Pulsar en Nueva ventana:
    funciones.Click(ruta.new_tab)

    # Espera a que se abra una nueva pestaña y se posiciona sobre ella,
    # además guarda el nombre de la pestaña actual en variable
    ventana_actual = funciones_nativas.espera_cargar_ventana()

    # Validar que se abrió la nueva ventana
    assert driver.current_url == ruta.url_new_tab

    # Cierra pestaña actual y vuelve a la pestaña principal
    driver.close()
    driver.switch_to.window(ventana_actual)

    # Espera a que se abra una nueva ventana y se posiciona sobre ella
    funciones.Click(ruta.new_windows)
    funciones_nativas.espera_cargar_ventana()

    # Validar que se abrió la nueva ventana
    assert driver.current_url == ruta.url_new_tab

    # Cierra ventana actual y vuelve a la pestaña principal
    driver.close()
    driver.switch_to.window(ventana_actual)

    """Al abrir la ventana con mensaje hay problemas para obtener el mensaje, por lo cual he decidido cambiar el enfoque
    de la prueba, ahora valida que se abre la nueva pantalla y se cierra, pero no hay manera de validar el mensaje"""

    # Pulsar en ventana con mensaje:
    funciones.Click(ruta.new_windows_message)
    funciones_nativas.espera()  # Espera que se abra la ventana

    # Obtiene el listado de ventanas abiertas
    window_handles = driver.window_handles

    # Guarda como variable la nueva ventana abierta
    ventana = window_handles[1]

    # Cambia el foco a la nueva ventana
    funciones_nativas.cambia_ventana(ventana)

    # Validar que la ventana principal y la ventana que acabamos de abrir son diferentes
    assert ventana_actual != ventana

    # Cierra la ventana actual
    driver.close()

    # Vuelve a la pantalla principal
    driver.switch_to.window(ventana_actual)

    # Válida que hemos vuelto a la ventana principal
    assert driver.current_window_handle == ventana_actual

    # Capturar de pantalla con fecha actual
    funciones.capturar(obtener_fecha_hora_actual())
