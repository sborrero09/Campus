def imprimirMat(m):
    for f in range(len(m)):
        for c in range(len(m[f])):
            print(m[f][c], end="\t")
    
def crearMatriz(fil, col):
    m = []
    for i in range(fil):
        c = [0] * col
        m.append(c) 