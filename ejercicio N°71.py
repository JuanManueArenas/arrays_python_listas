norma = 0
# input
n = int(input("Número de elementos del vector: "))
# processing
vector = [None] * n
for i in range(n):
    print("Posición:", i)
    vector[i] = int(input("Valor: "))
for i in range(n):
    norma = norma + vector[i]**2
norma = norma**0.5
# output
print("Vector generado:", vector)
print("La magnitud del vector es:", norma)