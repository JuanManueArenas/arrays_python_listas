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

for i in range(1, m-1):
    suma += M[i][0] + M[i][n-1]
for j in range(n):
    suma += M[0][j] + M[m-1][j]
    
print("Suma de los elementos periféricos de la matriz:", suma) # output