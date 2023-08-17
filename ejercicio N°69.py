salarios = [None]*5
empleados = [None]*5
ps = 0
resultado = 0
# processing
for i in range(5):
    empleados[i] = input("Nombre de empleado: ")
    salarios[i] = int(input("Salario de empleado: "))
    ps += salarios[i]
ps = ps / 5
for i in range(5):
    if salarios[i] > ps:
        resultado += 1
# output
print("Número de empleados que ganan más del ps:", resultado)