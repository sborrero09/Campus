contactos={}

cont = 0
while True:
    cont += 1
    nom = input(f"Digite el nombre del usuario # {cont} (o escriba 'NO' para terminar)")
    if nom.lower() == "no":
        break
    if nom in contactos:
        print("Nombre repetido")
        continue
    telefono = int(input("Digite el telefono: "))

    contactos[nom] = telefono

    for nom, telefono in contactos.items():
        print(f"Nombre: {nom}, Telefono: {telefono}")