import random

class SliderFuncions:
    # Inicia las variables
    def __init__(self, driver, slider):
        self.driver = driver
        self.slider = slider

    # Este método arrastra el slider a la posición indicada
    def arrastrar_slider(self, numero):
        self.driver.execute_script("arguments[0].value = arguments[1]", self.slider, numero)
        print("Slider movido a posición ", numero)

    # Genera 3 números aleatorios y los guarda en una lista
    def numeros_aleatorios(self):

        aleatorios = []

        for n in range(0, 3):
            aleatorios.append(random.randint(0, 100))

        return aleatorios
