import random

colors = ["Red", "Green", "Blue", "Yellow", "Black", "Magenta", "White", "Voilet", "Aqua", "Purple", "Indigo"]

class FuncionsAutoComplete:

    # Escoge un número de color al azar y devuelve los colores al azar
    @staticmethod
    def random_colors():
        numero_aleatorio = random.randrange(9)

        # Al menos debe tener 1 color
        if numero_aleatorio == 0:
            numero_aleatorio += 1

        print("Número de colores ", str(numero_aleatorio))
        colors_random = random.sample(colors, numero_aleatorio)
        return colors_random

    # Escoge un color al azar
    @staticmethod
    def one_color():
        color = random.choice(colors)
        return color
