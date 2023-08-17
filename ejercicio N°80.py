import random

b = []
c = []
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
        if M[i][j] % 2 == 0:
            b.append(M[i][j])
        else:
            c.append(M[i][j])

# output
print("Elementos pares de la matriz:", b)
print("Elementos impares de la matriz:", c)