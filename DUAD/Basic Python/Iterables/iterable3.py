# Cree un programa que intercambie el primer y ultimo elemento de una lista. Debe funcionar con listas de cualquier tamaño.
# Ejemplos:
# my_list = [4, 3, 6, 1, 7] → [7, 3, 6, 1, 4]

print("---- Cree un programa que intercambie el primer y ultimo elemento de una lista. Debe funcionar con listas de cualquier tamaño. ----")
first_list = [1,2,3,4,5]
print(f"Lista Inicial {first_list}")
#v1
print("---- v1 ----")
temp = first_list[0],first_list[len(first_list)-1]
first_list[0] = temp[1]
first_list[len(first_list)-1] = temp[0]
print(temp)
print(f"Lista Final {first_list}")
print("---- v2 ----")
#v2
second_list = [1,2,3,4,5]
temp_var = second_list[0]
print(f"Lista Inicial {second_list}")
print(temp_var)
second_list[0] = second_list[len(second_list)-1]
second_list[len(second_list)-1] = temp_var
print(f"Lista Final {second_list}")
#
print("---- v3 ----")
third_list = [1,2,3,4,5]
print(f"Lista Inicial {third_list}")
third_list[0],third_list[len(third_list)-1]=third_list[len(third_list)-1],third_list[0]
print(f"Lista Final {third_list}")
#Esto esta genial no lo sabia y aprendi algo nuevo me encanta este tipo de retos, asignacion multiple
