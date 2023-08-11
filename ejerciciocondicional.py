# Calcular la cantida dde digitos que tiene un numero entero positivo

# Ejemplo:
#     num:101
#     cantidad de digitos: 3

# Ejemplo 2 : 
#     num: 123456787
#     cantidad de digitos es: 9

num = int(input("Numero entero positivo: "))

if num  >= 0 and num < 10:
    cdig = "1"
elif num  >= 10 and num < 100:
     cdig = "2"
elif num  >= 100 and num < 1000:
     cdig = "3"
elif num  >= 1000 and num < 10000:
     cdig = "4"
elif num  >= 10000 and num < 100000:
     cdig = "5"
elif num  >= 100000 and num < 1000000:
     cdig = "6"
elif num  >= 1000000 and num < 10000000:
     cdig = "7"
elif num  >= 10000000 and num < 100000000:
     cdig = "8"
elif num  >= 100000000 and num < 1000000000:
     cdig = "9"pos
elif num  >= 10000000000 and num < 1000000000000:
     cdig = "11"

# if num  < 10:
#     cdig = "1"
# elif num < 100:
#     cdig = "2"
# elif num < 1000:
#     cdig = "3"
# elif num < 10000:
#     cdig = "4"
# elif num < 100000:
#     cdig = "5"
# elif num < 1000000:
#     cdig = "6"
# elif num < 10000000:
#     cdig = "7"
# elif num < 100000000:
#     cdig = "8"
# elif num < 1000000000:
#     cdig = "9"
# elif num < 10000000000:
#     cdig = "10"
# elif num < 1000000000000:
#     cdig = "11"
# else: 
#     print("Error. Nota inválida")
#     cdig = ""

print("Cantidad de digitos:", cdig)
