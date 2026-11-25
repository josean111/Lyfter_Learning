# Cree una función que se llame multiply, la cual obtiene dos valores y los multiplica entre si
# A esta función se le debe combinar dos decoradores:
# @log_call: imprime el nombre de la función, los argumentos, fecha actual y el retorno
# @validate_numbers: revisa que todos los argumentos sean numéricos
# Ejemplo:
# Entrada:
# multiply(3, 4)
# Salida
# "func:multiply - args: 3, 4 - [2025-07-17 14:00:00.000000] - Resultado: 12"
# "Resultado 12"
from datetime import datetime

def validate_numbers(func):
    def wrapper(*args, **kwargs):
        for value in args:
            if not isinstance(value, (int, float)) or isinstance(value, bool):
                raise TypeError("All parameters must be numbers")

        for value in kwargs.values():
            if not isinstance(value, (int, float)) or isinstance(value, bool):
                raise TypeError("All parameters must be numbers")

        return func(*args, **kwargs)
    return wrapper

def log_call(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        arguments = ""
        for arg in args:
            arguments += str(arg) + ", "

        for key, value in kwargs.items():
            arguments += f"{key}={value}, "

        arguments = arguments.rstrip(", ")
        print(f"func:{func.__name__} - args: {arguments} - [{datetime.now()}] - Resultado: {result}")
        
        return result
    return wrapper

@log_call
@validate_numbers
def multiply(a, b):
    return a * b

def main():
    try:
        result = multiply(3, 4)
        print(f"Resultado {result}")
    except TypeError as error:
        print(f"Error: {error}")

if __name__ == "__main__":
    main()