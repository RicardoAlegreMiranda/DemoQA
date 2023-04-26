from Elements.Paths.paths_Buttons import buttons
from Funcions import funcions, dateTime
from Funcions.funcions import Global_Funcions
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

#################################################################
############### <<Carga la configuración previa>> ###############
#################################################################

ruta = buttons  # Rutas de los Xpath
driver = None  # Inicio la variable global
funciones = None  # Inicio la variable global
acciones = None  # Acciones


#################################################################
################# <<AQUÍ EMPIEZAN LAS PRUEBAS > #################
#################################################################


# Esta prueba consiste en validar la función de los botones y aviso de los 3 botones en la web

# Esta es la configuración global para las pruebas (abre el driver y se lo envía mis funciones para iniciarlas)
def setup_function():
    global driver, funciones, acciones
    driver = webdriver.Chrome()  # Driver Chrome
    funciones = Global_Funcions(driver)  # Funciones
    acciones = ActionChains(driver)
    funciones.getURL(ruta.URL)

# Esta es la función que da cierre a cada prueba
def teardown_function():
    print("Fin de la prueba")
    driver.close()


def test_clickBotones():

    # Doble Click
    btnDobleClick = funciones.searchXP(ruta.doubleclick)
    acciones.double_click(btnDobleClick).perform()

    # Validar que se muestra el aviso correcto de doble Click
    assert funciones.getText(ruta.mensajeDoubleClick) == ruta.mensajeDobleClickOK

    # Right Click
    btnRightClick = funciones.searchXP(ruta.rightclick)
    acciones.context_click(btnRightClick).perform()

    # Validar que se muestra el aviso correcto de Click derecho
    assert funciones.getText(ruta.mensajeRightClik) == ruta.mensajeRightClickOK

    # Click Dinámico (este botón cambia de ID constantemente) Se usa el full-XPATH para localizarlo
    funciones.Click(ruta.click)

    # Validar que se muestra el aviso correcto de Click derecho
    assert funciones.getText(ruta.mensajeClickMe) == ruta.mensajeClickOK

    # Hace una captura de pantalla
    funciones.capturar(dateTime.obtener_fecha_hora_actual())
