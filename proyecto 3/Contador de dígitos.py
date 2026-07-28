# Contador de dígitos

numero = int(input("Ingrese un número: "))

if numero == 0:
    digitos = 1
else:
    digitos = 0
    if numero < 0:
        numero = abs(numero)
    while numero > 0:
        numero //= 10
        digitos += 1
print("el numero tiene", digitos, "digitos")