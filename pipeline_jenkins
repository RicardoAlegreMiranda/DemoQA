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
            // Para evitar errores debe instalar los modulos necesarios antes de ejecutar las pruebas
                bat '''
                    set PIP=C:\\Users\\alegr\\AppData\\Local\\Programs\\Python\\Python311\\Scripts\\pip.exe
                    set PYTHON=C:\\Users\\alegr\\AppData\\Local\\Programs\\Python\\Python311\\python.exe
                    %PIP% install selenium 
                    %PIP% install allure-behave
                    %PIP% install allure-pytest
                    %PIP% install allure-python-commons
                    %PIP% install openpyxl
                    %PIP% install urllib3
                    %PYTHON% Main.py
                '''
            }
        }
    }
}
