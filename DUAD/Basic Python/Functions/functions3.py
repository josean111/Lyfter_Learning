#3
# 3.Cree una función que retorne la suma de todos los números de una lista.
# La función va a tener un parámetro (la lista) y retornar un número (la suma de todos sus elementos).
# [4, 6, 2, 29] → 41
num_list = [4, 6, 2, 29] 
def list_sum(list_of_numbers):
    sum_num = 0
    for num in list_of_numbers:
        sum_num += num
    return sum_num
#3

print(f"The sum of this list {num_list} is {list_sum(num_list)}")