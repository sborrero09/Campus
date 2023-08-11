while True:
    try:
        n = input("Nombre: ")
        if n == None or n.strip() == "":
            print("Nombre inválido.")
            continue
        break
    except Exception as e: # "except Exception as e:" abarca todo tipo de errores
        print("Ha sucedido un error: ", e)
        
print("\n El nombre que se digitó es: ", n)