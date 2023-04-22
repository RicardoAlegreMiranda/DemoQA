from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

class FuncionsAlerts:
    def __init__(self, driver):
        self.driver = driver

    # Esté método devuelve el alert
    def obtener_alerta(self):
        alert = WebDriverWait(self.driver, 10).until(EC.alert_is_present())
        return alert

