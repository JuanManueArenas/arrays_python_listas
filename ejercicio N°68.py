suma = 0
vector = [None]*5
# processing
for i in range(5):
    a = int(input("Dame un elemento: "))
    vector[i] = a
    suma += vector[i]
    
# output
print("La suma de los elementos del vector es:", suma)