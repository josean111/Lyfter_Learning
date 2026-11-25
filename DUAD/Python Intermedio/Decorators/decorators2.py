# Cree un decorador que se encargue de revisar si todos los parámetros de la función que decore son números, y arroje una excepción de no ser así.
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

@validate_numbers
def multiply(*args):
    result = 1

    for number in args:
        result *= number

    return result

def main():
    try:
        print(multiply(2, 3, 4))

    except TypeError as error:
        print(f"Error: {error}")

    try:
        print(multiply(2, "hello", 4))

    except TypeError as error:
        print(f"Error: {error}")

    try:
        print(multiply(10, 20, 30.6))
    
    except TypeError as error:
        print(f"Error: {error}")

    try:
        print(multiply(5., 3, 6))
    
    except TypeError as error:
        print(f"Error: {error}")

    try:
        print(multiply(10, True, 30.6))
    
    except TypeError as error:
        print(f"Error: {error}")

if __name__ == "__main__":
    main()