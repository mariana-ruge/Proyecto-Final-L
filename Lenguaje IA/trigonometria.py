import numpy as np
import matplotlib.pyplot as plt

def graficar_funcion_trigonometrica(expr, rango=(-2 * np.pi, 2 * np.pi), puntos=1000):
    """
    Genera una gráfica de una función trigonométrica basada en una expresión.

    Parámetros:
    - expr (str): Expresión matemática de la función a graficar (por ejemplo, "np.sin(x)").
    - rango (tuple): Rango del dominio de la función (mínimo, máximo).
    - puntos (int): Número de puntos a evaluar en el rango.

    Devuelve:
    - None
    """
    try:
        # Crear el dominio de la función
        x = np.linspace(rango[0], rango[1], puntos)

        # Evaluar la expresión
        y = eval(expr)

        # Crear la gráfica
        plt.figure(figsize=(8, 6))
        plt.plot(x, y, label=f"y = {expr}", color="blue")
        plt.axhline(0, color="black", linewidth=0.8, linestyle="--")  # Eje X
        plt.axvline(0, color="black", linewidth=0.8, linestyle="--")  # Eje Y
        
        plt.title(f"Gráfica de {expr}")
        plt.xlabel("x")
        plt.ylabel("y")
        plt.legend()
        plt.grid(True, linestyle="--", alpha=0.6)

        # Guardar y mostrar la gráfica
        nombre_archivo = "grafica_trigonometrica.jpg"
        plt.savefig(nombre_archivo, format="jpg")
        plt.close()

        print(f"La gráfica se ha guardado como '{nombre_archivo}'")

    except Exception as e:
        print(f"[error] Ocurrió un error al generar la gráfica: {str(e)}")

# Ejemplo de uso
if __name__ == "__main__":
    expresion = "np.sin(x) + np.cos(x)"
    graficar_funcion_trigonometrica(expresion)

    # Puedes probar otras expresiones, como:
    # "np.sin(x)"
    # "np.cos(x)"
    # "np.tan(x)"
    # "np.sin(x) * np.cos(x)"
