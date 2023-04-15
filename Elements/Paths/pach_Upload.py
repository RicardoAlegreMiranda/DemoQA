
class upload:

    URL = "https://demoqa.com/upload-download"
    Download = "//a[@id='downloadButton']"
    Upload = "//input[contains(@id,'uploadFile')]"
    Confirma_Subida = "//p[contains(@id,'uploadedFilePath')]"

    # Este método sirve para modificar la ruta actual y convertirla en la ruta relativa necesaria
    def ruta_relativa(texto):
        partes = texto.split("//")  # Dividir el texto en partes utilizando "//" como delimitador
        nueva_cadena = "//".join(partes[:-1])  # Unir las partes excepto la última
        nueva_cadena += "//"  # Agregar de nuevo el último "//" al final
        return nueva_cadena + "Files//tester.jpg"
