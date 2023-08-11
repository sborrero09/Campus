cvendedores = int(input("Cantidad de vendedores: "))

for vendedores in range(1, cvendedores+1):
    print("Informació de los vendedores", vendedores)

    while True:
        try:
            di = int(input("Documento de identidad: "))
            if di < 1:
                print("El número es inválido")
                input()
                continue
            break
        except ValueError:
            print(" Documento de indetidad inválido")
            input("Presione cualquier tecla para continuar...")
            
        
    while True:
        try:
            nom = input("Nombre: ")
            if nom == None or nom.strip() == "":
                print("Nombre inválido.")
                continue
            break
        except Exception as e: 
            print("Ha sucedido un error: ", e)
                
            
    while True: 
        try:
            tipo = int(input("Tipo de vendedor (1 = Puerta a puerta, 2 = Telemercado, 3 = Ejecutivo de ventas): "))
            if tipo < 1  or tipo > 3:
                print("Error. Digite 1= Puerta a puerta o 2 = Telemercado o 3 = Ejecutivo de ventas")
                continue
            break
        except ValueError:
                print("Inválido")
                input("Presione cualquier tecla para continuar...")
            
cventas = int(input("Cantidad de ventas: "))

for ventas in range(1, cventas+1):
    print("Informació de los clientes", ventas)



    while True:       
        try:
                nomc = (input("Nombre del cliente: "))
                if nom == None or nom.strip() == "":
                    input("Presione cualquier tecla para continuar...")
                    continue
                break
        except Exception as e: 
            print("Ha sucedido un error: ", e)
        
    while True:    
        try:
                codc = int(input("Código del cliente: "))
                    continue
                break
        except ValueError:
                print(" Error. Código del cliente inválido. intente de nuevo")
                input("Presione cualquier tecla para continuar...")
        
            
    while True: 
        try:
                tipov = int(input("Tipo de venta (1 = Contado , 2 = Cŕedito): "))
        except ValueError:
                print(" Error. Digite 1 = Contado o 2 = Cŕedito")
                input("Presione cualquier tecla para continuar...")
                break
    while True:
        try:
            venta = int(input("Valor de la venta: "))
            break
        except ValueError:
            print(" Error. Número entero inválido. intente de nuevo")
            input("Presione cualquier tecla para continuar...")