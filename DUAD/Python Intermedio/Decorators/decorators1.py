# Cree un decorador que haga print de los parámetros y retorno de la función que decore.
def show_info(func):
    def wrapper(*args, **kwargs):
        print(f"\nFunction: {func.__name__}")
        print(f"Parameters: {args}, {kwargs}")

        result = func(*args, **kwargs)

        print(f"Return: {result}")
        return result

    return wrapper

@show_info
def add_numbers(a, b):
    return a + b

def main():
    result = add_numbers(10, 20)

if __name__ == "__main__":
    main()