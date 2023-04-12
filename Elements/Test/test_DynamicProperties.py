import time
from selenium.webdriver.common.by import By
from Funcions import funcions
from Elements.Paths import pachs_DynamicProperties
from selenium import webdriver

#################################################################
############### <<Carga la configuración previa>> ###############
#################################################################

# Instancia los objetos necesarios
ruta = pachs_DynamicProperties.dynamic  # Método para obtener los XPATH del formulario Web (llamado TextBox)
driver = None
funciones = None


# Esta es la configuración global para las pruebas (abre el driver y se lo envía mis funciones para iniciarlas)
def setup_function():
    global driver
    global funciones
    driver = webdriver.Chrome()  # Driver Chrome
    funciones = funcions.Global_Funcions(driver)  # Funciones


# Esta es la función que da cierre a cada prueba
def teardown_function():
    print("Fin de la prueba")
    driver.close()


#################################################################
################# <<AQUÍ EMPIEZAN LAS PRUEBAS > #################
#################################################################

def test_botones():
    # Abre el navegador
    funciones.getURL(ruta.URL)

    # Espera a que los botones dinámicos se activen en pantalla
    time.sleep(5.1)

    # Válida el texto dinámico, el cual debe ser igual al resultado esperado
    assert funciones.getText(ruta.TextDynamic) == ruta.TextoBotonDinamico

    # Válida que aparece el botón que no era visible durante los primeros 5 segundos
    assert funciones.searchXP(ruta.VisibleAfter).is_displayed()

    # Válida que el botón deshabilitado ahora está habilitado
    assert funciones.searchXP(ruta.WillEnable5seconds).is_enabled()

    # Obtiene el Color actual mirando el valor "Text-danger" del CSS del botón y guarda el color en una variable
    btn_Color = driver.find_element(by=By.CLASS_NAME, value='text-danger')
    color = btn_Color.value_of_css_property('color')

    # Válida el color del botón es el mismo que el color esperado
    assert color == ruta.ColorEsperado
