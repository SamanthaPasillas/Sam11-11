#convertir a mayuscula

def main():
    contador = 0

    while True:
        entrada = input("palabra o numero(espacio termina): ")

        if entrada == " ":
            break

        try:
            if entrada.isdigit():
                entrada = str(entrada)

            print(entrada.upper())
            contador += 1

        except Exception as e:
            print("Error:", e)

    print("programa terminado")
    print("cantidad de palabras procesadas:", contador)

main()