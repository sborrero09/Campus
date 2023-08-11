dia = int(input("Día: "))
mes = int(input("Mes: "))
año = int(input("Año: "))

if mes == 12 and dia == 31:
   mes = 1
   dia = 1
   año += 1
if mes == 1 or 3 or 5 or 7 or 8 or 10 and dia == 31:
    mes += 1
    dia = 1
if mes == 4 or 6 or 9 or 11 and dia == 30:
    mes += 0
    dia= 1
# if mes == 2 and dia == 28 and año % 100 == 0:
#      mes+= 1
#      dia= 1
# if mes == 2 and dia == 28 and año % 100 != 0:
#     dia= 29

# if mes == 2 and dia == 28 and año % 4 == 0 and año % 100 != 0 and año % 400 == 0:
#       mes += 0   
#       dia == 29
      
if año % 4 == 0:
    if año % 100 == 0 and año % 400 != 0:
            
        print("NO Es bisiesto")
    else:
        dia == 29
        print("es bisiesto")
        
else:
    print("No es bisiesto")

print(dia,mes,año)