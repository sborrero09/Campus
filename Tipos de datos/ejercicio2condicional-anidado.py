num1 = int(input("Primer numero entero positivo o negativo: "))
num2 = int(input("Segundo numero entero positivo o negativo: "))
num3 = int(input("Tercer numero entero positivo o negativo: "))

# if num3 < num1 > num2:
#     pos1 = num1
# elif num3 > num1 > num2:
#     pos2 = num1
# elif num3 > num2 > num1:
#     pos3 = num1
# if num3< num2 > num1:
#     pos1 = num2
# elif num1 > num2 > num3:
#     pos2 = num2
# elif num3 > num1 > num2:
#     pos3 = num2
# if num1 < num3 > num2:
#     pos1 = num3
# elif num2 > num3 > num1:
#     pos2 = num3
# elif num3 > num2 > num3:
#     pos3 = num3

if num3 < num1 > num2:
     pos1 = num1
 elif num3 > num1 > num2:
     pos2 = num1
 elif num3 > num2 > num1:
    pos3 = num1
 if num3< num2 > num1:
     pos1 = num2
 elif num1 > num2 > num3:
     pos2 = num2
 elif num3 > num1 > num2:
     pos3 = num2
 if num1 < num3 > num2:
     pos1 = num3
 elif num2 > num3 > num1:
     pos2 = num3
 elif num3 > num2 > num3:
     pos3 = num3


    

print(f"Mayor:,{pos1}:{pos2}:{pos3} ")
# print("En medio:,{pos1}:{pos2}:{pos3} ")
# print("Menor:,{pos1}:{pos2}:{pos3} ")
