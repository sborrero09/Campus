# Condicional Anidado
nom = input("Nombre del estudiante: ")
califc = float(input("Ingrese la calificación cuantitativa (0-100): "))

if califc >= 0 and califc < 60:
    ncual = "D"
elif califc  >= 60 and califc < 80:
    ncual = "C"
elif califc  >= 80 and califc < 90:
    ncual = "B"
elif califc  >= 90 and califc <= 100:
    ncual = "A"
else: 
    print("Error. Nota inválida")
    ncual = ""
    
print("Nombre:", nom)
print(f"Nota cuantitativa:{califc:,.1f}")
print(f"Nota Cualitativa:{ncual}")