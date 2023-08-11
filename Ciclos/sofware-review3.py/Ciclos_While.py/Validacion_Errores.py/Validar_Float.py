while True:
    try:
        n = float(input("Número: "))
        break
    except ValueError:
        print(" Error. Número real inválido. intente de nuevo")
        input("Presione cualquier tecla para continuar...")
    except Exception as e: # "except Exception as e:" abarca todo tipo de errores
        print("Ha sucedido un error: ", e)
        
print("\n El número que se digitó es: ", n)