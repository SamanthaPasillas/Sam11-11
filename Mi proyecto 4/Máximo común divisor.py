# maximo comun divisor

import math

def mcd(a, b):
    a = abs(a)
    b = abs(b)

    if a == 0 and b == 0:
        return 0

    while b != 0:
        a, b = b, a % b

    return a

num1 = int(input("primer numero: "))
num2 = int(input("segundo numero: "))

resultado = mcd(num1, num2)
resultado_math = math.gcd(num1, num2)

print(f"MCD calculado: {resultado}")
print(f"MCD con math.gcd: {resultado_math}")
print("los resultados coinciden" if resultado == resultado_math else "no coinciden")

if num1 == 0 and num2 == 0:
    print("caso especial: ambos numeros son cero")
else:
    print("programa terminado")