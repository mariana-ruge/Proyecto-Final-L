### ml_dsl_project/src/interpreter.py
# Intérprete principal que utiliza el patrón Visitor para ejecutar el DSL de aprendizaje automático

from antlr4 import *
from antlr.generated.MLDSLParser import MLDSLParser
from antlr.generated.MLDSLLexer import MLDSLLexer
from antlr.generated.MLDSLVisitor import MLDSLVisitor

class MLInterpreter(MLDSLVisitor):
    def __init__(self):
        super().__init__()
        self.model_registry = {}  # Diccionario para almacenar modelos ML

    # Implementación de visitantes para manejar cada nodo del árbol
    def visitProgram(self, ctx):
        try:
            for child in ctx.statement():
                self.visit(child)
        except Exception as e:
            print(f"Error ejecutando el programa: {e}")

    def visitModel_definition(self, ctx):
        try:
            model_name = ctx.ID().getText()
            print(f"Definiendo un nuevo modelo: {model_name}")
            for stmt in ctx.statement():
                self.visit(stmt)
        except Exception as e:
            print(f"Error al definir el modelo '{model_name}': {e}")

    def visitTrain_statement(self, ctx):
        try:
            model_name = ctx.ID().getText()
            if model_name in self.model_registry:
                print(f"Entrenando el modelo: {model_name}")
                # Aquí se debe llamar a la función train con datos específicos (X, y)
                # self.model_registry[model_name].train(X, y)
            else:
                print(f"Error: No se encontró el modelo '{model_name}'")
        except Exception as e:
            print(f"Error al entrenar el modelo '{model_name}': {e}")

    def visitEvaluate_statement(self, ctx):
        try:
            model_name = ctx.ID().getText()
            if model_name in self.model_registry:
                print(f"Evaluando el modelo: {model_name}")
                # Aquí se debe llamar a la función predict o similar
                # self.model_registry[model_name].predict(X)
            else:
                print(f"Error: No se encontró el modelo '{model_name}'")
        except Exception as e:
            print(f"Error al evaluar el modelo '{model_name}': {e}")

    def visitIf_statement(self, ctx):
        try:
            condition = self.visit(ctx.condition())
            if condition:
                print("Condición evaluada como verdadera, ejecutando bloque IF")
                for stmt in ctx.statement():
                    self.visit(stmt)
            elif ctx.ELSE():
                print("Condición evaluada como falsa, ejecutando bloque ELSE")
                for stmt in ctx.statement(1):
                    self.visit(stmt)
        except Exception as e:
            print(f"Error en la sentencia IF: {e}")

    def visitFor_statement(self, ctx):
        try:
            iterator = ctx.ID().getText()
            print(f"Iniciando bucle FOR con iterador: {iterator}")
            for stmt in ctx.statement():
                self.visit(stmt)
        except Exception as e:
            print(f"Error en la sentencia FOR con iterador '{iterator}': {e}")

    def visitFunction_definition(self, ctx):
        try:
            func_name = ctx.ID().getText()
            print(f"Definiendo función: {func_name}")
            for stmt in ctx.statement():
                self.visit(stmt)
        except Exception as e:
            print(f"Error al definir la función '{func_name}': {e}")

    def visitReturn_statement(self, ctx):
        try:
            value = self.visit(ctx.expression())
            print(f"Devolviendo valor: {value}")
        except Exception as e:
            print(f"Error en la sentencia RETURN: {e}")

    def visitCondition(self, ctx):
        try:
            left = self.visit(ctx.expression(0))
            right = self.visit(ctx.expression(1))
            operator = ctx.getChild(1).getText()
            if operator == '==':
                return left == right
            elif operator == '<':
                return left < right
            elif operator == '>':
                return left > right
        except Exception as e:
            print(f"Error evaluando la condición: {e}")

    def visitExpression(self, ctx):
        try:
            if ctx.INT():
                return int(ctx.INT().getText())
            elif ctx.FLOAT():
                return float(ctx.FLOAT().getText())
            elif ctx.ID():
                return ctx.ID().getText()  # En un caso real, deberíamos buscar el valor de la variable
            elif ctx.getChildCount() == 3:  # Expresión dentro de paréntesis
                left = self.visit(ctx.expression(0))
                right = self.visit(ctx.expression(1))
                operator = ctx.getChild(1).getText()
                if operator == '+':
                    return left + right
                elif operator == '-':
                    return left - right
                elif operator == '*':
                    return left * right
                elif operator == '/':
                    return left / right
        except Exception as e:
            print(f"Error evaluando la expresión: {e}")
