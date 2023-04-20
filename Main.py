import pytest
import warnings

# Ignoro los Warning de openpyxl
warnings.simplefilter(action='ignore', category=UserWarning)

# Ejecuta pruebas con pytest y generar reportes en el directorio "reports"
pytest.main(['-v', '--alluredir=reports'])
