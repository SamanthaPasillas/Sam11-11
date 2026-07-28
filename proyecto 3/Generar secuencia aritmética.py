# Secuencia aritmética

inicio = int(input("primer numero: "))
diferencia = int(input("Diferencia: "))
limite = int(input("limite maximo: "))

numero = inicio

while True:
    print(numero, end=" ")
    numero += diferencia
    if numero > limite:
        break

print("\nSecuencia aritmetica desde", inicio, "hasta", limite)