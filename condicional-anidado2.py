# Condicional Anidado - Si quiero redondear tengo que escribir import math y luego math.ceil

import math

nom = input("Nombre del estudiante: ")
califc =  math.ceil(float(input("Ingrese la calificación cuantitativa (0-100): ")))

if califc < 0 or califc > 100:
    print("Error. Nota invalida")
elif califc < 60:
    ncual = "D"
elif califc < 80:
    ncual = "C"
elif califc < 90:
    ncual = "B"
else:
    ncual = "A"

print("Nombre:", nom)
print(f"Nota cuantitativa:{califc:,.1f}")
print(f"Nota Cualitativa:{ncual}")