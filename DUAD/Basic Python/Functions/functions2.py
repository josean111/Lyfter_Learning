##########################################################################################################################################
#2
# 2. Experimente con el concepto de scope:
# Intente acceder a una variable definida dentro de una función desde afuera.
# Intente acceder a una variable global desde una función y cambiar su valor.
global_var = "Global"
def test_function():
    local_var = "Local"
    print(f"Dentro de la funcion soy una variable {local_var}")
    global global_var 
    global_var = "GLOBAL" 
    print(f"Dentro de la funcion soy una variable {global_var}")
#2
##########################################################################################################################################


if __name__ == '__main__':
    #print(f"Fuera de la funcion soy una variable {local_var}")  
    # #Traceback (most recent call last):
#   File "c:\Users\Admin\Desktop\Lyfter\Python\functions1.py", line 63, in <module>
#     print(f"Fuera de la funcion soy una variable {local_var}")
#                                                   ^^^^^^^^^
# NameError: name 'local_var' is not defined. Did you mean: 'global_var'?
    print(f"Fuera de la funcion soy una variable {global_var}")