from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

class FuncionsBrowser:
    def __init__(self, driver):
        self.driver = driver

    # Esté método permite esperar a que se cargue la nueva ventana o pestaña
    def espera_cargar_ventana(self):
        WebDriverWait(self.driver, 10).until(EC.number_of_windows_to_be(2))
        ventana_actual = self.driver.window_handles[0]
        nueva_ventana = self.driver.window_handles[1]
        self.driver.switch_to.window(nueva_ventana)
        print(nueva_ventana)
        return ventana_actual

    def cambia_ventana(self, ventana):
        self.driver.switch_to.window(ventana)
        print("Cambiado a ventana", ventana)

    def espera(self):
        WebDriverWait(self.driver, 10).until(EC.number_of_windows_to_be(2))
