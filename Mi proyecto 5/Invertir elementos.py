# invertir elementos

def invertir_manual(lista):
    invertida = []

    for i in range(len(lista) - 1, -1, -1):
        invertida.append(lista[i])

    return invertida

numeros = []

for i in range(6):
    valor = int(input(f"numero {i + 10}: "))
    numeros.append(valor)

print("original:", numeros)

invertida = invertir_manual(numeros)
print("invertida:", invertida)