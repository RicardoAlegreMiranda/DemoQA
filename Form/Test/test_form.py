from datetime import datetime
import os
import time

from selenium.webdriver import ActionChains, Keys
from selenium import webdriver
from selenium.webdriver.support.ui import Select

from Form.Paths import path_form
from Funcions import funcions, funcitions_excel, dateTime


#################################################################
############### <<Carga la configuración previa>> ###############
#################################################################

# Inicia las variables Globales necesarias para que sean accesibles
ruta = path_form  # Método para obtener los XPATH del formulario Web (llamado TextBox)
driver = None
funciones = None
lista_datos = None
lista_elementos = None
actions = None
lista_devuelta = []

# Obtener los datos de prueba del documento Excel
hojaExcel = ruta.Excel.HojaCorreo  # Obtener la hoja del Excel donde están los datos a utilizar
funciones_excel = funcitions_excel.FuncionesExcel(hojaExcel)


# Esta es la configuración global para las pruebas (abre el driver y se lo envía mis funciones para iniciarlas)
def setup_function():
    global driver, funciones, lista_datos, lista_elementos, actions

    lista_datos = []
    lista_elementos = []
    lista_elementos = ruta.form.Lista_Elementos

    # Inicia el Driver y las funciones Globales
    driver = webdriver.Chrome()  # Driver Chrome
    funciones = funcions.Global_Funcions(driver)
    actions = ActionChains(driver)

    # Obtiene los datos del excel y los guarda en una lista (tienen que venir 12 datos desde el excel)
    for n in range(1, 12):
        dato = funciones_excel.leer_celda(2, n)
        lista_datos.append(dato)

    # Abre el navegador
    funciones.getURL(ruta.form.URL)


# Esta es la función que da cierre a cada prueba
def teardown_function():
    print("Fin de la prueba")
    driver.close()


#################################################################
##### <<AQUÍ EMPIEZAN LAS PRUEBAS PARA EL FORMULARIO WEB>> ######
#################################################################

# Esta prueba se importan los datos del Excel y se rellena el formulario, se validan los datos y se hace screenshot
def test_Formulario():

    # Escribe el Nombre Apellido, Correo, Teléfono y Dirección
    for n in range(0, 5):
        funciones.writeXP(lista_elementos[n], lista_datos[n])

    # Obtiene el género y lo selecciona en la web
    funciones.Click(ruta.obtenerGenero(lista_datos[7]))

    # Pulsa sobre el Calendario y lo despliega
    funciones.Click(ruta.form.datepicker)

    # Llama al método que escribe en el DatePicker la fecha de prueba (Obtenida del Excel)
    selecionarFechaCalendario()

    # Llama la método que revuelve el Listado de Asignaturas
    asignaturas = ruta.separar_palabras(lista_datos[9])

    # Escribe las asignaturas en el autocompletar y pulsar ENTER
    funciones.Click(ruta.form.asignaturas)
    for asignatura in asignaturas:
        actions.send_keys(asignatura)
        actions.perform()
        time.sleep(0.1)
        actions.send_keys(Keys.ENTER)
        actions.perform()

    # Obtiene el listado y hace Click en los hobbies
    for hobbie in obtenerHobbies(lista_datos[10]):
        funciones.Click(hobbie)

    # Sube la imagen JPG

    funciones.writeXP(ruta.form.btn_uplodad, ruta.ruta_relativa())
    # Escribe el estado
    funciones.Click(ruta.form.estado)
    actions.send_keys(lista_datos[5] + Keys.ENTER)
    actions.perform()

    # Escribe la ciudad
    funciones.Click(ruta.form.ciudad)
    actions.send_keys(lista_datos[6] + Keys.ENTER)
    actions.perform()

    # Ejecuta una función JavaScript para cambiar el nivel de zoom de la página y espera
    driver.execute_script("document.body.style.zoom = '{}';".format(0.7))
    funciones.wait_zoom(ruta.form.zoom)

    # Pulsa tab + Enter (si intentamos pulsar en Submit directamente da error)
    actions.send_keys(Keys.TAB + Keys.ENTER)
    actions.perform()

    # Esperar a que el modal esté presente
    funciones.wait_zoom(ruta.form.tabla_modal)

    # Compara los datos encontrados dentro del Modal con los datos Esperados
    datos_modal = funciones.getText(ruta.form.tabla_modal)
    for date in lista_datos:

        assert str(date) in datos_modal
    # Hace una captura de pantalla
    funciones.capturar(dateTime.obtener_fecha_hora_actual())

    # Cierra el modal, si no se puede hacer click, hace tab + enter
    try:
        funciones.Click(ruta.form.closed_modal)
    except:
        actions.send_keys(Keys.TAB + Keys.ENTER)
        actions.perform()


#################################################################
##### <<FIN DE LAS PRUEBAS //////// EMPIEZAN LOS MÉTODOS> #######
#################################################################


# Este método sirve para obtener la fecha del Excel, modificarla a un formato compatible con el datepicker de la Web y
# después pulsar sobre la fecha correcta, llamado a esta función se ahorran todos estos pasos y se marca
# la fecha correcta
def selecionarFechaCalendario():
    # Almaceno la fecha en una variable String
    fecha_str = str(lista_datos[8])

    # Convertir la cadena de texto String de fecha en objeto datetime
    fecha_objeto = datetime.strptime(fecha_str, '%Y-%m-%d %H:%M:%S')

    # Uso el objeto datetime con la propiedad Select para seleccionar el Mes que viene
    SelectMes = funciones.searchXP(ruta.form.mes)
    SelectorMes = Select(SelectMes)
    SelectorMes.select_by_visible_text(ruta.obtenerMes(fecha_objeto.month))

    # Selecciono el año del desplegable
    SelectAno = funciones.searchXP(ruta.form.ano)
    SelectorAno = Select(SelectAno)
    SelectorAno.select_by_visible_text(str(fecha_objeto.year))

    # Cambio el formato de la fecha en el listado, para que tenga el mismo formato que en la web, para que después
    # se puedan comparar
    lista_datos[8] = str(fecha_objeto.day) + " " + ruta.obtenerMes(fecha_objeto.month) + "," + str(fecha_objeto.year)

    # hace Click en el día y Cierra el datePicker
    funciones.Click(ruta.obtenerDía(fecha_objeto.day))


# Obtiene los hobbies y devuelve los XPATH en una lista
def obtenerHobbies(hobbies):
    lista_hobbies = []

    if "Music" in hobbies:
        lista_hobbies.append(ruta.form.musica)
        lista_elementos.append("Music")

    if "Sports" in hobbies:
        lista_hobbies.append(ruta.form.deportes)
        lista_elementos.append("Sports")
    if "Read" in hobbies:
        lista_hobbies.append(ruta.form.lectura)
        lista_elementos.append("Reading")

    # Borra los hobbies de la posición 10 de la lista, para añadirlos de manera individual y que se puedan comparar
    # correctamente durante la validación. Los hobbies se han añadido en la lista de manera individual en el
    # método obtenerHobbies(), por lo cual ya se puede borrar esta posición del listado
    del lista_datos[10]

    return lista_hobbies
