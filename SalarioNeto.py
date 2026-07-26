# Salario Neto
Salario_bruto = float(input("Ingresar salario bruto: "))
Porcentaje_Impuestos = float(input("ingresas porcentaje de impuestos: "))
deducciones = float(input("ingresar el monto de deducciones: "))

# Calcular

Impuestos = Salario_bruto * (Porcentaje_Impuestos / 100)
Salario_Neto = Salario_bruto - Impuestos - deducciones

# Imprimir

print("El salario neto es: ", Salario_Neto)