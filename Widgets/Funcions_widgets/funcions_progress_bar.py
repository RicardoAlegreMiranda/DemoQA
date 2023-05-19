from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from Funcions import funcions
from Funcions.dateTime import obtener_fecha_hora_actual

# Este método recibe el driver y el porcentaje esperado para el progress bar
def start_stop(driver, porcentaje):

    # Inicia las variables globales
    funciones = funcions.Global_Funcions(driver)

    # Pulsar en Start para iniciar el progress bar
    funciones.Click("//button[contains(@id,'startStopButton')]")

    # Inicia el progress bar
    progress_bar = WebDriverWait(driver, 15).until(
        EC.visibility_of_element_located((By.XPATH, "//*[@id='progressBar']/div"))
    )
    # Espera a que el progress bar tenga el porcentaje esperado
    WebDriverWait(driver, 15).until(
        lambda driver: int(progress_bar.get_attribute("aria-valuenow")) >= porcentaje

    )

    valor_progress_bar = int(progress_bar.get_attribute("aria-valuenow"))
    # Pulsar Reset / Start según sea lo indicado
    if valor_progress_bar == 100:
        # Capturar de pantalla con fecha actual
        funciones.capturar(obtener_fecha_hora_actual())

        # Obtiene el valor del progress bar
        valor_progress_bar = progress_bar.get_attribute("aria-valuenow")

        # Pulsa Reset
        funciones.Click("//button[contains(@id,'resetButton')]")

    else:
        # Capturar de pantalla con fecha actual
        funciones.capturar(obtener_fecha_hora_actual())

        # Obtiene el valor del progress bar
        valor_progress_bar = progress_bar.get_attribute("aria-valuenow")

        # Pulsa en Start
        funciones.Click("//button[contains(@id,'startStopButton')]")

    # Devuelve el valor actual del progress bar
    return int(valor_progress_bar)
