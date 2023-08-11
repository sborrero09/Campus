def msgError(msg):
    print(msg)
    input("Presione cualquier tecla para continuar ...")
    
def findEmpl(lstEmpl, id):
    for i in range(len(lstEmpl)):
        if id == lstEmpl[i][0]:
            return i
        
    return None

def buscarEmpleado(lstEmpl):
    print("\n\n*** 3. Buscar empleado - ACME ***\n")
    
    id = leerId("Id del empleado: ")
    pos = findEmpl(lstEmpl, id)
    if pos != None:
        print("\nNombre:", lstEmpl[pos][1])
        print("Horas trabajadas:", lstEmpl[pos][2])
        print(f"Valor Hora: ${lstEmpl[pos][3]:,.0f}")
    else:
        print("\nEl empleado no ha sido ingresado")
        
    input("Presione cualquier tecla para continuar ...")

def modificarEmpleado(lstEmpl):
    print("\n** 2. Modificar empleado **")
    id_modificar = int(input("Ingrese el ID del empleado a modificar: "))
    for i, empleado in enumerate(lstEmpl):
        if empleado["id"] == id_modificar:
            print(f"Empleado {empleado['nombre']} encontrado:")
            nuevo_nombre = input("Ingrese el nuevo nombre (o deje vacío para mantener el actual): ")
            if nuevo_nombre.strip():
                lstEmpl[i]["nombre"] = nuevo_nombre
            lstEmpl[i]["horas_trabajadas"] = ("nuevas horas trabajadas (entre 1 y 160)", 1, 160)
            lstEmpl[i]["valor_hora"] = ("nuevo valor de la hora (entre 8000 y 150000)", 8000, 150000)
            print("Empleado modificado exitosamente.\n")
            return
    print("Empleado no encontrado.\n")

def eliminarEmpleado(lstEmpl):
     print("\n** 4. Eliminar empleado **")
    id_eliminar = int(input("Ingrese el ID del empleado a eliminar: "))
    for empleado in (lstEmpl):
        if empleado["id"] == id_eliminar:
            lstEmpl.remove(empleado)
            print("Empleado eliminado exitosamente.\n")
            return
    print("Empleado no encontrado.\n")

def listarEmpleados(lstEmpl):
    print("\n** 5. Listar empleados **")
    if not lstEmpl:
        print("No hay empleados registrados.\n")
        return

    pag_actual = 0
    num_empleados = len(lstEmpl)
    while pag_actual < num_empleados:
        print("\nEmpleados:")
        for i in range(pag_actual, pag_actual + 5):
            if i >= num_empleados:
                break
            empleado = lstEmpl[i]
            print(f"ID: {empleado['id']}, Nombre: {empleado['nombre']}, Horas trabajadas: {empleado['horas_trabajadas']}, Valor de la hora: {empleado['valor_hora']}")
        
        opcion = input("Presione 'Enter' para continuar viendo empleados o 'M' para volver al menú: ")
        if opcion.strip().lower() == 'm':
            break

        pag_actual += 5


def listnomEmpleado(lstEmpl):
    print("\n** 6. Listar nómina de un empleado **")
    id_buscar = int(input("Ingrese el ID del empleado para calcular la nómina: "))
    for empleado in lstEmpl:
        if empleado["id"] == id_buscar:
            salario_bruto = empleado["horas_trabajadas"] * empleado["valor_hora"]
            salario_minimo_colombia = 908526  # Salario mínimo en Colombia para 2023, consulta la cifra actualizada.
            if salario_bruto < salario_minimo_colombia:
                subsidio_transporte = 106454  # Valor del subsidio de transporte en Colombia para 2023, consulta la cifra actualizada.
            else:
                subsidio_transporte = 0
            descuento_eps = salario_bruto * 0.04
            descuento_pension = salario_bruto * 0.04
            salario_neto = salario_bruto + subsidio_transporte - descuento_eps - descuento_pension

            print(f"ID: {empleado['id']}")
            print(f"Nombre: {empleado['nombre']}")
            print(f"Horas trabajadas: {empleado['horas_trabajadas']}")
            print(f"Valor de la hora: {empleado['valor_hora']}")
            print(f"Salario bruto: {salario_bruto}")
            print(f"Subsidio de transporte: {subsidio_transporte}")
            print(f"Descuento EPS (4%): {descuento_eps}")
            print(f"Descuento pensión (4%): {descuento_pension}")
            print(f"Salario neto: {salario_neto}\n")
            return
    print("Empleado no encontrado.\n")

def listnomEmpleados(lstEmpl):
    print("\n** 7. Listar nómina de todos los empleados **")
    if not lstEmpl:
        print("No hay empleados registrados.\n")
        return

    pag_actual = 0
    num_empleados = len(lstEmpl)
    while pag_actual < num_empleados:
        print("\nNómina de empleados:")
        for i in range(pag_actual, pag_actual + 5):
            if i >= num_empleados:
                break
            empleado = lstEmpl[i]

def leerValHora(msg):
    while True:
        try:
            n = int(input(msg))
            if n < 1:
                msgError("Error. Valor de las horas mayor que 0")
                continue
            return n
        except ValueError:
            msgError("Error. Valor de las Horas inválidas")
            continue

def leerHoras(msg):
    while True:
        try:
            n = int(input(msg))
            if n < 1:
                msgError("Error. Horas mayor que 0")
                continue
            return n
        except ValueError:
            msgError("Error. Horas inválidas")
            continue
        
def leerNom(msg):
    while True:
        try:
            n = input(msg)
            if n == None or n.strip() == "":
                print("Error Nombre inválido.")
                continue
            return n
        except Exception as e:
            print("Ha sucedido un Error: ", e)
            continue
        
def leerId(msg):
    while True:
        try:
            n = int(input(msg))
            if n < 1:
                msgError("Error. Id mayor que 0")
                continue
            return n
        except ValueError:
            msgError("Error. Id inválido")
            continue

def agregarEmpleado(lstEmpl):
    print("\n\n*** 1. Agregar empleado - ACME ***\n")
    
    id = leerId("Id del empleado: ")
    nom = leerNom("Nombre del empleado: ")
    hora = leerHoras("Horas trabajadas: ")
    valh = leerValHora("Valor de la Hora trabajada: ")
    
    datempl = [id, nom, hora, valh]
    lstEmpl.append(datempl) 
    # print(lstEmpl)
    # input()

def menu():
    while True:
        try:
            print("\n\n*** NOMINA ACME ***")
            print("\tMENU")
            print("1- Agregar empleado\n\
2- Modificar empleado\n\
3- Buscar empleado\n\
4- Eliminar empleado\n\
5- Listar empleados\n\
6- Listar nómina de un empleado\n\
7- Listar nómina de todos los empleados\n\
8- Salir\n")
            op = int(input("\t>> Escoja una opción (1-8)?"))
            if op < 1 or op > 8:
                msgError("Error. Opción Inválida (de 1 a 8).")
                continue
            return op
        except ValueError:
            msgError("Error. Opción Inválida (de 1 a 8).")
            continue
        
def main():
    lstEmpl = []
    while True:
        op = menu()
        if op == 1:
            agregarEmpleado(lstEmpl)
        elif op == 2:
            modificarEmpleado(lstEmpl)
        elif op == 3:
            buscarEmpleado(lstEmpl)
        elif op == 4:
            eliminarEmpleado(lstEmpl)
        elif op == 5:
            listarEmpleados(lstEmpl)
        elif op == 6:
            listnomEmpleado(lstEmpl)
        elif op == 7:
            listnomEmpleados(lstEmpl)
        elif op == 8:
            print("\n", "Gracias por usar el programa... Adios...".center(80))
            break
    

# Programa Principal
# main()