def leerEntero(msg):
    while True:
        try:
            num = int(input(msg))
            if n < 1:
                print("El número no puede ser menor a 1 ")
                input("Presione cualquier tecla para continuar...")
                continue
            break
        except ValueError:
            print("Número inválido.")
            input("Presione cualquier tecla para continuar...")
            
    return num

def leerNombre(msg):
     while True:
        try:
            nom = (input(msg))
            if nom == None or nom.strip() == "":
                print("El nombre no puede ser vacio.")
                input("Presione cualquier tecla para continuar...")
                continue
            break
        except Exception as e:
            print("Nombre inválido.", e)
            input("Presione cualquier tecla para continuar...")
            
    return nom

n = leerEntero("Cantidad abonados: ")
valtot = 0
for i in range(1, n+1):
    print("\nAbonado #", i)
    nombre = leerNombre("Nombre: ")
    est = leerEstrato("Estrato: ")
    imp = leerImpulsos("Cantidad Impulso: ")
    tbas = tarifabasica(est)
    valimp = calcularImpulsos(imp)
    
    mostrarValPagar(nombre, tbas, valimp)
    valtot += tbas + valimp
    
print(f"\nValor total a pagar: ${valtot:,.of}")
    