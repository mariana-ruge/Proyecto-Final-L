# recursion_control.py

import sys
from error_handler import ErrorHandler

class RecursionControl:
    def __init__(self, recursion_limit=1000):
        self.recursion_limit = recursion_limit
        self.recursion_depth = 0
        sys.setrecursionlimit(self.recursion_limit)

    def check_recursion_depth(self):
        if self.recursion_depth > self.recursion_limit:
            raise RecursionError(f"Recursion depth exceeded the limit of {self.recursion_limit}.")

    def recursive_for_loop(self, interpreter, var, start, end, step, statements):
        # Verifica si la profundidad de recursión ha sido superada
        if self.recursion_depth > self.recursion_limit:
            self.check_recursion_depth()

        if start < end:
            self.recursion_depth += 1
            interpreter.variables[var] = start
            interpreter._execute_statements(statements)
            self.recursion_depth -= 1
            self.recursive_for_loop(interpreter, var, start + step, end, step, statements)  # Recursión
        else:
            return

    def recursive_while_loop(self, interpreter, condition, statements):
        # Verifica si la profundidad de recursión ha sido superada
        if self.recursion_depth > self.recursion_limit:
            self.check_recursion_depth()

        if interpreter._safe_eval(condition):
            self.recursion_depth += 1
            interpreter._execute_statements(statements)
            self.recursion_depth -= 1
            self.recursive_while_loop(interpreter, condition, statements)  # Recursión
        else:
            return
