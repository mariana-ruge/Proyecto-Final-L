from antlr4 import *
from gramaticaParser import gramaticaParser
import math
import numpy as np
import matplotlib.pyplot as plt

class CustomVisitor(ParseTreeVisitor):
    def __init__(self):
        self.variables = {}
        self.functions = {}
        self.results = []
        print("Visitor inicializado")

    def visitProgram(self, ctx: gramaticaParser.ProgramContext):
        print("\nIniciando visita del programa")
        if hasattr(ctx, 'statement'):
            statements = ctx.statement()
            for stmt in statements:
                result = self.visit(stmt)
                if result is not None:
                    self.results.append(result)
            
            # Imprimir resultados al final
            print("\nResultados de la ejecución:")
            for result in self.results:
                print(result)
            
            print("\nEstado final de las variables:")
            for var, value in self.variables.items():
                print(f"{var} = {value}")
            
            print("\nFunciones definidas:")
            for func in self.functions:
                print(f"{func}: {self.functions[func]['params']}")
            
            return self.results
        return []

    def visitAssignment_stmt(self, ctx: gramaticaParser.Assignment_stmtContext):
        name = ctx.ID().getText()
        value = self.visit(ctx.expr())
        if value is not None:
            self.variables[name] = value
            print(f"Asignado {value} a {name}")  # Add print for debugging
            return f"Asignado {value} a {name}"
        return None
    
    def visitArithmetic_stmt(self, ctx):
        left = self.visit(ctx.expr(0))  # Visit the first expression
        right = self.visit(ctx.expr(1))  # Visit the second expression
        operator = ctx.getChild(1).getText()  # Get the operator
        if operator == "+":
            return left + right
        elif operator == "-":
            return left - right
        elif operator == "*":
            return left * right
        elif operator == "/":
            return left / right
    
    def visitExpr(self, ctx):
        if ctx.NUMERO():
            return float(ctx.NUMERO().getText())
        elif ctx.ID():
            return self.variables.get(ctx.ID().getText(), None)
        elif ctx.expr():
            left = self.visit(ctx.expr(0))
            right = self.visit(ctx.expr(1))
            operator = ctx.getChild(1).getText()
            if operator == '+':
                return left + right
            elif operator == '-':
                return left - right
            elif operator == '*':
                return left * right
            elif operator == '/':
                return left / right


    def visitFunction_call(self, ctx):
        if not ctx:
            return None
        func_name = ctx.getChild(0).getText()
        arg = self.visit(ctx.expr())
        if arg is not None:
            try:
                if func_name == 'sqrt':
                    return math.sqrt(arg)
                elif func_name == 'sin':
                    return math.sin(arg)
                elif func_name == 'cos':
                    return math.cos(arg)
                elif func_name == 'tan':
                    return math.tan(arg)
                elif func_name == 'transpose' and isinstance(arg, np.ndarray):
                    return np.transpose(arg)
                elif func_name == 'inverse' and isinstance(arg, np.ndarray):
                    return np.linalg.inv(arg)
            except Exception as e:
                print(f"Error en función {func_name}: {e}")
        return None


    def visitMatrix_stmt(self, ctx:gramaticaParser.Matrix_stmtContext):
        try:
            name = ctx.ID().getText()
            matrix = self.visit(ctx.matrix_operation() if ctx.matrix_operation() else ctx.matrix())
            if isinstance(matrix, np.ndarray):
                self.variables[name] = matrix
                return f"Matriz {name} = \n{matrix}"
        except Exception as e:
            print(f"Error en matriz: {e}")
        return None

    def visitMatrix(self, ctx:gramaticaParser.MatrixContext):
        try:
            rows = [self.visit(row) for row in ctx.row()]
            return np.array(rows, dtype=float)
        except Exception as e:
            print(f"Error procesando matriz: {e}")
        return None

    def visitRow(self, ctx:gramaticaParser.RowContext):
        return [float(self.visit(expr)) for expr in ctx.expr()]

    def visitGraph_stmt(self, ctx:gramaticaParser.Graph_stmtContext):
        x = self.visit(ctx.expr(0))
        y = self.visit(ctx.expr(1))
        if x is not None and y is not None:
            plt.plot(x, y)
            plt.show()
            return f"Graficado: ({x}, {y})"
        return None