import numpy as np
import matplotlib.pyplot as plt
import os

def graficar_funcion_trigonometrica(func_expr, rango, archivo_salida="grafica_trigonometrica"):
    print(f"[DEBUG] Llamada a graficar_funcion_trigonometrica con la función: {func_expr}, rango: {rango}")
    
    # Crear un rango de valores de x
    x = np.linspace(rango[0], rango[1], 400)

    # Evaluar la expresión de la función trigonométrica usando eval
    try:
        # Pasa el contexto global (diccionario de funciones y variables) a eval
        y = eval(func_expr, {"np": np, "sin": np.sin, "cos": np.cos, "tan": np.tan, "x": x})

        # Graficar la función
        plt.plot(x, y)
        plt.title(f"Gráfica de {func_expr} con rango {rango}")
        plt.xlabel("x")
        plt.ylabel("y")
        plt.grid(True)

        # Generar un nombre único para cada archivo
        i = 1
        archivo_final = f"{archivo_salida}_{i}.jpg"
        while os.path.exists(archivo_final):
            print(f"[DEBUG] El archivo {archivo_final} ya existe, incrementando el número.")
            i += 1
            archivo_final = f"{archivo_salida}_{i}.jpg"
        
        # Guardar la gráfica como archivo .jpg
        print(f"[DEBUG] Guardando la gráfica en {archivo_final}")
        plt.savefig(archivo_final, format='jpg')
        print(f"Gráfica guardada en {archivo_final}")

    except Exception as e:
        print(f"[error] Ocurrió un error al generar la gráfica: {str(e)}")
