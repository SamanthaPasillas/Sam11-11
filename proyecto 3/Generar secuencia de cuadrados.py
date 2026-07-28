# Secuencia de cuadrados

N = int(input("numero positivo: "))
i = 1
while True:
    print(i ** 2)
    i += 1
    if i > N:
        break
print("secuencia de cuadros hasta: ", N)