import random

suma = 0

M = []

# input
m = int(input("Filas de la matriz: "))
n = int(input("Columnas de la matriz: "))
# processing
for i in range(m):
    M.append([])
    for j in range(n):
        M[i].append(random.randint(1,9))

for k in range(m):
    for j in range(n):
        print(M[k][j], end=" ")
    print()

for i in range(m):
    for j in range(n):
        suma = suma + M[i][j]
# output
print("Suma de los elementos de la matriz:", suma)