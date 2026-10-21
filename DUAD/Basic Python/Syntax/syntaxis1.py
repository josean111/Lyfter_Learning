# 1. Experimente haciendo sumas entre distintos tipos de datos y apunte los resultados.
# Si le salen errores, no se asuste. Lealos e intente comprender qué significan.
# Los errores son oportunidades de aprendizaje.
# Por ejemplo:
# string + string → ?
# string + int → ?
# int + string → ?
# list + list → ?
# string + list → ?
# float + int → ?
# bool + bool → ?

print("---- Experimente haciendo sumas entre distintos tipos de datos y apunte los resultados ----")

str1 = "soy string 1"
str2 = "soy string 2"
num1 = 3
num2 = 3.0
bool1 = True
bool2 = False
meses1 = ["enero","febrero","marzo"]
meses2 = ["abril","mayo","junio"]
print("string " + "string")
print(f"La suma de {str1} y {str2} es {str1+str2}")
#print("hola "+ 3) 
##TypeError: can only concatenate str (not "int") to str
#print(num1 + str1 ) 
##SyntaxError: invalid syntax. Perhaps you forgot a comma? deje espacio entre num 1 error de nombre de variable
##TypeError: unsupported operand type(s) for +: 'int' and 'str'
##no se pueden sumar diferentes tipos de datos, no importa el orden
print(meses1 + meses2)
#print(str1 + meses1)
##TypeError: can only concatenate str (not "list") to str
print(1.0 + 2)
print(num1 +  num2)
print(bool1 + bool2)
print(bool2 + bool2)
print(bool1 + bool1)

#2