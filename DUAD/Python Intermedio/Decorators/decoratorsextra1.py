# Cree una función que imprima “Hola, [nombre]” dos veces:
# Cree un decorador @repeat_twice que haga que la función decorada se ejecute dos veces seguidas, con los mismos argumentos
# Ejemplo:
# Salida:
# "Hola, Jeanca"
# "Hola, Jeanca"
def repeat_twice(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result, result
    return wrapper

@repeat_twice
def say_hello(name):
    return f"Hola, {name}"

def main():
    for message in say_hello("Jeanca"):
        print(message)

if __name__ == "__main__":
    main()