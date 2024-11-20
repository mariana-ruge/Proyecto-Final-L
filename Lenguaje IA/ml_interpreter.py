import sys
import math
import numpy as np
from antlr4 import *
from MLParser import MLParser
from MLListener import MLListener
from MLLexer import MLLexer

class MLInterpreter(MLListener):
    def __init__(self):
        self.variables = {}
        self.error_messages = []

    def _safe_eval(self, expression, context=None):
        """Safely evaluate mathematical expressions"""
        try:
            # Custom safe context with only essential math functions
            safe_context = {
                'math': math,
                'abs': abs,
                'round': round,
                'pow': pow,
                'max': max,
                'min': min
            }
            if context:
                safe_context.update(context)

            # Prevent direct access to built-ins
            return eval(expression, {"__builtins__": None}, safe_context)
        except ZeroDivisionError:
            self._log_error("Error matemático: División por cero")
            return float('inf')
        except Exception as e:
            self._log_error(f"Error de evaluación: {str(e)}")
            return None

    def _log_error(self, message):
        """Log and print error messages"""
        print(f"[error] {message}")
        self.error_messages.append(message)

    def exitArithmeticStatement(self, ctx:MLParser.ArithmeticStatementContext):
        """Handle arithmetic statements with error reporting"""
        try:
            result = self._safe_eval(ctx.expression().getText(), self.variables)
            if result is not None:
                print(f"Result: {result}")
        except Exception as e:
            self._log_error(f"Arithmetic error: {e}")

    def exitMatrixStatement(self, ctx:MLParser.MatrixStatementContext):
        """Handle matrix operations with robust error checking"""
        try:
            matrix_name = ctx.ID().getText()
            operation = ctx.matrixOperation()
            
            # Safely convert matrix arguments
            matrix_args = []
            for arg in operation.matrix():
                arg_value = self._safe_eval(arg.getText(), self.variables)
                if arg_value is None:
                    self._log_error(f"Could not evaluate matrix argument: {arg.getText()}")
                    return
                matrix_args.append(np.array(arg_value))
            
            # Matrix operation handling
            func = operation.matrixFunction().getText()
            try:
                if func == 'add' and len(matrix_args) == 2:
                    result = np.add(*matrix_args)
                elif func == 'subtract' and len(matrix_args) == 2:
                    result = np.subtract(*matrix_args)
                elif func == 'multiply' and len(matrix_args) == 2:
                    result = np.dot(*matrix_args)
                elif func == 'transpose' and len(matrix_args) == 1:
                    result = np.transpose(matrix_args[0])
                elif func == 'inverse' and len(matrix_args) == 1:
                    # Ensure square matrix for inverse
                    if len(matrix_args[0].shape) == 2 and matrix_args[0].shape[0] == matrix_args[0].shape[1]:
                        result = np.linalg.inv(matrix_args[0])
                    else:
                        self._log_error("Error: Inverse requires a square matrix")
                        return
                else:
                    self._log_error(f"Unsupported matrix operation: {func}")
                    return
                
                # Store and display result
                self.variables[matrix_name] = result.tolist()
                print(f"{matrix_name} = {result}")
            
            except Exception as e:
                self._log_error(f"Matrix operation error: {e}")
        
        except Exception as e:
            self._log_error(f"Matrix statement error: {e}")

    def exitConditionalStatement(self, ctx:MLParser.ConditionalStatementContext):
        """Handle conditional statements"""
        try:
            # Evaluate comparison expression
            left = self._safe_eval(ctx.comparisonExpression().expression(0).getText(), self.variables)
            right = self._safe_eval(ctx.comparisonExpression().expression(1).getText(), self.variables)
            op = ctx.comparisonExpression().compareOp().getText()
            
            # Perform comparison
            condition = {
                '==': left == right,
                '!=': left != right,
                '<': left < right,
                '<=': left <= right,
                '>': left > right,
                '>=': left >= right
            }[op]
            
            # Execute statements if condition is true
            if condition:
                for statement in ctx.statement():
                    self.visitChildren(statement)
        except Exception as e:
            self._log_error(f"Conditional statement error: {e}")

    def exitLoopStatement(self, ctx:MLParser.LoopStatementContext):
        """Handle loop statements with error checking"""
        try:
            if ctx.range():  # For loop with range
                start = int(ctx.range().NUMBER(0).getText())
                end = int(ctx.range().NUMBER(1).getText())
                var_name = ctx.variable().getText()
                
                for i in range(start, end + 1):
                    # Temporarily store loop variable
                    self.variables[var_name] = i
                    for statement in ctx.statement():
                        self.visitChildren(statement)
            
            elif ctx.comparisonExpression():  # While loop
                # Evaluate comparison expression
                left = self._safe_eval(ctx.comparisonExpression().expression(0).getText(), self.variables)
                right = self._safe_eval(ctx.comparisonExpression().expression(1).getText(), self.variables)
                op = ctx.comparisonExpression().compareOp().getText()
                
                # Determine loop condition
                condition = {
                    '==': left == right,
                    '!=': left != right,
                    '<': left < right,
                    '<=': left <= right,
                    '>': left > right,
                    '>=': left >= right
                }[op]
                
                # Execute loop while condition is true
                max_iterations = 100  # Prevent infinite loops
                iterations = 0
                while condition and iterations < max_iterations:
                    for statement in ctx.statement():
                        self.visitChildren(statement)
                    iterations += 1
        except Exception as e:
            self._log_error(f"Loop statement error: {e}")

    def exitFileStatement(self, ctx:MLParser.FileStatementContext):
        """Handle file operations"""
        try:
            if len(ctx.STRING()) == 2:  # Write operation
                filename = ctx.STRING(0).getText().strip('"')
                content = self._safe_eval(ctx.expression().getText(), self.variables)
                with open(filename, 'w') as file:
                    file.write(str(content))
                print(f"Written to {filename}")
            
            elif len(ctx.STRING()) == 1:  # Read operation
                filename = ctx.STRING(0).getText().strip('"')
                with open(filename, 'r') as file:
                    content = file.read()
                    print(f"File contents: {content}")
        except Exception as e:
            self._log_error(f"File operation error: {e}")

def main():
    if len(sys.argv) != 2:
        print("Usage: python ml_interpreter.py <script.txt>")
        return

    script_file = sys.argv[1]

    try:
        with open(script_file, 'r') as file:
            input_code = file.read()
        
        input_stream = InputStream(input_code)
        lexer = MLLexer(input_stream)
        stream = CommonTokenStream(lexer)
        parser = MLParser(stream)
        tree = parser.program()

        interpreter = MLInterpreter()
        walker = ParseTreeWalker()
        walker.walk(interpreter, tree)
    except Exception as e:
        print(f"Execution error: {e}")

if __name__ == '__main__':
    main()