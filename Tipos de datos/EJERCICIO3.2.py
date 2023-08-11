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
print(f"Valor total pasajes:${vp:,.0f}")
print(f"Valor a pagar por concepto de pasajes:${liqp:,.0f}")
print(f"Valor total encomiendas:${ve:,.0f}")
print(f"Valor a pagar por concepto de encomiendas:${liqe:,.0f}")
print(f"Valor total a pagar al conductor:${vtotal:,.0f}")