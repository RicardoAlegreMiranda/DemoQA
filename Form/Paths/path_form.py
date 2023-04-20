import os


class form:  # Aquí están las rutas de los XPATH
    URL = "https://demoqa.com/automation-practice-form"
    nombre = "//input[@id='firstName']"
    apellido = "//input[contains(@id,'lastName')]"
    mail = "//input[contains(@id,'userEmail')]"
    movil = "//input[contains(@id,'userNumber')]"
    datepicker = "//input[@id='dateOfBirthInput']"
    mes = "//select[@class='react-datepicker__month-select']"
    ano = "//select[contains(@class,'react-datepicker__year-select')]"
    dia = "//div[@class='react-datepicker__day react-datepicker__day--025'][contains(.,'25')]"
    asignaturas = "//div[contains(@class,'subjects-auto-complete__value-container " \
                  "subjects-auto-complete__value-container--is-multi css-1hwfws3')]"
    direccion = "//textarea[contains(@id,'currentAddress')]"
    estado = "//div[@class=' css-1hwfws3'][contains(.,'Select State')]"
    ciudad = "//div[@class='col-md-4 col-sm-12'][contains(.,'Select City')]"
    submit = "//button[contains(@id,'submit')]"
    ruta_imagen = "..//..//Files//sampleFile.jpeg"
    btn_uplodad = "//*[@id='uploadPicture']"
    closed_modal = "//button[contains(@id,'closeLargeModal')]"
    deportes = "//label[contains(@for,'hobbies-checkbox-1')]"
    musica = "//label[contains(@for,'hobbies-checkbox-3')]"
    lectura = "//label[@for='hobbies-checkbox-2'][contains(.,'Reading')]"
    Lista_Elementos = [nombre, apellido, mail, movil, direccion]


class Excel:
    HojaCorreo = "Form"


# Esta función toma un texto con palabras separadas por comas y devuelve una lista de palabras.
def separar_palabras(texto):
    palabras = texto.split(",")  # Dividir el texto en palabras utilizando la coma como delimitador
    palabras = [palabra.strip() for palabra in palabras]  # Eliminar espacios en blanco alrededor de cada palabra
    return palabras


# Este método sirve para obtener el XPATH del día (dentro de date-picker) correcto donde hacer click
def obtener_dia(fecha_objeto):

    # Obtener el día de la semana actual
    dia_semana = fecha_objeto.strftime('%A')
    # Obtener el mes actual
    mes = fecha_objeto.strftime('%B')
    # Obtener el día con el formato adecuado
    dia_mes = str(fecha_objeto.day) + (
        'th' if 11 <= fecha_objeto.day <= 13 else {1: 'st', 2: 'nd', 3: 'rd'}.get(fecha_objeto.day % 10, 'th'))
    if dia_mes.startswith('0'):
        dia_mes = dia_mes[1:]
    # Obtener el año
    anio = fecha_objeto.strftime('%Y')
    # EL xpath debe tener un formato similar a este //div[contains(@aria-label,'Choose Sunday, May 3rd, 1987')]
    xpath = f"//div[contains(@aria-label,'Choose {dia_semana}, {mes} {dia_mes}, {anio}')]"
    return xpath


# Este método sirve para obtener el mes (en formato texto en inglés) para poder seleccionar el mes del datepicker
def obtenerMes(mes):
    # Inicio la variable
    Mes_Escrito = ""

    # Listado con los meses en inglés
    meses_ingles = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October',
                    'November', 'December']

    # Compara el mes en (número y lo pone como mes escrito)
    match mes:
        case 1:
            Mes_Escrito = meses_ingles[0]
        case 2:
            Mes_Escrito = meses_ingles[1]
        case 3:
            Mes_Escrito = meses_ingles[2]
        case 4:
            Mes_Escrito = meses_ingles[3]
        case 5:
            Mes_Escrito = meses_ingles[4]
        case 6:
            Mes_Escrito = meses_ingles[5]
        case 7:
            Mes_Escrito = meses_ingles[6]
        case 8:
            Mes_Escrito = meses_ingles[7]
        case 9:
            Mes_Escrito = meses_ingles[8]
        case 10:
            Mes_Escrito = meses_ingles[9]
        case 11:
            Mes_Escrito = meses_ingles[10]
        case 12:
            Mes_Escrito = meses_ingles[11]

    return Mes_Escrito  # Devuelve el mes en formato Texto


# Este método obtiene el XPATH del Género y lo devuelve
def obtenerGenero(dato):
    xpath = ""
    male = "//label[@for='gender-radio-1'][contains(.,'Male')]"
    female = "//label[@for='gender-radio-2'][contains(.,'Female')]"
    other = "//label[@for='gender-radio-3'][contains(.,'Other')]"
    # Aquí se establece cuál es género obtenido en el Excel y que debe marcar el formulario
    match dato:
        case "Male":
            xpath = male
        case "Female":
            xpath = female
        case "Other":
            xpath = other

    return xpath


# Este método sirve para modificar la ruta actual y convertirla en la ruta relativa necesaria para la subida
# del archivo JPG
def ruta_relativa():
    # Obtén la ruta del directorio actual
    ruta_actual = os.path.dirname(os.path.abspath(__file__))
    # Modifica la ruta actual para que tenga el formato esperado
    ruta_imagen_modificada = ruta_actual.replace("\\", "//")
    partes = ruta_imagen_modificada.split("//")  # Dividir el texto en partes utilizando "//" como delimitador
    nueva_cadena = "//".join(partes[:-1])  # Unir las partes excepto la última
    nueva_cadena += "//"  # Agregar de nuevo el último "//" al final
    return nueva_cadena + "Files//tester.jpg"  # Ahora tenemos la ruta actual del archivo JPG
