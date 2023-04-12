import pytest
import subprocess


# Ejecutar casos de prueba con pytest
pytest.main(["-s", "-v", "--alluredir=reportes"])

# Iniciar servidor de Allure después de la ejecución de las pruebas
#subprocess.run(["allure", "serve", "reportes"])