
# 2. Cree una función que reciba una lista de palabras y un número n, y retorne una nueva lista con solo las palabras que tengan más de n letras
# Ejemplo: Entrada:  [ "cielo" , "sol" , "maravilloso" , "día" ] 
# "Ingrese el numero de letras minimas en la palabra: "  4
# Salida: [ "cielo" ,  "maravilloso" ]
word_list = [ "cielo" , "sol" , "maravilloso" , "día" ] 
def count_n_chars(word_list,length):
    new_list = []
    for word in word_list:
        if len(word) > length:
            new_list.append(word)
    return new_list


if __name__ == '__main__':
    print(count_n_chars(word_list, int(input("Ingrese el numero de letras minimas en la palabra: "))))