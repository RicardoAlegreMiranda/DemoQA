import time
from Funcions import funcions, dateTime
from Elements.Paths import paths_RadioButton
from selenium import webdriver

#################################################################
############### <<Carga la configuración previa>> ###############
#################################################################

# Instancia los objetos necesarios
ruta = paths_RadioButton.radio  # Método para obtener los XPATH del formulario Web (llamado TextBox)
driver = None
funciones = None

# Esta es la configuración global para las pruebas (abre el driver y se lo envía mis funciones para iniciarlas)
def setup_function():
    global driver, funciones
    driver = webdriver.Chrome()  # Driver Chrome
    funciones = funcions.Global_Funcions(driver)  # Funciones

# Esta es la función que da cierre a cada prueba
def teardown_function():
    print("Fin de la prueba")
    driver.close()


#################################################################
##### <<AQUÍ EMPIEZAN LAS PRUEBAS PARA EL RADIO BUTTON>> ########
#################################################################

# Esta prueba consiste en validar los 3 radio-button (incluido el deshabilitado)
def test_RadioButton():

    # Abre el navegador
    funciones.getURL(ruta.URL)

    # Habilita el botón no
    ruta.habilitar_botonNO(driver)

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

    # Válida que pone Sí debajo en la caja de texto
    assert funciones.getText(ruta.result) == ruta.resuttadoEsparadoImpressive
    time.sleep(4)

    # Hace una captura de pantalla
    funciones.capturar(dateTime.obtener_fecha_hora_actual())
