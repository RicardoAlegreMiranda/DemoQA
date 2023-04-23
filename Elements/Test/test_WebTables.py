from selenium import webdriver

import Elements.Paths.paths_WebTables
from Elements.Paths.paths_WebTables import borrar_tabla, modificar_tabla, Excel
from Funcions import funcions, funcitions_excel, dateTime

#################################################################
############### <<Carga la configuración previa>> ###############
#################################################################

# Instancia los objetos necesarios
ruta = Elements.Paths.paths_WebTables.WebTables
driver = None
funciones = None


# Obtener los datos de prueba del documento Excel
hojaExcelCorreo = Excel.HojaCorreo  # Obtener la hoja del Excel donde están los datos a utilizar

# Crear una lista vacía para almacenar los datos obtenidos
datos_obtenidos = []

# Carga los métodos para acceder los datos de prueba alojados en el documento Excel
funciones_excel = funcitions_excel.FuncionesExcel(hojaExcelCorreo)
filas = funciones_excel.obtener_num_filas()  # El número de filas que tiene el documento Excel
columnas = funciones_excel.obtener_num_columnas()  # El número de columnas del documento


# Esta es la configuración global para las pruebas (abre el driver y se lo envía mis funciones para iniciarlas)
def setup_function():
    global driver, funciones
    driver = webdriver.Chrome()  # Driver Chrome
    funciones = funcions.Global_Funcions(driver)  # Funciones

    # Abre en navegador
    funciones.getURL(ruta.URL)
# Esta es la función que da cierre a cada prueba
def teardown_function():
    print("Fin de la prueba")
    driver.close()


#################################################################
######## <<AQUÍ EMPIEZAN LAS PRUEBAS PARA LA TABLA WEB>> ########
#################################################################

# Esta prueba consiste en añadir nuevas columnas de datos en la Web Table, los datos serán pre-cargados desde una hoja
# de Excel, y después de escribir todos los datos, válida que los datos de pruebas están presentes en la Web
def test_nuevaFila():

    # Se abre un bucle para rellenar el WebTable con los datos obtenidos del Excel
    for fila in range(2, filas + 1):

        # Pulsa en Add (Añadir un nuevo usuario)
        funciones.Click(ruta.add)

        # Aquí se Busca el dato en el Excel y se Escribe el campo que corresponde de este formulario Web
        for columna in range(1, columnas + 1):
            # Busca el dato en el Excel (fila y columna) y lo escribe en el formulario
            funciones.writeXP(ruta.ListaXPATH[columna - 1], funciones_excel.leer_celda(fila, columna))

            # Guarda el dato obtenido en una lista para después poder validar contra los datos de la WEB
            datos_obtenidos.append(funciones_excel.leer_celda(fila, columna))

        # Hace <<Click>> en Submit (Se envía el formulario)
        funciones.Click(ruta.Submit)

    # Este método obtiene todos los elementos de la tabla de datos Web
    datosTabla = funciones.buscarElementosNombreClase(ruta.tabla, 'rt-td')

    # Añade todos los datos que no estén vacío a la lista "real_dato"
    real_dato = []
    for dato in datosTabla:
        if len(dato.text) > 1:
            real_dato.append(dato.text)
            real_dato.append(dato.text)

    # Pasa todos los datos obtenidos a tipo String (para evitar errores en la validación)
    datos_obtenidos_sin_integer = [str(item) for item in datos_obtenidos]

    # Válida que los todos datos obtenidos en el Excel están presenten en los datos obtenidos de la Web
    for dat in datos_obtenidos_sin_integer:
        assert dat in real_dato

    # Hace una captura de pantalla
    funciones.capturar(dateTime.obtener_fecha_hora_actual())

# Este test consiste en validar que se borran los datos al pulsar en la papelera
def test_borrarDatos():

    # Este método obtiene todos los elementos de la tabla de datos Web
    datosTabla = funciones.buscarElementosNombreClase(ruta.tabla, 'rt-td')

    # Añade todos los datos que no estén vacíos en la lista
    AntesDeBorrar = []
    for dato in datosTabla:
        if len(dato.text) > 1:
            AntesDeBorrar.append(dato.text)

    # Pulsa la tecla borrar en el primer puesto (Se puede modificar el número por cualquier número de fila)
    funciones.Click(borrar_tabla(2))

    # Vuelve a obtener los datos de la Web después de borrar la primera columna de la tabla
    datosTablaBorrados = funciones.buscarElementosNombreClase(ruta.tabla, 'rt-td')

    # Añade todos los datos que no estén vacíos en la lista
    Borrado = []
    for dato in datosTablaBorrados:
        if len(dato.text) > 1:
            Borrado.append(dato.text)

    # Se valida que después de borrar 1 fila, tenemos 6 datos menos
    assert len(AntesDeBorrar) - 6 == len(Borrado)

    # Hace una captura de pantalla
    funciones.capturar(dateTime.obtener_fecha_hora_actual())

# Esta prueba consiste en modificar los datos ya existentes en una columna e introducir nuevos datos en su lugar
def test_modificar():

    # Click en modificar (se puede cambiar la fila que se quiere modificar cambiando el número)
    funciones.Click(modificar_tabla(2))

    # Aquí se editan los datos que del usuario que vamos a modificar
    n = 0
    for dato in ruta.ListaDatosModifica:

        # Primero borra los datos encontrados
        funciones.Limpiar(ruta.ListaXPATH[n])
        # Escribe nuevos datos en el formulario
        funciones.writeXP(ruta.ListaXPATH[n], dato)
        n += 1
    # Click en submit para guardar los cambios
    funciones.Click(ruta.Submit)

    # Este método obtiene todos los elementos de la tabla de datos Web
    datosTabla = funciones.buscarElementosNombreClase(ruta.tabla, 'rt-td')

    # Añade todos los datos que no estén vacíos en la lista para compararlos
    ListaDatos = []
    for dato in datosTabla:
        if len(dato.text) > 1:
            ListaDatos.append(dato.text)

    # Válida que los todos datos obtenidos de prueba están presenten en los datos obtenidos de la Web
    for dat in ruta.ListaDatosModifica:
        assert dat in ListaDatos

    # Hace una captura de pantalla
    funciones.capturar(dateTime.obtener_fecha_hora_actual())
