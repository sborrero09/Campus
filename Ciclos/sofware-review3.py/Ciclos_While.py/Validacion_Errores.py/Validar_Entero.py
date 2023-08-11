while True:
    try:
        n = int(input("Número: "))
        break
    except ValueError:
        print(" Error. Número entero inválido. intente de nuevo")
        input("Presione cualquier tecla para continuar...")
        
print("\n El número que se digitó es: ", n)