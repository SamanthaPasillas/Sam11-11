# encontrar mayor y menor

def maximo_manual(lista):
    if len(lista)== 0:
        return None
    maximo = lista[0]
    for num in lista[1:]:
        if num > maximo:
            maximo = num
    return maximo

def minimo_manual(lista):
    if len(lista) == 0:
        return None

    minimo = lista[0]

    for num in lista[1:]:
        if num < minimo:
            minimo = num

    return minimo

numeros = []
for i in range(8):
    valor = int(input(f"numero {i + 1}: "))
    numeros.append(valor)

mayor_manual = maximo_manual(numeros)
menor_manual = minimo_manual(numeros)

mayor_builtin = max(numeros)
menor_builtin = min(numeros)

print("Lista:", numeros)
print("Mayor (manual):", mayor_manual)
print("Menor (manual):", menor_manual)
print("Mayor (builtin):", mayor_builtin)
print("Menor (builtin):", menor_builtin)