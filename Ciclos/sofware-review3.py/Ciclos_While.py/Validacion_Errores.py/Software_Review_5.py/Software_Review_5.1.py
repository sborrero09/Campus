cvendedores = int(input("Cantidad de vendedores: "))

total_comisiones = 0

for vendedores in range(1, cvendedores+1):
    print("Informació del vendedor #", vendedores)

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
                materias = "Matemáticas","Física","Química","Historia","Lengua"
            
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

    Total_ventas_vendedor = 0
    Total_comision_vendedor =0

    for ventas in range(1, cventas+1):
            print("Información del cliente #", ventas)



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
                        break
                except ValueError:
                        print(" Error. Código del cliente inválido. intente de nuevo")
                        input("Presione cualquier tecla para continuar...")
                
                    
            while True: 
                try:
                        tipov = int(input("Tipo de venta (1 = Contado , 2 = Cŕedito): "))
                        if tipov < 1  or tipo > 2:
                            print("Error. 1 = Contado , 2 = Cŕedito")
                            continue
                        break
                except ValueError:
                        print("Inválido")
                        input("Presione cualquier tecla para continuar...")
                    
            while True:
                try:
                    venta = int(input("Valor de la venta: "))
                    break
                except ValueError:
                    print(" Error. Número inválido. intente de nuevo")
                    input("Presione cualquier tecla para continuar...")
                    
                    vfinal = 0
                    
                    if tipov == 1 and tipo == 1:
                        vfinal = vfinal + (venta * 0.25)
                        
                    elif tipov == 2 and tipo == 1:
                        vfinal = vfinal + (venta * 0.20)
                        
                    elif tipov == 1  and tipo  == 2:
                        vfinal = vfinal + (venta * 0.15)
                        
                    elif tipov == 2 and tipo == 2:
                        vfinal = vfinal + (venta * 0.10)
                        
                    elif tipov == 1  and tipo == 3:
                        vfinal = vfinal + (venta * 0.20)
                        
                    else: 
                        tipov == 2 and tipov == 3 
                        vfinal = vfinal + (venta * 0.15)
                    
                    Total_ventas_vendedor += venta
                    Total_comision_vendedor += vfinal
                    
print(end = "-" *50)
print(f"Valor a pagar por comisión al vendedor {nom} es de: $ {Total_comision_vendedor}")
print(f"Valor total de ventas del vendedor {nom} es de: $ {Total_ventas_vendedor}")
print(end = "-" * 50)
    
total_comisiones += Total_ventas_vendedor

print(f"El valor total a pagar por comisiones de todos los vendedores es: ${total_comisiones:,.0f} ")
print("Fin del programa")