import numpy as np

# Definir la función de activación sigmoide
# Esta función transforma los valores de entrada a un rango entre 0 y 1.
# Se usa para "activar" neuronas en redes neuronales.
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

# Derivada de la función sigmoide
# Se utiliza para calcular los ajustes durante el entrenamiento de la red neuronal.
def sigmoid_derivative(x):
    return x * (1 - x)

# Lista de operaciones a clasificar
# Estas son cadenas de texto que representan diferentes tipos de declaraciones y estructuras de código.
operations = [
    "calc(3 + 5)",  # Operación aritmética
    "predecir(2 * 3)",  # Operación aritmética
    "matrix A = add([1, 2], [3, 4])",  # Operación de matrices
    "if (x > 5) { calc(2 + 2) }",  # Declaración condicional
    "read(\"file.txt\")",  # Operación de archivo: leer
    "write(\"file.txt\", 42)",  # Operación de archivo: escribir
    "print(\"Result\", 42)",  # Operación de archivo: imprimir
    "while (x < 10) { x++ }",  # Estructura de bucle: while
    "for (i in range(0, 10)) { calc(i * 2) }",  # Estructura de bucle: for
    "regresion([1, 2, 3], [4, 5, 6])"  # Operación de regresión
]

# Lista de etiquetas correspondientes a cada operación
# Estas etiquetas representan las categorías de cada operación.
labels = [
    "arithmeticStatement",  # Operaciones aritméticas
    "arithmeticStatement",  # Operaciones aritméticas
    "matrixStatement",  # Operaciones con matrices
    "conditionalStatement",  # Declaraciones condicionales
    "fileStatement",  # Operaciones de archivo
    "fileStatement",  # Operaciones de archivo
    "fileStatement",  # Operaciones de archivo
    "loopStatement",  # Declaraciones de bucles
    "loopStatement",  # Declaraciones de bucles
    "regresionStatement"  # Operaciones de regresión
]

# Función para extraer características de una operación
# Convierte cada operación en un conjunto de números (vectores) basados en su contenido.
def extract_features(operation):
    features = []
    features.append(operation.count('calc'))          # Cuenta cuántas veces aparece 'calc'.
    features.append(operation.count('predecir'))      # Cuenta cuántas veces aparece 'predecir'.
    features.append(operation.count('matrix'))        # Cuenta cuántas veces aparece 'matrix'.
    features.append(operation.count('if'))            # Cuenta cuántas veces aparece 'if'.
    features.append(operation.count('read'))          # Cuenta cuántas veces aparece 'read'.
    features.append(operation.count('write'))         # Cuenta cuántas veces aparece 'write'.
    features.append(operation.count('print'))         # Cuenta cuántas veces aparece 'print'.
    features.append(operation.count('while'))         # Cuenta cuántas veces aparece 'while'.
    features.append(operation.count('for'))           # Cuenta cuántas veces aparece 'for'.
    features.append(operation.count('regresion'))     # Cuenta cuántas veces aparece 'regresion'.
    return features  # Devuelve un vector de características.

# Función para codificar etiquetas en números
# Convierte las categorías de texto en números, ya que las redes neuronales trabajan con números.
def encode_labels(labels):
    label_encoder = {label: idx for idx, label in enumerate(set(labels))}  # Asigna un número único a cada etiqueta.
    return np.array([label_encoder[label] for label in labels]), label_encoder  # Devuelve las etiquetas codificadas y el diccionario.

# Función para entrenar el perceptrón
# Aquí es donde el modelo "aprende" a clasificar las operaciones.
def train(X, y_encoded, input_size, hidden_size=10, output_size=1, epochs=1000, learning_rate=0.01):
    # Inicialización aleatoria de los pesos de las conexiones entre neuronas
    np.random.seed(42)  # Para garantizar resultados reproducibles.
    W1 = np.random.randn(input_size, hidden_size)  # Pesos entre la capa de entrada y la oculta.
    b1 = np.zeros((1, hidden_size))  # Sesgo de la capa oculta.
    W2 = np.random.randn(hidden_size, output_size)  # Pesos entre la capa oculta y la de salida.
    b2 = np.zeros((1, output_size))  # Sesgo de la capa de salida.

    # Entrenamiento mediante propagación hacia adelante y retropropagación
    for epoch in range(epochs):
        # Propagación hacia adelante
        z1 = np.dot(X, W1) + b1  # Calcula la entrada a la capa oculta.
        a1 = sigmoid(z1)  # Activa la capa oculta.
        z2 = np.dot(a1, W2) + b2  # Calcula la entrada a la capa de salida.
        a2 = sigmoid(z2)  # Activa la capa de salida.

        # Cálculo del error (diferencia entre salida esperada y salida real)
        error = a2 - np.eye(output_size)[y_encoded]

        # Retropropagación del error
        d_z2 = error * sigmoid_derivative(a2)  # Gradiente de la salida.
        d_W2 = np.dot(a1.T, d_z2)  # Ajuste para los pesos W2.
        d_b2 = np.sum(d_z2, axis=0, keepdims=True)  # Ajuste para los sesgos b2.

        d_a1 = np.dot(d_z2, W2.T)  # Error propagado hacia atrás a la capa oculta.
        d_z1 = d_a1 * sigmoid_derivative(a1)  # Gradiente de la capa oculta.
        d_W1 = np.dot(X.T, d_z1)  # Ajuste para los pesos W1.
        d_b1 = np.sum(d_z1, axis=0, keepdims=True)  # Ajuste para los sesgos b1.

        # Actualización de los pesos y sesgos
        W1 -= learning_rate * d_W1
        b1 -= learning_rate * d_b1
        W2 -= learning_rate * d_W2
        b2 -= learning_rate * d_b2

        # Mostrar la pérdida cada 100 épocas
        if epoch % 100 == 0:
            loss = np.mean(np.square(error))  # Error cuadrático medio.
            print(f"Epoch {epoch}, Loss: {loss:.4f}")

    return W1, b1, W2, b2  # Devuelve los pesos y sesgos entrenados.

# Función para clasificar nuevas operaciones
# Usa los pesos entrenados para predecir a qué categoría pertenece una nueva operación.
# Función para clasificar nuevas operaciones
def classify_operation(operation, W1, b1, W2, b2, label_encoder):
    # Extraer las características de la operación
    features = np.array(extract_features(operation)).reshape(1, -1)  # Convierte la operación en un vector de características.
    z1 = np.dot(features, W1) + b1  # Calcula la entrada a la capa oculta.
    a1 = sigmoid(z1)  # Activa la capa oculta.
    z2 = np.dot(a1, W2) + b2  # Calcula la entrada a la capa de salida.
    a2 = sigmoid(z2)  # Activa la capa de salida.

    # Obtiene la clase predicha en base a la mayor probabilidad
    predicted_class_index = np.argmax(a2, axis=1)[0]

    # Devuelve el nombre de la clase en lugar del índice
    predicted_class_name = [key for key, value in label_encoder.items() if value == predicted_class_index][0]
    return predicted_class_name


# Función principal para entrenar y clasificar
def train_perceptron():
    X = np.array([extract_features(op) for op in operations])  # Convierte todas las operaciones en vectores de características.
    y_encoded, label_encoder = encode_labels(labels)  # Codifica las etiquetas.

    # Entrenar el modelo con los datos
    input_size = X.shape[1]  # Número de características de entrada.
    W1, b1, W2, b2 = train(X, y_encoded, input_size, hidden_size=10, output_size=len(label_encoder), epochs=1000, learning_rate=0.01)

    return W1, b1, W2, b2, label_encoder  # Devuelve el modelo entrenado y el codificador de etiquetas.

if __name__ == "__main__":
    W1, b1, W2, b2, label_encoder = train_perceptron()
