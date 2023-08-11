n = int(input("Ingrese telefono con formato (+codpais-num-ext): "))
part = n.split("-")

# part: [+codepais, num , ext] 
# Validar
if len(part) == 3 and part[0].startswith("+") and \
    len(part[0]) == 3 and part[0][1:].isdigit() and \
        part[1].isdigit() and len(part[2]) == 2 and \
            part[2].isdigit():
                print(part[1])
else:
    print("Formato inválido")