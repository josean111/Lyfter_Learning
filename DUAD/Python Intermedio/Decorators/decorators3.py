# Cree una clase de User que:
# Tenga un atributo de date_of_birth.
# Tenga un property de age.
# Luego cree un decorador para funciones que acepten un User como parámetro que se encargue de revisar si el User es mayor de edad 
# y arroje una excepción de no ser así.
from datetime import date

class User:
    def __init__(self, date_of_birth):
        self.date_of_birth = date_of_birth

    @property
    def age(self):
        today = date.today()
        return ( today.year - self.date_of_birth.year - ((today.month, today.day) < (self.date_of_birth.month, self.date_of_birth.day)) )

def adult_only(func):
    def wrapper(user, *args, **kwargs):
        if user.age < 18:
            raise ValueError("User must be at least 18 years old")

        return func(user, *args, **kwargs)

    return wrapper

@adult_only
def access_account(user):
    print(f"Welcome! Your age is {user.age}")
    print("Access granted")

def main():
    adult = User(date(1995, 5, 10))
    minor = User(date(2015, 5, 10))

    try:
        access_account(adult)

    except (ValueError, TypeError) as error:
        print(f"Error: {error}")

    try:
        access_account(minor)

    except (ValueError, TypeError) as error:
        print(f"Error: {error}")

if __name__ == "__main__":
    main()