# Ejercicio 3
nom = input("Nombre del conductor: ")
placa = input("Ingrese placa del vehículo: ")
vp = int(input("Ingrese el valor total por concepto de pasajes: "))
ve = int(input("Ingrese el valor tortal por concepto de encomiendas: "))

liqp = (vp / 100) * 25
liqe = (ve / 100) * 15
vtotal = liqp + liqe
print("Nombre:", nom)
print("Placa:", placa)
print("Valor total pasajes:${:,.f}", format(vp))
print("Valor a pagar por concepto de pasajes:${:,.f}", format(liqp))
print("Valor total encomiendas:${:,.f}", format(ve))
print("Valor a pagar por concepto de encomiendas:${:,.f}", format(liqe))
print("Valor total a pagar al conductor:${:,.f}", format(vtotal))



