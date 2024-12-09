class FileOperations:
    _operation_executed = False  # Variable de clase para gestionar la repetición

    @staticmethod
    def read_file(filename):
        if FileOperations._operation_executed:
            print(f"Operación de archivo ya ejecutada, se evita la repetición.")  # Depuración
            return None  # Evitar la ejecución

        try:
            with open(filename, 'r') as file:
                content = file.read()
                FileOperations._operation_executed = True  # Marcar operación ejecutada
                return content
        except FileNotFoundError:
            ErrorHandler.log_error(f"File not found: {filename}")
            return None
        except Exception as e:
            ErrorHandler.log_error(f"File operation error: {str(e)}")
            return None

    @staticmethod
    def write_file(filename, content):
        if FileOperations._operation_executed:
            print(f"Operación de archivo ya ejecutada, se evita la repetición.")  # Depuración
            return  # Evitar la ejecución

        try:
            with open(filename, 'w') as file:
                file.write(str(content))
                FileOperations._operation_executed = True  # Marcar operación ejecutada
        except Exception as e:
            ErrorHandler.log_error(f"File operation error: {str(e)}")
