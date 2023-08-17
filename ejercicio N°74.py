import random
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
        print(M[k][j], end=" ") # output
    print()