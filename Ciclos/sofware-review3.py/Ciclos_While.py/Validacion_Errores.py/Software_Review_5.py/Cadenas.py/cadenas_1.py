s = "yo soy tu padre"

print(s[7])
print(s[-8])
# s[7] = "s"

# Recorrido de la cadena por su indice
for i in range(len(s)): # len nos dice la longitud de la cadena
    print(s[i], end=", ")
   
print()  
# Recorrido de la cadena por sus elementos 
for elem in s:
    print(elem, end="-")