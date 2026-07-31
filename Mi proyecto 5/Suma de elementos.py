# Suma de elementos

def sumar_lista(lista):
    suma = 0

    for num in lista:
        suma += num

    return suma

numeros = []

for i in range(5):
    valor = int(input(f"ingrese numero {1 + 1}: "))
    numeros.append(valor)

total = sumar_lista(numeros)
total_sum = sum(numeros)

print ("suma con bucle:", total)
print("suma con sum():", total_sum)
