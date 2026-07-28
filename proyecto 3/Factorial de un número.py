# Factorial de un número

numero = int(input("Ingrese un número: "))
factorial = 1
if numero < 0:
    print("Factorial no definido para negativos")
else:
    for i in range(1, numero + 1):
        factorial *= i

print("El factorial de:", numero, "es:", factorial)