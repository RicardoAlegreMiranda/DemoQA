import time

import allure
from allure_commons.types import AttachmentType
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

t = 0.3


class Global_Funcions:

    def __init__(self, driver):
        self.driver = driver

    # Abre el navegador en la ruta indicada y lo maximiza
    def getURL(self, url):
        try:
            self.driver.get(url)
            self.driver.maximize_window()
            print("\nPágina abierta :" + str(url))
            time.sleep(t)
        except:
            print("No se pudo abrir la página: " + url)

    # Busca un elementoWeb por Xpath
    def searchXP(self, XPATH):
        try:
            # Espera a cargar elemento
            wait = WebDriverWait(self.driver, 5)
            wait.until(EC.presence_of_element_located((By.XPATH, XPATH)))
            elemento = self.driver.find_element(by=By.XPATH, value=XPATH)
            print("Encontrado XPATH " + XPATH + "\n")
            time.sleep(t)
            return elemento
        except:
            print("No se ha encontrado elemento XPATH: " + XPATH + "\n")

    # Busca un elemento por ID
    def searchID(self, ID):
        try:
            # Espera a cargar elemento
            wait = WebDriverWait(self.driver, 5)
            wait.until(EC.presence_of_element_located((By.XPATH, ID)))
            elemento = self.driver.find_element(by=By.XPATH, value=ID)
            print("Encontrado ID " + ID + "\n")
            time.sleep(t)
            return elemento
        except:
            print("No se ha encontrado elemento ID: " + ID + "\n")

    # Escribe en un elemento WEB
    def writeXP(self, XPATH, Texto):
        try:
            # Espera a cargar elemento
            wait = WebDriverWait(self.driver, 5)
            wait.until(EC.presence_of_element_located((By.XPATH, XPATH)))
            # Busca Elemento lo guarda en variable elemento y escribe en él
            elemento = self.driver.find_element(by=By.XPATH, value=XPATH)
            elemento.send_keys(Texto)

            # Aviso de que se mandó correctamente
            print("Escrito: " + Texto + " En XPATH " + XPATH + "\n")
            time.sleep(t)
        except:
            print("No se ha podido escribir en elemento XPATH " + XPATH + " el texto " + str(Texto) + "\n")

    # Hace click en un elemento
    def Click(self, XPATH):
        try:

            # Espera a cargar elemento
            wait = WebDriverWait(self.driver, 5)
            wait.until(EC.presence_of_element_located((By.XPATH, XPATH)))

            # Busca Elemento
            elemento = self.driver.find_element(by=By.XPATH, value=XPATH)

            # Clic en el Elemento
            elemento.click()

            # Aviso de que se hace clic
            print("Clic: " + XPATH + "\n")
            time.sleep(t)
        except:
            # Intenta hacer clic por ID en lugar de XPATH
            click_by_id(self.driver, XPATH)
            print("No se pudo hacer Clic_by_xpath: " + XPATH + "\n")

    # Hace click en un elemento por ID
    def click_by_id(self, ID):
        try:

            # Espera a cargar elemento
            wait = WebDriverWait(self.driver, 5)
            wait.until(EC.presence_of_element_located((By.ID, ID)))

            # Busca Elemento
            elemento = self.driver.find_element(by=By.ID, value=ID)

            # Clic en el Elemento
            elemento.click()

            # Aviso de que se hace clic
            print("Clic_by_id: " + ID + "\n")
            time.sleep(t)
        except:
            print("No se pudo hacer Clic_by_id: " + XPATH + "\n")

    # Este método permite borrar los datos de un campo
    def Limpiar(self, XPATH):
        try:
            self.driver.find_element(by=By.XPATH, value=XPATH).clear()
        except:
            print("No se pudo borrar los datos del elemento " + XPATH)

    # Este método permite hacer captura de pantalla de la pantalla actual
    def capturar(self, Nombre):
        try:
            allure.attach(self.driver.get_screenshot_as_png(), name=Nombre, attachment_type=AttachmentType.PNG)
            print("Realizada captura de pantalla " + Nombre)
        except:
            print("No se pudo realizar la captura de pantalla")

    # Devuelve el atributo Clase de un elemento WEB
    def clase(self, XPATH):
        clase = self.driver.find_element(by=By.XPATH, value=XPATH).get_attribute('class')
        return clase

    # Este método devuelve el texto de una clase
    def getText(self, XPATH):
        texto = self.driver.find_element(by=By.XPATH, value=XPATH).text
        return texto

    # Este método busca los elementos de una clase por su nombre
    def buscarElementosNombreClase(self, XPATH, VALUE):
        valor = self.searchXP(XPATH)
        datos_tabla = valor.find_elements(by=By.CLASS_NAME, value=VALUE)
        return datos_tabla

    # Este método sirve para localizar los links de una Web
    def enlaces(self):
        try:
            enlaces = self.driver.find_elements(by=By.TAG_NAME, value="a")
            return enlaces
        except:
            print("No se encuentran enlaces")

    def wait_zoom(self, xpath):
        wait = WebDriverWait(self.driver, 5)  # Configura un WebDriverWait con un tiempo de espera máximo de 10 segundos
        wait.until(EC.presence_of_element_located((By.XPATH, xpath)))
