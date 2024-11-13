### ml_dsl_project/run_dsl.py
# Punto de entrada principal para ejecutar scripts en el DSL

import sys
from antlr4 import *
from antlr.generated.MLDSLParser import MLDSLParser
from antlr.generated.MLDSLLexer import MLDSLLexer
from src.interpreter import MLInterpreter

def initialize_models():
    from src.ml_models.mlp import MLPModel
    from src.ml_models.regression import RegressionModel
    from src.ml_models.clustering import ClusteringModel
    
    model_registry = {}
    model_registry['mlp'] = MLPModel()
    model_registry['regression'] = RegressionModel()
    model_registry['clustering'] = ClusteringModel()
    return model_registry

def main(argv):
    if len(argv) < 2:
        print("Usage: python run_dsl.py <input_file>")
        return

    input_file = FileStream(argv[1])

    try:
        # Crear el lexer, parser, y el árbol de parseo
        lexer = MLDSLLexer(input_file)
        stream = CommonTokenStream(lexer)
        parser = MLDSLParser(stream)
        tree = parser.program()

        # Verificar errores de sintaxis
        if parser.getNumberOfSyntaxErrors() > 0:
            print("Error: Se encontraron errores de sintaxis en el script DSL.")
            return

        # Inicializar los modelos de ML
        model_registry = initialize_models()

        # Interpretar el árbol de parseo usando el patrón visitor
        interpreter = MLInterpreter()
        interpreter.model_registry = model_registry
        interpreter.visit(tree)

    except Exception as e:
        print(f"Ocurrió un error al procesar el script DSL: {e}")

if __name__ == "__main__":
    main(sys.argv)
