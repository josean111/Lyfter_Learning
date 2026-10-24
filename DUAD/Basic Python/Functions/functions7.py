#7
# 7. Cree una función que acepte una lista de números y retorne una lista con los números primos de la misma.
# [1, 4, 6, 7, 13, 9, 67] → [7, 13, 67]
# Tip 1: Investigue la lógica matemática para averiguar si un número es primo, y conviértala a código. No busque el código, eso no ayudaría.
# Tip 2: Aquí hay que hacer varias cosas (recorrer la lista, revisar si cada numero es primo, y agregarlo a otra lista). Así que lo mejor es agregar otra función para revisar si el numero es primo o no.
check_prime = [1, 4, 6, 0,-3, 7, 13, 9, 67]
def check_if_prime(num):
    counter = 0
    for i in range(1,num+1):
        if (num % i) == 0:
            counter += 1
    return counter == 2

def prime_number_list(check_prime):
    prime_only = []
    for number in check_prime:
        if check_if_prime(number):
            prime_only.append(number)
    return prime_only
#7
##########################################################################################################################################

if __name__ == '__main__':
    print(f"The original number list is {check_prime} but only this are prime numbers {prime_number_list(check_prime)}")