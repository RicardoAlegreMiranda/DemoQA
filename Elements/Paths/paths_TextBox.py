class TextBox:
    Url = "https://demoqa.com/text-box"
    Name = "//input[contains(@id,'userName')]"
    Email = "//input[contains(@id,'userEmail')]"
    CAddress = "//textarea[contains(@id,'currentAddress')]"#Current Address
    PAdress = "//textarea[contains(@id,'permanentAddress')]" #Permanent Address
    Submit = "//button[@id='submit']"
    finalName = "//p[contains(@id,'name')]"
    finalEmail = "//p[contains(@id,'email')]"
    finalCAddress = "//p[contains(@id,'currentAddress')]"
    finalPAddress = "//p[contains(@id,'permanentAddress')]"
    ListaDatos = [Url, Name, Email, CAddress, PAdress]
    ListaDatosFinales = [finalName, finalEmail, finalCAddress, finalPAddress]
    EmailClassError = "mr-sm-2 field-error form-control"

class Excel:
    HojaTextBoxOK = "TextBox"
    HojaCorreo = "Correo"
