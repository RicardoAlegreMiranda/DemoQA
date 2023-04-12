import openpyxl

class FuncionesExcel:
    def __init__(self, ruta_excel, hoja_nombre):
        self.ruta_excel = ruta_excel
        self.libro_excel = openpyxl.load_workbook(self.ruta_excel)
        self.hoja_excel = self.libro_excel[hoja_nombre]


    def obtener_num_filas(self):
        return self.hoja_excel.max_row

    def obtener_num_columnas(self):
        return self.hoja_excel.max_column

    def leer_celda(self, fila, columna):
        return self.hoja_excel.cell(row=fila, column=columna).value

    def escribir_celda(self, fila, columna, valor):
        self.hoja_excel.cell(row=fila, column=columna).value = valor
        self.libro_excel.save(self.ruta_excel)

    def cerrar_excel(self):
        self.libro_excel.close()