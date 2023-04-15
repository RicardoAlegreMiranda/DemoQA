from Elements.Paths.paths_Links import links
from Funcions import funcions
from selenium import webdriver


#################################################################
############### <<Carga la configuración previa>> ###############
#################################################################

ruta = links   # Rutas de los Xpath
driver = None
funciones = None

#################################################################
################# <<AQUÍ EMPIEZAN LAS PRUEBAS > #################
#################################################################

# Esta es la configuración global para las pruebas (abre el driver y se lo envía mis funciones para iniciarlas)
def setup_function():
    global driver, funciones
    driver = webdriver.Chrome()  # Driver Chrome
    funciones = funcions.Global_Funcions(driver)  # Funciones

# Esta es la función que da cierre a cada prueba
def teardown_function():
    print("Fin de la prueba")
    driver.close()

def test_Links():

    # Abre el navegador
    funciones.getURL(ruta.URL)

    # Localiza los links con el método propio
    enlaces = funciones.enlaces()

    # Iterar a través de los elementos de enlace y guarda los links en una lista
    ListaLinks =  []
    for enlace in enlaces:
        url = enlace.get_attribute("href")
        ListaLinks.append(url)
        print(url)

    # Convertir todos los elementos de la lista en Strings
    ListaLinksSTR = [str(elemento) for elemento in ListaLinks]

    # Creo una lista para guardar los links filtrados
    ListaFiltrada = []

    # Eliminar de la Lista los elementos que no tengan HTTP (Para filtrar links no deseados)
    for n in ListaLinksSTR:
        if "http" in n:
            ListaFiltrada.append(n)

    for link in ListaFiltrada:

        funciones.getURL(link)

        # Aquí se Valida que la URL actual es que misma del Link (para ver si el link funciona)
        assert driver.current_url == link
