
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

if m == n:
    for i in range(m):
        for j in range(n):
            if i + j == m-1:
                suma = suma + M[i][j]

    print("Suma de los elementos de la diagonal secundaria: ", suma) # output
else:
    print("No existe una diagonal secundaria") # output