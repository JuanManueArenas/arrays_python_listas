mayor = -(100**10)
menor = 100**10
# input
n = int(input("Número de elementos: "))
# processing
vector = [None]*n
for i in range(n):
    print("Posición", i)
    vector[i] = int(input("Valor: "))
    if vector[i] > mayor:
        mayor = vector[i]
        pos_mayor = i
    if vector[i] < menor:
        menor = vector[i]
        pos_menor = i
        
# output
print("Valor del mayor:", mayor)
print("Posición del mayor:", pos_mayor)
print("Valor del menor:", menor)
print("Posición del menor:", pos_menor)