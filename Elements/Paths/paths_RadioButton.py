from Funcions import funcions

# Variable global
No = "//*[@id='noRadio']"


# Esta función habilita el botón para que pueda ser pulsado
def habilitar_btn_no(driver):
    # Encontrar el botón
    funciones = funcions.Global_Funcions(driver)
    btn_no = funciones.searchXP(No)

    # Ejecutar un script de JavaScript para habilitar el elemento de radio botón No
    driver.execute_script("arguments[0].removeAttribute('disabled');", btn_no)

    # Verificar si el atributo 'disabled' ha sido eliminado correctamente
    if btn_no.get_attribute('disabled'):
        print("El atributo 'disabled' no ha sido eliminado correctamente.")
    else:
        print("El atributo 'disabled' ha sido eliminado exitosamente.")


class radio:
    URL = "https://demoqa.com/radio-button"
    Yes = "//label[@class='custom-control-label'][contains(.,'Yes')]"
    Impressive = "//label[@class='custom-control-label'][contains(.,'Impressive')]"
    Noes = "//label[@class='custom-control-label disabled'][contains(.,'No')]"
    result = "//*[@id='app']/div/div/div[2]/div[2]/div[2]/p/span"
    resultadoEsperadoYes = "Yes"
    resuttadoEsparadoImpressive = "Impressive"
