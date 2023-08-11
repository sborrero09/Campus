# Hallar un promedio de notas (0 a 5.0) hasta que la nota 
# sea -1 o cualquiera otro número negativo 


sum = 0.0
nota = 0
cant = 0

while nota >= 0:
    while True:
        nota = float(input("Ingrese la nota: "))
        if nota > 5:
            print("Error. Ingre una nota de (0.0  a 5.0) o -1 para terminar")
            continue
        break
    if nota > 0:
        cant += 1
        sum += nota
prom = round(sum / cant, 1)
print(f"El promedio es: {prom:.1f}")
    