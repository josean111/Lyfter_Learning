
#4
# 4. Cree una función que le dé la vuelta a un string y lo retorne.
# Esto ya lo hicimos en iterables.
# “Hola mundo” → “odnum aloH”
reverse_me = "Hola mundo"
def reverse_word(word):
    reversed_string = ""
    #temporary_str = "" #v1
    for letter in word:
        #temporary_str = reversed_string #v1
        reversed_string = letter + reversed_string
    return reversed_string
#4

if __name__ == '__main__':
    print(f"The word is {reverse_me} and in reverse is {reverse_word(reverse_me)}")