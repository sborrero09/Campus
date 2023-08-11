# Imprima los numeros pares del 2 al 50 incluyendo al 50

# for par in range(2, 51, 2):
#     print(par, end=", ")  # Al usar end=", " cambia la manera en que termina el print 

# Imprima los multiplos de 5 menores de 100

# for m in range(5, 100, 5):
#     print(m, end=", ")

# Indicar si un numero ingresado por el usuario es primo o no
n = int(input("Numero: "))

if n > 1:
    if n % 2 == 0:
        print("El número no es primo")
    else:
        esprimo = True
        for d in range(2, n):  
            if n % d == 0:
                esprimo = False
                break
                
        if esprimo == True:
            print("El número es primo") 
        else: 
            print("El número no es primo")

else:
    print("Error. Número inválido, deben ser mayores de 1") 
    