import numpy as np
import matplotlib.pyplot as plt
from regresion_2 import RegresionLineal  # Asegúrate de tener esta clase definida

def ejecutar_regresion(X_expr, y_expr):
    """Ejecuta la regresión lineal y guarda la gráfica."""
    try:
        # Convertir las expresiones a listas
        X = np.array(eval(X_expr))  # Usar np.array para asegurar que X sea una matriz numpy
        y = np.array(eval(y_expr))  # Lo mismo para y

        # Verifica la forma de X y y para asegurarse de que sean 2D (filas, columnas)
        if X.ndim == 1:
            X = X.reshape(-1, 1)  # Si es 1D, lo transformamos en 2D (con una columna)
        if y.ndim == 1:
            y = y.reshape(-1, 1)  # Si y es 1D, lo transformamos en 2D (con una columna)

        # Ejecuta la regresión usando el modelo de regresión lineal
        modelo = RegresionLineal()
        modelo.ajustar(X, y)

        # Imprime los resultados de la regresión
        print("Coeficientes:", modelo.coeficientes)
        print("Intercepto:", modelo.intercepto)
        
        # Realiza una predicción de ejemplo (asegurándose de que X_test tenga la forma correcta)
        X_test = np.array([[6]])  # Cambio: ahora X_test es una matriz 2D de una sola fila
        prediction = modelo.predecir(X_test)
        print("Predicción para X=[[6]]:", prediction)

        # Resumen del modelo
        print("Resumen del modelo:", modelo.resumen(X, y))

        # Crear la gráfica de la regresión
        plt.figure(figsize=(8, 6))
        
        # Graficar los puntos originales
        plt.scatter(X, y, color='blue', label='Datos originales')
        
        # Graficar la línea de regresión
        plt.plot(X, modelo.predecir(X), color='red', label='Línea de regresión')

        # Etiquetas y título
        plt.xlabel("X")
        plt.ylabel("y")
        plt.title("Regresión Lineal")
        plt.legend()

        # Guardar la gráfica como un archivo .jpg
        plt.savefig("regresion_resultado.jpg", format='jpg')
        plt.close()  # Cerrar la gráfica

        print("La gráfica se ha guardado como 'regresion_resultado.jpg'")

    except Exception as e:
        print(f"[error] Error en la ejecución de la regresión: {str(e)}")
