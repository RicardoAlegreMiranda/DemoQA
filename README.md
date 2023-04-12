
# Automatización DEMO-QA por Ricardo Alegre

Este proyecto contiene el código fuente necesario para automatizar las pruebas de regresión de las funcionalidades de la Web pública https://demoqa.com/elements y https://demoqa.com/automation-practice-form


Para las pruebas se utiliza un archivo Excel del cual se importan los datos de prueba, en cada hoja del Excel hay datos para las pruebas los cuales se pueden editar y cambiar por nuevos datos de prueba. Se podría cambiar la fuente de datos de Excel a cualquier otra fuente, como por ejemplo MySQL.

Se han usado los frameworks de:

- Selenium
- Pytest
- Allure
- PyCharm IDE


# Enfoque de las pruebas:
En las pruebas se realiza una regresión completa por todas las principales funcionalidades de la Web, en apartados Elementos y Formulario, también se pueden utilizar algunas pruebas como un "Smoke Test" y validar que el entorno (en este caso la Web de DEMOQA) están funcionando correctamente


# ¿Cómo usar?:
Se puede ejecutar el archivo main.py el cual ejecuta todos los casos de prueba o  bien se pueden ejecutar los casos de prueba individualmente desde las Carpetas Elements/Test y Form/Test. Actualmente hay 15 casos de prueba, los cuales tardan unos 2 minutos aprox. en ser ejecutados.

 ![main](https://user-images.githubusercontent.com/40073353/231497110-75d74e74-dccd-4adf-9fa5-1dabbd4bf812.jpg)

# Datos de prueba:
En la carpeta Test_Dates está el documento Excel. Cada Hoja contiene los datos para un caso de prueba, algunas pruebas se pueden añadir todos los datos de pruebas deseados y el caso de prueba se ejecutará una vez por cada conjunto de pruebas portado.

Por ejemplo: En la TestBox hay 3 líneas de datos de prueba, si se añaden líneas adicionales las pruebas se ejecutarán una vez por cada línea, o si se borran líneas el caso se ejecutará menos veces.

![excel](https://user-images.githubusercontent.com/40073353/231498067-7c3ae46f-44ef-45aa-bf49-2b4fe42c4db4.jpg)


# Reportes:
Al terminar la ejecución (el archivo main.py) se devuelve en pantalla el total de pruebas ejecutas, el número pruebas pasadas y el número de pruebas falladas. 
 
 ![PyTestReport](https://user-images.githubusercontent.com/40073353/231497407-1b937466-ee1a-4ba8-a47d-5e7d026ed563.jpg)
  
También se genera automaticamente un reporte con el framework de allurereports, guarda datos sobre la ejecución de la prueba y toma capturas de pantalla a modo de evidencia de la ejecución. Para poder visualizar dicho informe es necesario abrir el servidor de allurserver(Es necesario tener instalado allurereports).

Para iniciar el servidor se puede hacer desde la terminal de PyCharm del proyecto con el comando: allure serve .\allurereports\ en la carpeta: allurereports
 
 
 Los informes que presenta se ven asi: 

![allure1](https://user-images.githubusercontent.com/40073353/231497552-d0608e11-7c2e-428b-b1d0-0510690e5d05.jpg)

![allure2](https://user-images.githubusercontent.com/40073353/231497626-313c9a4b-1a07-44e9-87de-2f7eaa4f1d5c.jpg)

![allure3](https://user-images.githubusercontent.com/40073353/231497706-800cfd1f-80a1-4028-8762-144999a03474.jpg)
  
 # Estructura:
En la carpeta Funcions se guardan los métodos más utilizados, dicha carpeta se importa en todos los casos de prueba.

En las carpetas Paths están los archivos para las rutas (XPATH e ID) y algunos métodos que son únicos para la prueba en cuestión, por ejemplo en la ruta: Form/Paths está el archivo path_form.py el cual contiene todas las rutas necesarias paras las pruebas. Además contiene la ruta para acceder a los datos de pruebas del documento excel, y algunos métodos propios que son necesarios para ejecutar la prueba de dicho formulario. 
 
Todos estos datos y métodos serán utilizados en el archivo Form/Test/test_form-py en dicho archivo están los casos de prueba para el formulario.

Al utilizar PyTest cada archivo de pruebas (test_*****.py) tiene las funciones:

- def setup_funtion() para iniciar los datos y el entorno que necesita la prueba (generalmente el Driver de Chorme)

- def test_Ejemplo_Uno() Donde se realiza la prueba con los assert necesarios para validar que cumple la funcionalidad que deseamos probar

- def test_Ejemplo_Dos().....las pruebas se inician de manera secuencial.

- def teardown_funtion () Para terminar la prueba, generalmente en este caso se ha utilizado para cerrar el Driver 

Este proyecto ha sido creado como demostración de cara a futuros procesos de selección, por Ricardo Alegre Miranda. El uso de dicho código fuente es público y se puede compartir sin necesidad de licencia.
