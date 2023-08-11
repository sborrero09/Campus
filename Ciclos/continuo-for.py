for i in range(20):
    if i % 5 == 0:
        continue # El continue sirve para omitir un numero, en este caso no hace print 
                # de los multiplos de 5
    print(i, end=", ")