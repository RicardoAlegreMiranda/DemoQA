import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Widgets.Paths import paths_tools_tips
from Funcions import funcions

def obtener_texto_elemento(driver, elemento):

    # Mueve el ratón sobre el elemento
    action = ActionChains(driver)
    action.move_to_element(elemento).perform()

    # Encuentra el elemento
    time.sleep(0.3)
    tooltip_locator = (By.CLASS_NAME, "tooltip-inner")
    tooltip = WebDriverWait(driver, 5).until(EC.visibility_of_element_located(tooltip_locator))
    action.reset_actions()

    # Devuelve el texto sobre el elemento
    return tooltip.text


