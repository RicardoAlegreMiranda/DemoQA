from selenium.webdriver.common.by import By


class WebTables:
    URL = "https://demoqa.com/webtables"
    add = "//button[contains(@id,'addNewRecordButton')]"
    edit = "// *[ @ id = 'edit-record-1']"
    delete = "//*[@id='delete-record-1']"
    FirstName = "//input[contains(@id,'firstName')]"
    LastName = "//input[contains(@id,'lastName')]"
    Email = "//input[contains(@id,'userEmail')]"
    Age = "//input[contains(@id,'age')]"
    Salary = "//input[contains(@id,'salary')]"
    Department = "//input[contains(@id,'department')]"
    Submit = "//button[contains(@id,'submit')]"
    SearchBox = "//input[contains(@id,'searchBox')]"
    tabla = "//*[@id='app']/div/div/div[2]/div[2]/div[2]/div[3]/div[1]/div[2]"
    ListaXPATH = [FirstName, LastName, Email, Age, Salary, Department]
    ListaDatosModifica = ["Roberto", "Gonzalez", "roberto@gmail.com", "52", "22000", "RR.HH"]

    # Este método sirve para obtener el Xpath correcto para borrar una fila
    def borrarTabla(NumeroFila):
        borrar = "//*[@id='delete-record-" + str(NumeroFila) + "']"
        return borrar

    # Este método sirve para obtener el Xpath correcto para modificar una fila
    def modificarTabla(NumeroFila):
        modificar = "// *[ @ id = 'edit-record-" + str(NumeroFila) + "']"
        return modificar

class Excel:
    DirExcel = "../../Test_Dates/TestDates.xlsx"
    HojaCorreo = "WebTables"





