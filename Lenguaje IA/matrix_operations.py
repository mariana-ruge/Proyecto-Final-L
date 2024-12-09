import numpy as np

class MatrixOperations:
    
    @staticmethod
    def suma(A, B):
        """Suma de dos matrices"""
        # Validación de tipo y dimensiones
        if len(A) != len(B) or len(A[0]) != len(B[0]):
            raise ValueError("Las matrices deben tener las mismas dimensiones para sumar")
        
        # Suma de las matrices componente por componente
        return [[A[i][j] + B[i][j] for j in range(len(A[0]))] for i in range(len(A))]





    @staticmethod
    def multiplicacion(A, B):
        """Multiplicación de dos matrices"""
        # Validación de tipo
        if not isinstance(A, list) or not isinstance(B, list):
            raise ValueError("Ambos argumentos deben ser matrices (listas de listas)")
        
        # Validación de dimensiones para multiplicación
        if len(A[0]) != len(B):
            raise ValueError("Las dimensiones de las matrices no son compatibles para la multiplicación")
        
        # Inicialización de la matriz de resultado
        result = [[0 for _ in range(len(B[0]))] for _ in range(len(A))]
        
        # Multiplicación de matrices (producto de filas por columnas)
        for i in range(len(A)):
            for j in range(len(B[0])):
                result[i][j] = sum(A[i][k] * B[k][j] for k in range(len(B)))
        
        return result

    @staticmethod
    def determinante(A):
        """Determinante de una matriz 2x2"""
        # Validación de tipo y dimensiones
        if not isinstance(A, list) or len(A) != 2 or len(A[0]) != 2:
            raise ValueError("Solo se soportan matrices 2x2 para calcular el determinante")
        
        # Cálculo del determinante para matrices 2x2
        return A[0][0] * A[1][1] - A[0][1] * A[1][0]

    @staticmethod
    def transpuesta(A):
        """Transpuesta de una matriz"""
        # Validación de tipo
        if not isinstance(A, list):
            raise ValueError("El argumento debe ser una matriz (lista de listas)")
        
        # Transposición de la matriz
        return [[A[j][i] for j in range(len(A))] for i in range(len(A[0]))]

    @staticmethod
    def producto_punto(v1, v2):
        """Producto punto de dos vectores"""
        # Validación de tipo
        if not isinstance(v1, list) or not isinstance(v2, list):
            raise ValueError("Ambos argumentos deben ser vectores (listas)")
        
        # Validación de dimensiones
        if len(v1) != len(v2):
            raise ValueError("Los vectores deben tener la misma longitud para el producto punto")
        
        # Cálculo del producto punto
        return sum(v1[i] * v2[i] for i in range(len(v1)))

    @staticmethod
    def multiplicacion_por_escalar(A, escalar):
        """Multiplicación de una matriz por un escalar"""
        # Validación de tipo para la matriz
        if not isinstance(A, list):
            raise ValueError("El primer argumento debe ser una matriz (lista de listas)")
        
        # Validación de tipo para el escalar
        if not isinstance(escalar, (int, float)):
            raise ValueError("El segundo argumento debe ser un número (int o float)")

        # Multiplicación de la matriz por el escalar
        return [[elemento * escalar for elemento in fila] for fila in A]
