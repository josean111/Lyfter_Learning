# Cree un decorador @requires_login que:
# Verifique si la variable global user_logged_in es True
# Si no lo es, debe lanzar una excepción "Usuario no autenticado"
# Si lo es, la función decorada se ejecuta normalmente
# Ejemplo:
# Entrada:
# user_logged_in = False
# @requires_login
# def view_profile():
#     print("Mostrando perfil del usuario")
user_logged_in = False

def requires_login(func):
    def wrapper(*args, **kwargs):
        if not user_logged_in:
            raise ValueError("Usuario no autenticado")

        return func(*args, **kwargs)
    return wrapper

@requires_login
def view_profile():
    print("Mostrando perfil del usuario")

def main():
    try:
        view_profile()

    except ValueError as error:
        print(f"Error: {error}")

    global user_logged_in
    user_logged_in = True
    try:
        view_profile()

    except ValueError as error:
        print(f"Error: {error}")

if __name__ == "__main__":
    main()