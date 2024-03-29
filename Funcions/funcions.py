import time

import allure
from allure_commons.types import AttachmentType
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

t = 0.2

class Global_Funcions:

    def __init__(self, driver):
        self.driver = driver

    # Abre el navegador en la ruta indicada y lo maximiza
    def getURL(self, url):
        try:
            self.driver.get(url)
            self.driver.implicitly_wait(5)
            self.driver.maximize_window()
            print("\nPágina abierta :" + str(url))
        except Exception as e:
            print("No se pudo abrir la página: " + url)
            print(f"Detalles del error: {str(e)}")

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
        except Exception as e:
            print("No se ha encontrado elemento XPATH: " + XPATH + "\n")
            print(f"Detalles del error: {str(e)}")
            return False

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
        except Exception as e:
            print("No se ha encontrado elemento ID: " + ID + "\n")
            print(f"Detalles del error: {str(e)}")

    # Busca un elemento por tag_name
    def search_tag_name(self, tag):
        try:
            elemento = self.driver.find_elements(by=By.TAG_NAME, value=tag)
            return elemento
        except Exception as e:
            print("No se encontró ningún elemento con tag name: ", tag)
            print(f"Detalles del error: {str(e)}")

    # Busca un elemento por CSS Selector
    def search_css_selector(self, CSS):
        try:
            elemento_css_selector = self.driver.find_elements(by=By.CSS_SELECTOR, value=CSS)
            return elemento_css_selector
        except Exception as e:
            print("No se encontró ningún elemento con CSS_Selector: ", CSS)
            print(f"Detalles del error: {str(e)}")

    # Busca un atributo CSS de un elemento
    def search_css_property(self, XPATH, CSS_Attribute):
        try:
            elemento = self.searchXP(XPATH)
            attribute = elemento.value_of_css_property(CSS_Attribute)
            print("Atributo encontrado: ", attribute)
            return attribute
        except Exception as e:
            print("No se ha encontrado el atributo CSS", CSS_Atributte)
            print(f"Detalles del error: {str(e)}")

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
        except Exception as e:
            print("No se ha podido escribir en elemento XPATH " + XPATH + " el texto " + str(Texto) + "\n")
            print(f"Detalles del error: {str(e)}")

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
        except Exception as e:
            # Intenta hacer clic por ID en lugar de XPATH
            print("No se pudo hacer Clic_by_xpath: " + XPATH + "\n")
            print(f"Detalles del error: {str(e)}")
            self.click_script(XPATH)  # Si falla el método principal intenta hacer click de manera alternativa

    # Método para hacer click por Script si falla el método principal
    def click_script(self, xpath):
        try:
            # Este es el método alternativo para hacer clic
            element = self.driver.find_element(by=By.XPATH, value=xpath)
            self.driver.execute_script("arguments[0].click();", element)
            print("Click_script: " + xpath)
        except Exception as e:
            print("No se pudo hacer click por script: " + xpath)
            print(f"Detalles del error: {str(e)}")

    # Este método permite borrar los datos de un campo
    def Limpiar(self, XPATH):
        try:
            self.driver.find_element(by=By.XPATH, value=XPATH).clear()
        except Exception as e:
            print("No se pudo borrar los datos del elemento " + XPATH)
            print(f"Detalles del error: {str(e)}")

    # Este método permite hacer captura de pantalla de la pantalla actual
    def capturar(self, Nombre):
        try:
            allure.attach(self.driver.get_screenshot_as_png(), name=Nombre, attachment_type=AttachmentType.PNG)
            print("Realizada captura de pantalla " + Nombre)
        except Exception as e:
            print("No se pudo realizar la captura de pantalla")
            print(f"Detalles del error: {str(e)}")

    # Devuelve el atributo Clase de un elemento WEB
    def clase(self, XPATH):
        try:
            clase = self.driver.find_element(by=By.XPATH, value=XPATH).get_attribute('class')
            return clase
        except Exception as e:
            print("No se ha encontrado el atributo clase en: ", XPATH)
            print(f"Detalles del error: {str(e)}")

    # Este método devuelve el texto de una clase
    def getText(self, XPATH):
        # Espera a cargar elemento
        try:
            wait = WebDriverWait(self.driver, 5)
            wait.until(EC.presence_of_element_located((By.XPATH, XPATH)))

            # Encuentra el elemento, obtiene el texto y lo devuelve
            texto = self.driver.find_element(by=By.XPATH, value=XPATH).text
            return texto
        except Exception as e:
            print("No se pudo obtener el texto en ", XPATH)
            print(f"Detalles del error: {str(e)}")
            # Intenta conseguir el texto por JavaScript
            self.get_text_java_script(XPATH)

    # Usando JavaScript para obtener el texto del elemento
    def get_text_java_script(self, XPATH):
        try:
            element = self.driver.find_element(by=By.XPATH, value=XPATH)
            element_text = self.driver.execute_script("return arguments[0].textContent", element)
            print("Texto encontrado con JS en:", XPATH)
            return element_text
        except Exception as e:
            print("No se pudo obtener el texto por JS ", XPATH)
            print(f"Detalles del error: {str(e)}")

    # Este método busca los elementos de una clase por su nombre
    def buscarElementosNombreClase(self, XPATH, VALUE):
        try:
            elemento = self.searchXP(XPATH)
            lista_elementos = elemento.find_elements(by=By.CLASS_NAME, value=VALUE)
            return lista_elementos
        except Exception as e:
            print("No se han encontrado los nombres de clase ", VALUE)
            print(f"Detalles del error: {str(e)}")

    # Este método sirve para localizar los links de una Web
    def enlaces(self):
        try:
            enlaces = self.driver.find_elements(by=By.TAG_NAME, value="a")
            return enlaces
        except Exception as e:
            print("No se encuentran enlaces")
            print(f"Detalles del error: {str(e)}")

    # Este método cambia el Zoom de la página actual a 0.7 para que todos los elementos sean visibles
    def cambia_zoom(self, zoom):
        try:
            self.driver.execute_script("document.body.style.zoom = '{}';".format(zoom))
            wait = WebDriverWait(self.driver, 5)
            wait.until(EC.presence_of_element_located((By.XPATH, "//*[contains(@style, 'zoom: "+str(zoom)+"')]")))
            print("Se ha cambiado el zoom a ", zoom)
        except Exception as e:
            print("No se ha cambiado el zoom a ", zoom)
            print(f"Detalles del error: {str(e)}")
    # Busca elementos por nombre de clase

    def search_elements_by_class_name(self, ClassName):
        try:
            elemento = self.driver.find_elements(by=By.CLASS_NAME, value=ClassName)
            print(str(len(elemento)) + " elementos encontrados con nombre clase " + ClassName)
            return elemento
        except Exception as e:
            print("No se han encontrado elementos por nombre de clase: ", ClassName)
            print(f"Detalles del error: {str(e)}")

    # Pulsa enter
    def key_enter(self, XPATH):
        self.searchXP(XPATH).send_keys(Keys.ENTER)

    # Obtén el valor de un atributo concreto
    def get_attribute(self, xpath, value):
        try:
            elemento = self.searchXP(xpath)
            valor = elemento.get_attribute(value)
            print("Atributo encontrado: ", valor)
            return valor
        except Exception as e:
            print("No se ha encontrado el atributo "+value+" en el xpath "+xpath)
            print(f"Detalles del error: {str(e)}")

    # Mueve el ratón encima de un elemento
    def move_mouse_to_element(self, XPATH):
        try:
            # Busca el elemento por XPATH
            elemento = self.searchXP(XPATH)

            # Mueve el ratón sobre el elemento
            action = ActionChains(self.driver)

            # Mueve el ratón al lugar esperado
            action.move_to_element(elemento).perform()
            print("Se ha movido el ratón al elemento ", XPATH)
        except Exception as e:
            print("No se ha podido mover el ratón encima de ", XPATH)
            print(f"Detalles del error: {str(e)}")
