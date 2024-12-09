import numpy as np

class RegresionLineal:
    def _init_(self):
        self.coeficientes = None
        self.intercepto = None
    
    def ajustar(self, X, y):
        """Ajusta el modelo de regresión lineal usando mínimos cuadrados."""
        X = np.array(X)
        y = np.array(y)
        
        X_con_intercepto = np.column_stack((np.ones(X.shape[0]), X))
        
        coefs = np.linalg.inv(X_con_intercepto.T @ X_con_intercepto) @ X_con_intercepto.T @ y
        
        self.intercepto = coefs[0]
        self.coeficientes = coefs[1:]
        
        return self
    
    def predecir(self, X):
        """Realiza predicciones usando el modelo."""
        X = np.array(X)
        return self.intercepto + np.dot(X, self.coeficientes)
    
    def error_cuadratico_medio(self, X, y):
        """
        Calcula el Error Cuadrático Medio (MSE).
        
        Args:
            X (array-like): Características de entrada
            y (array-like): Valores objetivo reales
        
        Returns:
            float: Error Cuadrático Medio
        """
        X = np.array(X)
        y = np.array(y)
        
        y_pred = self.predecir(X)
        
        # Calcula el Error Cuadrático Medio
        mse = np.mean((y - y_pred) ** 2)
        
        return mse
    
    def resumen(self, X, y):
        """
        Proporciona un resumen completo del modelo.
        
        Args:
            X (array-like): Características de entrada
            y (array-like): Valores objetivo reales
        
        Returns:
            dict: Resumen de métricas del modelo
        """
        return {
            'intercepto': self.intercepto,
            'coeficientes': self.coeficientes,
            'error_cuadratico_medio': self.error_cuadratico_medio(X, y)
        }