resultado = 0
# input
n = int(input("Número de elementos de los vectores: "))

# processing
vector1 = [None] * n

print("Elementos del segundo vector:")
for i in range(n):
    print("Posición:", i)
    vector1[i] = int(input("Valor: "))

vector2 = [None] * n
print("Elementos del segundo vector:")
for i in range(n):
    print("Posición:", i)
    vector2[i] = int(input("Valor: "))
for i in range(n):
    producto += vector2[i]*vector1[i]

# output
print("Vector 1:", vector1)
print("Vector 2:", vector2)
print("El producto punto entre los dos vectores es:", resultado)