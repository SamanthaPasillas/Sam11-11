# Vocales o consonantes

vocales = "aeiouAEIOU"

while True:
    letra = input("Ingrese una letra (espacio para terminar): ")

    if letra == " ":
        break

    letra = letra.lower()
    if letra in vocales:
        print("Es una vocal.")
    else:
        print("Es una consonante.")