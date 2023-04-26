from selenium import webdriver

from Elements.Paths.paths_RadioButton import radio, habilitar_btn_no
from Funcions import funcions, dateTime

#################################################################
############### <<Carga la configuración previa>> ###############
#################################################################

# Instancia los objetos necesarios
ruta = radio
funciones = None
driver = None

# Esta es la configuración global para las pruebas (abre el driver y se lo envía mis funciones para iniciarlas)
def setup_function():
    global driver, funciones
    driver = webdriver.Chrome()  # Driver Chrome
    funciones = funcions.Global_Funcions(driver)  # Funciones
    funciones.getURL(ruta.URL)  # Abre el navegador


# Esta es la función que da cierre a cada prueba
def teardown_function():
    print("Fin de la prueba")
    driver.close()

#################################################################
##### <<AQUÍ EMPIEZAN LAS PRUEBAS PARA EL RADIO BUTTON>> ########
#################################################################

# Esta prueba consiste en validar los 3 "radio-button" (incluido el deshabilitado)
def test_RadioButton():

    # Habilita el botón no
    habilitar_btn_no(driver)

    # Pulsa en NO
    funciones.Click(ruta.Noes)

    # Pulsa en Sí
    funciones.Click(ruta.Yes)

    # Válida que pone Sí debajo en la caja de texto
    assert funciones.getText(ruta.result) == ruta.resultadoEsperadoYes

    # Pulsa en impresionado
    funciones.Click(ruta.Impressive)

    # Hace una captura de pantalla
    funciones.capturar(dateTime.obtener_fecha_hora_actual())

    # Válida que pone Impressive debajo en la caja de texto
    assert funciones.getText(ruta.result) == ruta.resuttadoEsparadoImpressive

    # Hace otra captura de pantalla
    funciones.capturar(dateTime.obtener_fecha_hora_actual())
