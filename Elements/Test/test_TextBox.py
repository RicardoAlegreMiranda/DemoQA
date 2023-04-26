import allure
from Funcions import funcions, funcitions_excel, dateTime
from Elements.Paths import paths_TextBox
from selenium import webdriver
from selenium.webdriver.common.by import By

#################################################################
############### <<Carga la configuración previa>> ###############
#################################################################

# Instancia los objetos necesarios
ruta = paths_TextBox.TextBox  # Método para obtener los XPATH del formulario Web (llamado TextBox)
driver = None
funciones = None

# Obtener los datos de prueba del documento Excel
hojaExcelOK = paths_TextBox.Excel.HojaTextBoxOK  # Obtener la hoja del Excel donde están los datos a utilizar
hojaExcelCorreo = paths_TextBox.Excel.HojaCorreo  # Obtener la hoja del Excel donde están los datos a utilizar
listaXpath = [ruta.Name, ruta.Email, ruta.CAddress, ruta.PAdress]  # Lista con los Xpath a probar

# Crear una lista vacía para almacenar los datos obtenidos
datos_obtenidos = []

# Esta es la configuración global para las pruebas (abre el driver y se lo envía mis funciones para iniciarlas)
def setup_function():
    global driver, funciones
    driver = webdriver.Chrome()  # Driver Chrome
    funciones = funcions.Global_Funcions(driver)  # Funciones

    # Se abre el navegador con la URL indicada
    funciones.getURL(ruta.Url)

    funciones.cambia_zoom()  # Cambia el zoom a 0.7

# Esta es la función que da cierre a cada prueba
def teardown_function():
    print("Fin de la prueba")
    driver.close()

#################################################################
##### <<AQUÍ EMPIEZAN LAS PRUEBAS PARA EL FORMULARIO WEB>> ######
#################################################################

@allure.severity(allure.severity_level.CRITICAL)
@allure.description("""Esta prueba consiste en validar los campos Nombre, Correo, Dirección, al escribirlos en la web y 
pulsar el submit, deben aparecer escritos los datos abajo""")
def test_Datos_FormularioWeb():
    # Carga los métodos para acceder los datos de prueba alojados en el documento Excel
    funciones_excel = funcitions_excel.FuncionesExcel(hojaExcelOK)
    filas = funciones_excel.obtener_num_filas()  # El número de filas que tiene el documento Excel
    columnas = funciones_excel.obtener_num_columnas()  # El número de columnas del documento

    # Se abre un bucle para ejecutar la prueba (Busca el dato en el excel, lo escribe en la web y lo válida)
    for fila in range(2, filas + 1):

        # Aquí se Busca el dato en el Excel y se Escribe el campo que corresponde de este formulario Web
        for columna in range(1, columnas + 1):
            # Busca el dato en el Excel (fila y columna) y lo escribe en el formulario
            funciones.writeXP(ruta.ListaDatos[columna], funciones_excel.leer_celda(fila, columna))

            # Guarda el dato obtenido en una lista para después poder validar contra los datos de la WEB
            datos_obtenidos.append(funciones_excel.leer_celda(fila, columna))

        # Hace <<Click>> en Submit (Se envía el formulario)
        funciones.Click(ruta.Submit)

        # Realiza una captura de pantalla y le pone la fecha actual como nombre de la captura
        funciones.capturar(dateTime.obtener_fecha_hora_actual())

        # Aquí se valida que el formulario llega bien a destino (los datos deben ser leídos en pantalla)
        for rutaDato in ruta.ListaDatosFinales:
            # Validar que los datos el excel son los mismos que devuelve el Front (la web)
            assert datos_obtenidos[0] in funciones.searchXP(rutaDato).text

            # Borra el dato que acaba de validar del listado, de este modo siempre se valida la posición 0 del listado y
            # al terminar el ciclo, dicho listado queda vacío a la espera de la siguiente prueba
            datos_obtenidos.remove(datos_obtenidos[0])

        # Se borran los datos del formulario para repetir la prueba con otros datos
        for xpath in listaXpath:
            funciones.Limpiar(xpath)  # borra los datos de la lista

    # Cierra el documento Excel con los datos
    funciones_excel.cerrar_excel()


@allure.severity(allure.severity_level.CRITICAL)
@allure.description("""Esta prueba consiste en validar que NO permite introducir un correo con formato invalido""")
def test_Correo_Invalido():
    # Carga los datos necesarios para la prueba
    funciones_excel = funcitions_excel.FuncionesExcel(hojaExcelCorreo)
    filas = funciones_excel.obtener_num_filas()  # El número de filas que tiene el documento Excel
    columnas = funciones_excel.obtener_num_columnas()  # El número de columnas del documento

    # Se abre un bucle para ejecutar la prueba (Busca el dato en el excel, lo escribe en la web y lo válida)
    for fila in range(2, filas + 1):

        # Aquí se Busca el dato en el Excel y se Escribe el campo que corresponde de este formulario Web
        for columna in range(1, columnas + 1):
            # Busca el dato en el Excel (fila y columna) y lo escribe en el formulario
            funciones.writeXP(ruta.ListaDatos[columna], funciones_excel.leer_celda(fila, columna))

        # Hace <<Click>> en Submit (Se envía el formulario)
        funciones.Click(ruta.Submit)

        # Validar que la Clase cambia al dar el error en Color Rojo en la web (ocurre cuando cambia el nombre
        # de la Clase del Email y dicho cambio es lo que validamos)
        assert funciones.clase(ruta.Email) == ruta.EmailClassError

        # Hace una captura de pantalla
        funciones.capturar(dateTime.obtener_fecha_hora_actual())

        # Se borran los datos del formulario para repetir la prueba con otros datos
        for xpath in listaXpath:
            funciones.Limpiar(xpath)  # borra los datos de la lista
