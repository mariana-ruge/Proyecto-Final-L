import random
# Función para generar un número aleatorio entre un rango
def generar_numero_aleatorio(min_value=None, max_value=None):
    if min_value is None and max_value is None:
        return random.random()  # Devuelve un número entre 0 y 1 si no se especifican límites
    elif min_value is None:
        return random.randint(0, max_value)  # Si solo se especifica un máximo
    elif max_value is None:
        return random.randint(min_value, 100)  # Si solo se especifica un mínimo
    else:
        return random.randint(min_value, max_value)  # Rango completo
