# Dado una cantidad de segundos, indique cuantas horas, minutos y segundos restantes corresponde
seg = int(input("Ingrese segundos: "))
min = seg // 60 
hr = min // 60
segr = seg % 60
print("La cantidad de horas es:", hr)
print("La cantidad de minutos ", min)
print("La cantidad de segundos restantes es", segr)

