# Construya un programa tal que lea un número entero N, muestre la cantidad de términos y el resultado
# de la siguiente serie: 1- 1/2 +1/3- 1/4 + ... + 1/n 

n = int(input("Número: "))

acum = 0

for i in range (1, n+1):
    if i % 2 == 0:
        acum = acum - 1/i
    else:
        acum = acum + 1/i
        
print("Cantidad de terminos: ", n)
print("Resultado de la serie: ", acum)
        
    
    



