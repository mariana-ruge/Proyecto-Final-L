import math

class Evaluator:
    def __init__(self, variables):
        self.variables = variables

    def _safe_eval(self, expression, context=None):
        try:
            safe_context = {
                'math': math,
                'abs': abs,
                'round': round,
                'pow': pow,
                'max': max,
                'min': min,
                'range': range
            }

            full_context = {**safe_context, **self.variables}

            if context:
                full_context.update(context)

            if expression:
                result = eval(expression, {"__builtins__": None}, full_context)
                return result
            else:
                return None
        except Exception as e:
            ErrorHandler.log_error(f"Evaluation error: {str(e)}")
            return None
