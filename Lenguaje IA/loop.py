from error_handler import ErrorHandler

MAX_RECURSION_DEPTH = 1000  # Límite de recursión para evitar desbordamientos

def exitForLoop(self, ctx):
    try:
        # Acceder a los nodos de manera segura y convertir a lista si es necesario
        children = list(ctx.getChildren())  # Convertir el generador en lista
        variable_name = children[1].getText()  # 'i'
        range_expr = children[3].getText()  # '0..10'

        # Obtener el inicio y fin del rango
        start, end = map(int, range_expr.split(".."))
        step = 1  # Valor predeterminado de step

        # Verificar si el 'step' está presente y extraer su valor correctamente
        if len(children) > 5:  # Si hay un 'step'
            step_expr = children[7].getText()  # Cambiar de children[5] a children[7] para obtener el valor correcto

            # Intentamos obtener el valor numérico de 'step' en vez de solo el texto "step"
            if step_expr.strip().isdigit():  # Si es un número directo
                step = int(step_expr.strip())
            else:
                # Si no es un número, intentamos evaluarlo
                step_value = self._safe_eval(step_expr)
                
                if step_value is None:
                    print("Step es None, utilizando valor predeterminado de 1.")
                    step = 1
                else:
                    step = step_value

        # Inicializar la variable
        self.variables[variable_name] = start

        # Ejecutar el bucle con el rango definido
        while self.variables[variable_name] <= end:
            # Imprimir la iteración
            print(f"{self.variables[variable_name]}")

            # Ejecutar las sentencias dentro del bucle
            for statement in ctx.statement():
                self.exitStatement(statement)

            # Incrementar la variable de control
            self.variables[variable_name] += step

    except Exception as e:
        ErrorHandler.log_error(f"Error in for loop execution: {e}")

def exitWhileLoop(self, ctx, iterations=0):
    try:
        # Obtener la expresión de la condición (por ejemplo, 'i < 5')
        condition = ctx.comparisonExpression().getText()

        # Limitar el número de iteraciones (evitar recursión infinita)
        if iterations >= MAX_RECURSION_DEPTH:
            print("Reached maximum recursion depth.")
            ErrorHandler.log_error(f"Maximum recursion depth reached in while loop.")
            return
        
        # Evaluar la condición de forma segura
        condition_result = self._safe_eval(condition)

        if not condition_result:  # Si la condición ya es falsa, terminamos la recursión
            return

        for statement in ctx.statement():
            self.exitStatement(statement)

        # Actualizar el valor de la variable de control 'i' (aquí incrementamos 'i')
        self.variables['i'] += 1  # Asegurándonos de que 'i' se incremente

        # Imprimir el valor de 'i' en cada iteración
        print(f"{self.variables['i']}")

        # Llamar recursivamente a la función
        self.exitWhileLoop(ctx, iterations + 1)
    
    except Exception as e:
        print(f"Error during while loop execution: {e}")
        ErrorHandler.log_error(f"Error in while loop execution: {e}")
