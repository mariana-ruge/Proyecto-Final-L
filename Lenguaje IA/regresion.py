import numpy as np
import matplotlib.pyplot as plt
from regresion_2 import RegresionLineal  # Asegúrate de tener esta clase definida

def ejecutar_regresion(X_expr, y_expr):
    try:
        X = np.array(eval(X_expr))
        y = np.array(eval(y_expr))
        if X.ndim == 1:
            X = X.reshape(-1, 1)
        if y.ndim == 1:
            y = y.reshape(-1, 1)

        modelo = RegresionLineal()
        modelo.ajustar(X, y)

        print("Coeficientes:", modelo.coeficientes)
        print("Intercepto:", modelo.intercepto)

        X_test = np.array([[6]])
        prediction = modelo.predecir(X_test)
        print("Predicción para X=[[6]]:", prediction)

        print("Resumen del modelo:", modelo.resumen(X, y))

        plt.figure(figsize=(8, 6))
        plt.scatter(X, y, color='blue', label='Datos originales')
        plt.plot(X, modelo.predecir(X), color='red', label='Línea de regresión')
        plt.xlabel("X")
        plt.ylabel("y")
        plt.title("Regresión Lineal")
        plt.legend()
        plt.savefig("regresion_resultado.jpg", format='jpg')
        plt.close()

        print("La gráfica se ha guardado como 'regresion_resultado.jpg'")
        return modelo

    except Exception as e:
        print(f"[error] Error en la ejecución de la regresión: {str(e)}")
        return None
