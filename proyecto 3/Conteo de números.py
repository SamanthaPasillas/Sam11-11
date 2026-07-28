# Conteo de números

positivos = 0
negativos = 0
ceros = 0

cantidad = int(input("¿Cuántos números ingresará?: "))
i = 1

while i <= cantidad:
    numero = float(input("Número: "))

    if numero > 0:
        positivos += 1
    elif numero < 0:
        negativos += 1
    else:
        ceros += 1

    i += 1

print("Positivos:", positivos)
print("Negativos:", negativos)
print("Ceros:", ceros)