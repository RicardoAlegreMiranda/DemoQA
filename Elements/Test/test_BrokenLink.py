from Funcions import funcions
from Elements.Paths import paths_BrokenLink
from selenium import webdriver

#################################################################
############### <<Carga la configuración previa>> ###############
#################################################################

# Instancia los objetos necesarios
ruta = paths_BrokenLink.brokenLink  # Método para obtener los XPATH del formulario Web (llamado TextBox)
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
################ <<AQUÍ EMPIEZAN LAS PRUEBAS>> ##################
#################################################################

# Esta prueba consiste en validar que se cargan las imágenes de la web con el tamaño esperado
def test_imágenes():
    # Abre el navegador
    funciones.getURL(ruta.URL)

    # Obtiene las medidas la imagen 1
    imagen1 = funciones.searchXP(ruta.imagen1)
    ancho_imagen = imagen1.size['width']
    alto_imagen = imagen1.size['height']
    print("ancho " + str(ancho_imagen) + " Alto " + str(alto_imagen))

    # Válida que la imagen1 tenga el tamaño esperado (ni muy grande ni muy pequeña)
    assert (300 < ancho_imagen < 500) and (80 < alto_imagen < 160)

    # Obtiene las medidas la imagen 2
    imagen2 = funciones.searchXP(ruta.imagen2)
    ancho_imagen2 = imagen2.size['width']
    alto_imagen2 = imagen2.size['height']
    print("ancho " + str(ancho_imagen2) + " Alto " + str(alto_imagen2))

    # Válida que la imagen2 tenga el tamaño esperado (ni muy grande ni muy pequeña)
    assert (100 < ancho_imagen2 < 500) and (50 < alto_imagen2 < 250)


# Esta prueba consiste en validar que los links funcionan correctamente al pulsar sobre ellos
def test_links():
    # Abre el navegador
    funciones.getURL(ruta.URL)

    # Click en el primer link y espera que cargue la página
    funciones.Click(ruta.link1)
    driver.implicitly_wait(5)

    # Valida que el link nos lleva a la URL que esperamos
    assert driver.current_url == ruta.URLESperada

    #  vuelve atrás y espera a que cargue la página
    driver.back()
    driver.implicitly_wait(5)

    # Click en el segundo link del navegador y espera a que cargue
    funciones.Click(ruta.link2)
    driver.implicitly_wait(5)

    # Valida que el link nos lleva a la URL que esperamos
    assert driver.current_url == ruta.URLESperada
