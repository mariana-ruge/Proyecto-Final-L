from antlr4 import *
from gramaticaLexer import gramaticaLexer
from gramaticaParser import gramaticaParser
from gramaticaVisitor import CustomVisitor

def main():
    try:
        # Leer el archivo de entrada
        input_stream = FileStream("prueba.txt", encoding="utf-8")
        print("Archivo leído correctamente")
        print("\nContenido del archivo:")
        with open("prueba.txt", "r", encoding="utf-8") as f:
            print(f.read())
    except Exception as e:
        print(f"Error al leer el archivo: {e}")
        return

    # Crear el lexer y el parser
    lexer = gramaticaLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = gramaticaParser(token_stream)
    
    # Obtener el árbol de sintaxis
    tree = parser.program()
    print("\nÁrbol de sintaxis generado correctamente")
    
    # Crear y ejecutar el visitor personalizado
    visitor = CustomVisitor()
    results = visitor.visit(tree)
    
    # Mostrar resultados
    print("\nResultados de la ejecución:")
    if results:
        for result in results:
            print(result)
    else:
        print("No se generaron resultados")
    
    # Mostrar el estado final de las variables
    print("\nEstado final de las variables:")
    if visitor.variables:
        for var_name, value in visitor.variables.items():
            print(f"{var_name} = {value}")
    else:
        print("No hay variables definidas")

    # Mostrar las funciones definidas
    print("\nFunciones definidas:")
    if visitor.functions:
        for func_name in visitor.functions:
            print(f"- {func_name}")
    else:
        print("No hay funciones definidas")

if __name__ == "__main__":
    main()