# Operador AND en ( P  q ) si p es False entonces (p  q) es falso si o si
# Operador OR em ( p v q) si p es True entonces (p v q) es verdaddero si o si
# Operador NOT
# Ejercicio Condicional simple

nom = input("Nombre del empleado: ")
salario = int(input("Ingrese salario del empleado: "))

if salario <= 1_200_000:
    aux = 120_000
else:
    aux = 0
    
print("Nombre:", nom)
print(f"Salario:${salario:,.0f}")
print(f"Auxilio de transporte:${aux:,.0f}")