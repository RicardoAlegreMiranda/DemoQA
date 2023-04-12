import os
import time
from Funcions import funcions, dateTime
from Elements.Paths import pach_Upload
from selenium import webdriver

#################################################################
############### <<Carga la configuración previa>> ###############
#################################################################

# Instancia los objetos necesarios
ruta = pach_Upload.upload # Método para obtener los XPATH del formulario Web (llamado TextBox)
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

# Esta prueba válida que la imagen se sube de manera correcta
def test_carga_imagen():

    # Abre el navegador
    funciones.getURL(ruta.URL)

    # Sube la imagen (Uso la función de escritura por qué es la misma) en lugar de un texto por parámetro le envío
    # la dirección del archivo JPG
    funciones.writeXP(ruta.Upload, ruta.ruta_archivo)

    # Lee el mensaje de subida
    Texto_Subida = funciones.getText(ruta.Confirma_Subida)

    # Se valida que el nombre del archivo (tester.jpg) aparece en como subido en la Web
    assert "tester.jpg" in Texto_Subida

    # Hace una captura de pantalla
    funciones.capturar(dateTime.obtener_fecha_hora_actual())

# Esta prueba válida que se descarga la imagen de manera correcta
def test_Descarga():
    # Abre el navegador
    funciones.getURL(ruta.URL)

    # Pulsa en Download para descargar la imagen
    funciones.Click(ruta.Download)

    # Espera a que se descargue la imagen
    time.sleep(3)

    # Comprueba si la imagen está en a ruta de descarga
    assert os.path.exists(ruta.ruta_descarga_PC)
