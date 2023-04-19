from Elements.Paths.paths_CheckBox import CheckBox, dato_obtenido
from Funcions import funcions, dateTime
from selenium import webdriver


#################################################################
############### <<Carga la configuración previa>> ###############
#################################################################

ruta = CheckBox  # Rutas de los Xpath
driver = None
funciones = None
datos_obtenidos = []

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

def test_CheckBox1():
    # Abre el navegador:
    funciones.getURL(ruta.URL)

    # Despliega todos los CheckBox (hace Click en cada uno de ellos)
    for n in ruta.Desplegar:
        funciones.Click(n)

    # Click en opciones esperadas (word, desktop, angular, general)
    for h in ruta.Seleccionar:
        funciones.Click(h)

    # Hace una captura de pantalla
    funciones.capturar(dateTime.obtener_fecha_hora_actual())

    # Click para Replegar todas las opciones
    funciones.Click(ruta.desplegale)

    # Este bucle llama al método que sirve para obtener los datos que muestra la pantalla y los guarda en una lista
    for numero in range(2, len(ruta.text_expected)):
        dato = dato_obtenido(numero, driver)
        datos_obtenidos.append(dato)

    # Este bucle compara los datos obtenidos en pantalla con los datos esperados
    n = 0
    for obtenido in datos_obtenidos:
        assert obtenido in ruta.text_expected
        n += 1
