from Funcions import funcions
class CheckBox:
    URL = "https://demoqa.com/checkbox"
    word = "//span[@class='rct-title'][contains(.,'Word File.doc')]"
    desktop = "//span[@class='rct-title'][contains(.,'Desktop')]"
    angular = "//span[@class='rct-title'][contains(.,'Angular')]"
    general = "//span[@class='rct-title'][contains(.,'General')]"
    desplegale = "//*[@id='tree-node']/ol/li/span/button"
    despliegaDocuments = "//*[@id='tree-node']/ol/li/ol/li[2]/span/button"
    despliegaDownload = "//*[@id='tree-node']/ol/li/ol/li[3]/span/button"
    despliegaOffice = "//*[@id='tree-node']/ol/li/ol/li[2]/ol/li[2]/span/button"
    despliegaWorkSpace = "//*[@id='tree-node']/ol/li/ol/li[2]/ol/li[1]/span/button"
    result = "//*[@id='result']"
    text_success = "'.text-success'"
    text_expected = ["desktop", "notes", "commands", "angular", "general", "wordFile"]
    span_result = "//*[@id='result']/span[2]"
    Desplegar = [desplegale, despliegaDocuments, despliegaWorkSpace, despliegaOffice, despliegaDownload]
    Seleccionar = [word, desktop, angular, general]

    # Este método sirve para ver los datos que se muestran en pantalla
def dato_obtenido(numero, driver):
    funciones = funcions.Global_Funcions(driver)
    dato = funciones.searchXP("//*[@id='result']/span[" + str(numero) + "]").text
    return dato

