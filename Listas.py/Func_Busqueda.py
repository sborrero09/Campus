def findlist(lst, elem):
    #Encuentra el elemento y devuelve la posción 
    # o devuelve None si no lo encuentra
    for i in range(len(lst)):  
        if elem == lst[i]:
            return i
    return None

def existLst(lst, elem):
    # Devuelve True si existe
    # Devuelve False si no existe
    
    for e in lst:
        if elem == e:
            return True
    
    return False