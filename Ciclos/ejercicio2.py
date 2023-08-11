n = int(input("Cantidad de usuarios: "))

for usu in range(1, n+1):
    print("Información del usuario #: ", usu,)
    cod = int(input("\tCodigo: "))
    nom = input("\tNombre: ")
    est = input("\tEstado (V: Vigente o S: Suspendido")
    estr = int(input("\tEstrato (1 a 6): "))
    con = float(input("\tConsumo cm3: "))
    
    if est == "V" or  est == "v":
            
        if estr == 1:
            tb = 10000
        elif estr == 2:
            tb = 20000
        elif estr == 3:
            tb = 30000
        elif estr == 4:
            tb = 45000
        elif estr == 5:
            tb = 60000
        elif estr == 6:
            tb = 70000
        
    valcon = 200 * con
    vser = tb + valcon
        
    
    print("\n\t", "-" * 30)
    print("\tNombre:", nom)
    print(f"\tTarifa básica: $ {tb:,.0f}")
    print(f"\tValor del consumo del mes es: $ {valcon:,.0f}")
    print(f"\tValor a pagar por el servicio del mes es: $ {vser:,.0f}")


       
