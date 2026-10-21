# Cree un programa que itere e imprima un string letra por letra de derecha a izquierda.
# Pista: investigue de que otras maneras se puede usar el range.
# Ejemplos:
# my_string = ‘Pizza con piña’ →
# a
# ñ
# i
# p

# n
# o
# c

# a
# z
# z
# i
# p

print("---- Cree un programa que itere e imprima un string letra por letra de derecha a izquierda. ----")
word = input("Dame una palabra: ")
word_list = []
counter = 0
#v1
print("---- v1 ----")
last_ind = len(word) - 1
while last_ind >= 0:
    print(word[last_ind])
    word_list.insert(counter,word[last_ind])
    last_ind -= 1
    counter += 1
print("---- v2 ----")
#v2
for i in word_list:
    print(i)
#v3 range
print("---- v3 ----")
for j in range(len(word)-1,-1,-1):
    print(word[j])