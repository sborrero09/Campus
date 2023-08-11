asig = {}
while True:
    mat = input("Ingrese el nombre de la materia: ")    
    nota = int(input(f"Ingrese la nota de {mat} "))
    op = input("Desea continuar? Si/No: ")
    if op == "No":
        print("Gracias por usar el programa")
        break
for k, v in asig.items():
    print(f"En {k} has sacado {v}")