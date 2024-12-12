class Condicionales:
    def __init__(self, interpreter):
        self.interpreter = interpreter

    def manejar_condicional(self, ctx):
        """
        Maneja las sentencias condicionales 'if', 'else if', y 'else'.
        """
        try:
            # Flag para rastrear si ya se ha ejecutado una rama
            branch_executed = False

            # Iteramos por todas las ramas condicionales
            for i in range(len(ctx.comparisonExpression())):
                # Condición y bloque de instrucciones actuales
                condition_expr = ctx.comparisonExpression(i).getText()
                instructions = ctx.statement(i).getText()

                # Depuración: Muestra las condiciones e instrucciones detectadas
                print(f"Condición {i}: {condition_expr}")
                print(f"Instrucciones {i}: {instructions}")

                # Si aún no se ha ejecutado ninguna rama
                if not branch_executed:
                    # Evaluar la condición
                    condition_result = self.interpreter._safe_eval(condition_expr)
                    
                    # Depuración: Muestra el resultado de la evaluación
                    print(f"Evaluando condición '{condition_expr}': {condition_result}")
                    
                    # Si la condición es verdadera
                    if condition_result:
                        # Depuración: Indica qué bloque se está ejecutando
                        print(f"Ejecutando bloque de instrucciones para condición {i}: {instructions}")
                        self.interpreter._execute_statements([instructions])
                        branch_executed = True

            # Si ninguna rama se ejecutó y hay un bloque 'else'
            if not branch_executed and len(ctx.statement()) > len(ctx.comparisonExpression()):
                # Ejecutar el bloque 'else' (último bloque)
                else_instructions = ctx.statement(len(ctx.comparisonExpression())).getText()
                print(f"Ejecutando bloque 'else': {else_instructions}")
                self.interpreter._execute_statements([else_instructions])

        except Exception as e:
            print(f"[error] Error en la evaluación del condicional: {e}")

