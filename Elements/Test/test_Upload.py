import os
import time
from Funcions import funcions, dateTime
from Elements.Paths import pach_Upload
from selenium import webdriver

#################################################################
############### <<Carga la configuración previa>> ###############
#################################################################

# Instancia los objetos necesarios
ruta = pach_Upload.Upload
driver = None
funciones = None

# Obtener la ruta de la carpeta actual
ruta_carpeta_descarga = os.getcwd()

# Configurar las opciones de Chrome
options = webdriver.ChromeOptions()

# Establecer la carpeta de descarga (para la prueba de descargar el archivo)
prefs = {'download.default_directory': ruta_carpeta_descarga}
options.add_experimental_option('prefs', prefs)


# Esta es la configuración global para las pruebas (abre el driver y se lo envía mis funciones para iniciarlas)
def setup_function():
    global driver, funciones
    driver = webdriver.Chrome(options=options)  # Driver Modificado con carpeta de descarga diferente
    funciones = funcions.Global_Funcions(driver)  # Funciones
    funciones.getURL(ruta.URL)  # Abre el navegador

# Esta es la función que da cierre a cada prueba
def teardown_function():
    print("Fin de la prueba")
    driver.close()


#################################################################
################# <<AQUÍ EMPIEZAN LAS PRUEBAS > #################
#################################################################

# Esta prueba válida que la imagen se sube de manera correcta
def test_carga_imagen():

    # Obtén la ruta del directorio actual
    ruta_actual = os.path.dirname(os.path.abspath(__file__))
    # Modifica la ruta actual para que tenga el formato esperado
    ruta_imagen_modificada = ruta_actual.replace("\\", "//")
    # Convierte la ruta actual modifica a la ruta del archivo JPG
    archivoJPG = ruta.ruta_relativa(ruta_imagen_modificada)

    # Sube la imagen JPG a la Web
    funciones.writeXP(ruta.Upload, archivoJPG)

    # Lee el mensaje de subida
    Texto_Subida = funciones.getText(ruta.Confirma_Subida)

    # Se valida que el nombre del archivo (tester.jpg) aparece en como subido en la Web
    assert "tester.jpg" in Texto_Subida

    # Hace una captura de pantalla
    funciones.capturar(dateTime.obtener_fecha_hora_actual())


# Esta prueba válida que se descarga la imagen de manera correcta
def test_Descarga():

    # Pulsa en Download para descargar la imagen
    funciones.Click(ruta.Download)

    # Espera a que se descargue la imagen
    time.sleep(3)

    # Comprueba si la imagen está en a ruta de descarga
    assert os.path.exists(ruta_carpeta_descarga)
