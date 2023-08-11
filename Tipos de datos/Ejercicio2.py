# Ejercicio 2
nom = input("Nombre del estudiante: ")
nr1 = int(input("Ingrese nota del reto 1: 0 - 100 "))
nr2 = int(input("Ingrese nota del reto 2: 0 - 100 "))
nr3 = int(input("Ingrese nota del reto 3: 0 - 100 "))
ing = int(input("Ingrese nota de ingles: 0 - 100 "))


nota1 = (nr1 / 100) * 20
nota2 = (nr2 / 100) * 25
nota3 = (nr3 / 100) * 35
notaing = (ing / 100) * 20
calcdef= nota1 + nota2 + nota3  + notaing
print("La primera nota es:", nota1)
print("La segunda nota es:", nota2)
print("La tercera nota es:", nota3)
print("La cuarta nota es:", notaing)
print("La nota definitiva es:", calcdef)


