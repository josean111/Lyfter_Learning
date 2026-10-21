# 2. Agrupar empleados por departamento
# Dada una lista de empleados donde cada uno tiene nombre, correo y departamento, cree un diccionario que agrupe los empleados por su departamento:
# Ejemplo: Entrada:
# employees = [
#     {"name": "Carlos", "email": "carlos@empresa.com", "department": "Ventas"},
#     {"name": "Ana", "email": "ana@empresa.com", "department": "TI"},
#     {"name": "Luis", "email": "luis@empresa.com", "department": "Ventas"},
#     {"name": "Sofía", "email": "sofia@empresa.com", "department": "RRHH"},
# ]

print("---- Agrupar empleados por departamento cree un diccionario que agrupe los empleados por su departamento: ----")
print("---- v1 ----")
employees = [
    {"name": "Carlos", "email": "carlos@empresa.com", "department": "Ventas"},
    {"name": "Ana", "email": "ana@empresa.com", "department": "TI"},
    {"name": "Luis", "email": "luis@empresa.com", "department": "Ventas"},
    {"name": "Sofía", "email": "sofia@empresa.com", "department": "RRHH"},
]
department = {}
#print(employees)
#print(employees.values())#["department"])
for emp in employees:
    department_val = emp["department"]
    if department_val not in department:
        department[department_val] = []
    department[department_val].append(emp)
#print(department)   
for dept, name in department.items():
    print(f"{dept}: {name}")
#v2
print("---- v2 ----")
department2 = {}
for emp in employees:
    department_val = emp["department"]
    department2.setdefault(department_val,[])
    department2[department_val].append(emp)
#print(department)   
for dept, employee in department2.items():
    print(f"{dept}: ")
    for emp in employee:
        print(f"    {emp["name"]}: {emp["email"]}")

