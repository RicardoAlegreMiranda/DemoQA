import pytest
import warnings

warnings.simplefilter(action='ignore', category=UserWarning)
# Ejecuta pruebas con pytest y generar reportes en el directorio "reports"
pytest.main(['-v', '--alluredir=reports'])
