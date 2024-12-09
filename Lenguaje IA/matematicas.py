# matematicas.py

# matematicas.py

def raiz(a, x):
    if x == 0:
        raise ValueError("No se puede calcular la raíz con exponente cero")
    return a ** (1 / x)


def potencia(base, exponente):
    return base ** exponente

def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    if b != 0:
        return a / b
    else:
        raise ValueError("No se puede dividir por cero")

def modulo(a, b):
    return a % b
