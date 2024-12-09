# error_handler.py
class ErrorHandler:
    @staticmethod
    def log_error(message, line_number=None):
        full_error = f"[error] Line {line_number}: {message}" if line_number else f"[error] {message}"
        print(full_error)
        return full_error
