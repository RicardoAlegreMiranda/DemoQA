from selenium import webdriver

from Alerts_Frame_Windows.Funcions_Alerts_Frame_Windows.funcions_alerts import FuncionsAlerts
from Alerts_Frame_Windows.Paths import paths_alerts
from Funcions import funcions
from Funcions.dateTime import obtener_fecha_hora_actual

#################################################################
############### <<Carga la configuración previa>> ###############
#################################################################

# Inicia las variables Globales necesarias para que sean accesibles
ruta = paths_alerts.alerts  # Método para obtener los XPATH del formulario Web (llamado TextBox)
driver = None
funciones = None
funciones_nativas = None

def setup_function():
    global driver, funciones, funciones_nativas

    # Inicia el Driver y las funciones Globales
    driver = webdriver.Chrome()  # Driver Chrome
    funciones = funcions.Global_Funcions(driver)
    funciones_nativas = FuncionsAlerts(driver)
    driver.get(ruta.URL)

# Esta es la función que da cierre a cada prueba
def teardown_function():
    print("Fin de la prueba")
    driver.close()

def test_alerts():

    # Hace clic en el botón 1
    funciones.Click(ruta.boton1)

    # Validar que el texto del alert es el esperado y hace clic en aceptar
    assert funciones_nativas.obtener_alerta().text == ruta.text_expected1
    funciones_nativas.obtener_alerta().accept()

    # Hace clic en el botón 2
    funciones.Click(ruta.boton2)

    # Válida el texto del segundo alert, además espera el tiempo necesario a que salga
    assert funciones_nativas.obtener_alerta().text == ruta.text_expected2
    funciones_nativas.obtener_alerta().accept()

    # Hace clic en el botón 3
    funciones.Click(ruta.boton3)

    # Acepta el alert
    funciones_nativas.obtener_alerta().accept()

    # Válida que sale el mensaje esperado en la pantalla
    assert funciones.getText(ruta.confirm_result) == ruta.text_expected_ok

    # Pulsa de nuevo el botón 3
    funciones.Click(ruta.boton3)

    # Pulsar en Cancelar en el alert
    funciones_nativas.obtener_alerta().dismiss()

    # Válida que sale el mensaje esperado en la pantalla
    assert funciones.getText(ruta.confirm_result) == ruta.text_expected_cancel

    # Pulsar el botón 4
    funciones.Click(ruta.boton4)

    # Cambiar al alert, escribe el mensaje y cancela
    alerta_mensaje = funciones_nativas.obtener_alerta()
    alerta_mensaje.send_keys(ruta.text_prompt)
    alerta_mensaje.dismiss()

    # Comprueba que NO se ha escrito nada
    assert not funciones.searchXP(ruta.prompt_result)

    # Pulsar el botón 4
    funciones.Click(ruta.boton4)

    # Cambiar al alert, escribe el mensaje y acepta
    alerta_mensaje = funciones_nativas.obtener_alerta()
    alerta_mensaje.send_keys(ruta.text_prompt)
    alerta_mensaje.accept()

    # Comprueba que se ha escrito el mensaje y que es el mensaje esperado
    assert funciones.getText(ruta.prompt_result) == ruta.text_expected_prompt

    # Capturar de pantalla con fecha actual
    funciones.capturar(obtener_fecha_hora_actual())
