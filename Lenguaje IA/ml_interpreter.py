# Importación de módulos estándar y librerías externas necesarias
import sys  # Proporciona acceso a funciones y parámetros específicos del sistema
import math  # Proporciona funciones matemáticas estándar
from antlr4 import *  # Importa las herramientas de ANTLR para análisis léxico y sintáctico

# Importación de módulos personalizados
from MLParser import MLParser  # Parser generado por ANTLR para interpretar el lenguaje
from MLListener import MLListener  # Clase base generada por ANTLR para manejar eventos del árbol
from MLLexer import MLLexer  # Lexer generado por ANTLR para tokenizar el código fuente
from error_handler import ErrorHandler  # Módulo para manejar y registrar errores
from file_operations import FileOperations  # Módulo para manejo de archivos
from matrix_operations import MatrixOperations  # Módulo para operaciones con matrices
from regresion import ejecutar_regresion  # Función para ejecutar regresiones
from matematicas import (  # Operaciones matemáticas definidas en un módulo externo
    potencia, raiz, suma, resta, multiplicacion, division, modulo
)
from perceptron import train_perceptron, classify_operation, train  # Función para entrenar un modelo de perceptrón
from loop import exitForLoop, exitWhileLoop  # Funciones para manejar bucles importadas de loops.py
from condicionales import Condicionales
from trigonometria import graficar_funcion_trigonometrica  # [Agregado] Importa el módulo de funciones trigonométricas



# Constante para definir el límite máximo de recursión en bucles
MAX_RECURSION_DEPTH = 1000  # Previene desbordamientos de pila en recursiones profundas


# Clase principal que extiende MLListener, utilizada para interpretar el lenguaje
class MLInterpreter(MLListener):
    # Constructor de la clase
    def __init__(self, input_lines):
        self.variables = {}  # Diccionario para almacenar variables y sus valores
        self.error_messages = []  # Lista para guardar mensajes de error
        self.input_lines = input_lines  # Código fuente que será interpretado
        self.execution_count = 0  # Contador para evitar múltiples ejecuciones de declaraciones
        self.perceptron_model = None  # Modelo de perceptrón, inicialmente vacío
        self.recursion_depth = 0  # Profundidad actual de recursión, usada para controlar bucles
        self.condicionales = Condicionales(self) #Para manejar los bucles

        

    # Método para evaluar expresiones de manera segura
    def _safe_eval(self, expression):
        try:
            expression = expression.replace("^", "**")  # Ajusta el operador de potenciación
            safe_context = {
                'raiz': raiz,
                'suma': suma,
                'resta': resta,
                'multiplicacion': multiplicacion,
                'division': division,
                'modulo': modulo,
                'potencia': potencia,
                'determinante': MatrixOperations.determinante,
                'transpuesta': MatrixOperations.transpuesta,
                'producto_punto': MatrixOperations.producto_punto,
                'multiplicacion_por_escalar': MatrixOperations.multiplicacion_por_escalar,
                **self.variables  # Incluye las variables definidas
            }

            result = eval(expression, {"__builtins__": None}, safe_context)
            return result

        except Exception as e:
            ErrorHandler.log_error(f"Error evaluando la expresión '{expression}': {e}")
            return None



    # Método para manejar bucles 'for', delega a la función modularizada
    def exitForLoop(self, ctx):
        # Llama a la función modularizada exitForLoop desde loops.py
        exitForLoop(self, ctx)

    # Método para manejar bucles 'while', delega a la función modularizada
    def exitWhileLoop(self, ctx, iterations=0):
        # Llama a la función modularizada exitWhileLoop desde loops.py
        exitWhileLoop(self, ctx, iterations)

    # Método para manejar declaraciones aritméticas
    def exitArithmeticStatement(self, ctx: MLParser.ArithmeticStatementContext):
        try:
            operation = ctx.getChild(0).getText()  # Extrae la operación ('calc' o 'predecir')
            expression = ctx.expression().getText()  # Extrae la expresión a evaluar

            # Evalúa la expresión utilizando _safe_eval
            result = self._safe_eval(expression)

            # Dependiendo de la operación, imprime el resultado
            if result is not None:
                if operation == 'calc':
                    print(f"{expression} = {result}")  # Imprime un cálculo
                elif operation == 'predecir':
                    print(f"Predicción: {result}")  # Imprime una predicción
            else:
                ErrorHandler.log_error(f"Invalid arithmetic statement: {expression}")

        except Exception as e:
            print(f"[error] {str(e)}")  # Imprime cualquier error inesperado
            
    
    def exitMatrixStatement(self, ctx):
        try:
            variable_name = ctx.ID().getText()
            if ctx.matrix():
                value = self._safe_eval(ctx.matrix().getText())
                self.variables[variable_name] = value
            elif ctx.matrixOperation():
                operation = ctx.matrixOperation().getText()
                value = self._safe_eval(operation)
                self.variables[variable_name] = value
            elif ctx.matrixAccess():
                # Manejo del acceso a matrices
                access_expr = ctx.matrixAccess().getText()
                value = self._safe_eval(access_expr)
                print(f"{variable_name}[...] = {value}")
            else:
                ErrorHandler.log_error(f"No se reconoce el tipo en matrixStatement para {variable_name}")
        except Exception as e:
            ErrorHandler.log_error(f"Error en matrixStatement: {e}")

    def exitFileStatement(self, ctx):
        try:
            if ctx.read():
                filename = ctx.read().getText()
                with open(filename, 'r') as file:
                    content = file.read()
                    print(content)
            elif ctx.write():
                filename = ctx.write().getText()
                expression = ctx.expression().getText()
                value = self._safe_eval(expression)
                with open(filename, 'w') as file:
                    file.write(str(value))
            else:
                ErrorHandler.log_error(f"Unknown file operation: {ctx.getText()}")
        except Exception as e:
            ErrorHandler.log_error(f"Error handling file statement: {e}")



    # Método para manejar asignaciones de variables
    def exitAssignment(self, ctx: MLParser.AssignmentContext):
        if ctx.start.line in self.variables:  # Evita ejecutar la misma línea más de una vez
            return

        variable_name = ctx.variable().getText()  # Obtiene el nombre de la variable
        expression = ctx.expression().getText()  # Obtiene la expresión asignada
        value = self._safe_eval(expression)  # Evalúa la expresión

        if value is not None:
            self.variables[variable_name] = value  # Asigna el valor a la variable
        else:
            ErrorHandler.log_error(f"Failed to assign value to {variable_name}")  # Registra un error si la evaluación falla

        self.variables[ctx.start.line] = variable_name  # Marca la línea como ejecutada
        
    # En el intérprete, agregar un método para manejar la instrucción de perceptrón
    def exitPerceptronStatement(self, ctx: MLParser.PerceptronStatementContext):
        # Verifica que el perceptrón esté entrenado antes de ejecutarlo
        if self.perceptron_model is None:
            print(" ")
            return
        # Extrae la operación o expresión contenida en el perceptronStatement
        operation = ctx.getText()
        
        # Clasifica la operación utilizando el perceptrón entrenado
        predicted_class = classify_operation(operation, *self.perceptron_model[:4])
        
        # Muestra el resultado de la clasificación
        print(f"Predicted Class: {predicted_class}")


    def exitConditionalStatement(self, ctx):
        """
        Maneja las declaraciones condicionales 'if' y 'else'.
        """
        self.condicionales.manejar_condicional(ctx)




    def handle_print_statement(self, ctx):
        """Método para manejar declaraciones de print de manera explícita"""
        try:
            # Extrae la expresión y depura su valor
            expression = ctx.expression().getText()  # Obtiene el texto de la expresión
            print(f"Expresión de print: {expression}")  # Depuración: muestra la expresión

            result = self._safe_eval(expression)  # Evalúa la expresión
            print(f"Resultado de la expresión print: {result}")  # Depuración: muestra el resultado

            if result is not None:
                print(result)  # Imprime el resultado
            else:
                ErrorHandler.log_error(f"Error al ejecutar print en la expresión: {expression}")
        except Exception as e:
            ErrorHandler.log_error(f"Error en la instrucción print: {e}")


    def exitPrintStatement(self, ctx):
        expression = ctx.expression().getText()  # Obtiene el texto de la expresión
        result = self._safe_eval(expression)  # Evalúa la expresión
        if result is not None:
            print(result)  # Imprime el resultado
        else:
            ErrorHandler.log_error(f"Error al evaluar la expresión print: {expression}")


    def exitStatement(self, ctx):
        if self.execution_count > 0:
            return

        # Verifica el tipo de declaración y llama al método correspondiente
        if ctx.printStatement():
            self.handle_print_statement(ctx.printStatement())  # Llama al método para manejar la instrucción print
        elif ctx.arithmeticStatement():
            self.exitArithmeticStatement(ctx.arithmeticStatement())
        elif ctx.matrixStatement():
            self.exitMatrixStatement(ctx.matrixStatement())
        elif ctx.fileStatement():
            self.exitFileStatement(ctx.fileStatement())
        elif ctx.loopStatement():
            self.exitLoopStatement(ctx.loopStatement())
        elif ctx.assignment():
            self.exitAssignment(ctx.assignment())
        elif ctx.incrementStatement():
            self.exitIncrementStatement(ctx.incrementStatement())
        elif ctx.regresionStatement():
            self.exitRegresionStatement(ctx.regresionStatement())

        self.execution_count += 1  # Incrementa el contador de ejecuciones

    
    
    def exitRegresionStatement(self, ctx: MLParser.RegresionStatementContext):
        try:
            # Verificar si ya se ejecutó la regresión
            if hasattr(self, 'regresion_ejecutada') and self.regresion_ejecutada:
                print("")
                return
            
            # Marcamos que la regresión ha sido ejecutada
            self.regresion_ejecutada = True

            # Obtén las dos expresiones
            X_expr = ctx.expression(0).getText()  # Primera expresión (datos)
            y_expr = ctx.expression(1).getText()  # Segunda expresión (objetivos)

            # Llama a la función de regresión
            result = ejecutar_regresion(X_expr, y_expr)

            # Imprime el resultado
            print(f"Regresión resultado: {result}")

        except Exception as e:
            print(f"[error] {str(e)}")



# Punto de entrada principal del programa
def main():
    # Verifica que se haya proporcionado un archivo como argumento
    if len(sys.argv) != 2:
        print("Usage: python ml_interpreter.py <script.txt>")  # Muestra un mensaje de uso
        return

    try:
        # Lee el archivo proporcionado como entrada
        with open(sys.argv[1], 'r') as file:
            input_lines = file.readlines()  # Lee todas las líneas
            input_code = ''.join(input_lines)  # Une las líneas en un solo string

        # Procesa el código fuente utilizando ANTLR
        input_stream = InputStream(input_code)  # Convierte el código a un flujo de entrada
        lexer = MLLexer(input_stream)  # Tokeniza el código
        stream = CommonTokenStream(lexer)  # Genera un flujo de tokens
        parser = MLParser(stream)  # Analiza el flujo de tokens
        tree = parser.program()  # Genera el árbol sintáctico
    


        # Entrena el perceptrón si se encuentra la instrucción correspondiente
        perceptron_model = None
        W1, b1, W2, b2, label_encoder = train_perceptron()  # Entrenar el modelo
        # Ahora puedes intentar clasificar operaciones después de que el modelo esté entrenado.
        operation = "calc(3 + 5)"  # Ejemplo de operación a clasificar
        predicted_class = classify_operation(operation, W1, b1, W2, b2, label_encoder)
        print(f"Predicted class: {predicted_class}")
        if 'train_perceptron' in input_code:
            perceptron_model = train_perceptron()

        # Crea una instancia del intérprete
        interpreter = MLInterpreter(input_lines)
        interpreter.perceptron_model = perceptron_model  # Asigna el modelo entrenado

        # Recorre el árbol sintáctico con el intérprete
        walker = ParseTreeWalker()  # Crea un objeto para recorrer el árbol
        walker.walk(interpreter, tree)  # Ejecuta el recorrido del árbol
        
    

    except Exception as e:
        # Maneja cualquier error durante la ejecución
        print(f"Execution error: {e}")


# Ejecuta la función principal si el script es ejecutado directamente
if __name__ == '__main__':
    main()

