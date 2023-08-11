#Ejercicio en clase
b = float(input("Ingrese la base: "))
h = float(input("Ingrese la altura: "))

a = b * h / 2

print("El area es:", a)
# f-string
print(f"El area es: {a:.3f}")
# funcion format()
print("El area es:{:.2f}".format(a))
# Si se le agrega una , a {:.2f} osea {:,.2f} nos da como resultaods un numero en miles (usado para cifras de dinero)
print("El area es:{:,.2f}".format(a))

