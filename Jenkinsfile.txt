// Este es el Script para ejecutar las pruebas en Jenkins W10 en máquina local
pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout([$class: 'GitSCM', branches: [[name: 'main']], extensions: [], userRemoteConfigs: [[url: 'https://github.com/RicardoAlegreMiranda/DemoQA.git']]])
            }
        }
        stage('Build') {
            steps {
                git branch: 'main', url: 'https://github.com/RicardoAlegreMiranda/DemoQA.git'
            }
        }
        stage('Test') {
            steps {
                // Instala todas los modulos necesarios
                bat '''
                    // Es necesario indicar la ruta exacta de Python, PIP y Allure, EDITAR estas rutas para que coincidan en su máquina    
                    set PIP=C:\\Users\\Usuario\\AppData\\Local\\Programs\\Python\\Python311\\Scripts\\pip.exe //
                    set PYTHON=C:\\Users\\Usuario\\AppData\\Local\\Programs\\Python\\Python311\\python.exe
                    set ALLURE=C:\\allure\\bin\\allure.bat
                    %PIP% install selenium 
                    %PIP% install allure-behave
                    %PIP% install allure-pytest
                    %PIP% install allure-python-commons
                    %PIP% install openpyxl
                    %PIP% install urllib3
                    %PIP% install pytest
                '''
                
                // Ejecuta las pruebas y genera un reporte
                 bat '%PYTHON% Main.py'
            }
        }
    }
}
