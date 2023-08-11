#   En las variables tipo contador, se aplica la formula asi: variable = variable + 1 
# En las variables tipo sumador, se aplica la formula así: Variable: Variable + Neto_empleado

#Construya un programa que muestro los números divisibles de 3 y 7 entre 1 y 1000.

# for nd in range(1, 1001):
#     if nd % 3   == 0 and nd % 7 == 0:
#         print(nd, end = ", ")

# Calcular el promedio de n notas ingresadas por un docente



n = int(input("Cuantas notas son: "))

sumnotas = 0
for i in range(1, n+1):
    nota = float(input(f"Nota: {i} (0.0 a 5.0) "))
    sumnotas = sumnotas + nota
    
prom = round(sumnotas / n, 1)
print(f"El promedio entre las notas e: {prom:,.1f}")
