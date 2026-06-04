herramientas = []
existencias = []

while True:
    cantidad = input("Ingresa la cantidad de herramientas a cargar: ").strip()

    if cantidad.isdigit():
        cantidad = int(cantidad)
        if cantidad > 0:
            break
        else: 
            print("Error: la cantidad debe ser mayor a 0")
    else:
        print("Error: debe ingresar un numero entero positivo")

i = 0

while i < cantidad:
    nombre = input("Ingresa el nombre de la herramienta: ").strip()

    if nombre == "":
        print("Error: el nombre no puede estar vacio")
    
    elif nombre in herramientas:
        print("Error: el nombre ya fue ingresado")
    
    elif nombre.isdigit():
        print("Error: el nombre no puede ser un numero")
    
    else:
        herramientas.append(nombre)
        i = i + 1



i = 0
while i < len(herramientas):
    cantidad_unidades = input("Ingrese la cantidad de unidades para " + herramientas[i] + ": ").strip()
    if cantidad_unidades.isdigit():
        existencias.append(int(cantidad_unidades))
        i = i +1 
    else:
        print("Error: los numeros deben ser enteros positivos")


while True:
    print("-----------Menu-----------")
    print("1.Visualización de Inventario")
    print("2.Consulta de Stock")
    print("3.Reporte de Agotados")
    print("4.Alta de Nuevo Producto")
    print("5.Actualización de Stock (Venta/Ingreso)")
    print("6.Salir")

    opcion = input("Seleccione una opcion: ").strip()

    if opcion == "1":
        print("Invetario completo:")
        i = 0
        while i < len(herramientas):
            print(herramientas[i], ": ", str(existencias[i]), "unidades")
            i = i + 1 

    elif opcion == "2":
        buscar = input("Ingresa el nombre de la herramienta que estas buscando: ")
        if buscar in herramientas:
            index = 0
            while index < len(herramientas):
                if herramientas[index] == buscar:
                    print(buscar, "tiene", str(existencias[index]), "unidaes")
                    break
                
                index = index + 1
        else:
            print("La herramienta no se encuentra en el inventario")


    elif opcion == "3":
        index = 0
        agotados = False
        while index < len(herramientas):
            if existencias[index] == 0:
                if not agotados:
                    print("Productos agotados:")
                    agotados = True
                print(herramientas[index])
            index = index + 1
        if not agotados:
            print("No hay productos agotados")

    elif opcion == "4":
        
        nuevo_herramienta = input("Ingresa la herramienta que desea agregar: ").strip()
        if nuevo_herramienta == "":
            print("Error: el nombre no puede estar vacio")
    
        elif nuevo_herramienta in herramientas:
            print("Error: el nombre ya fue ingresado")
            
        else:
            nueva_cantidad = input("Ingrese el stock de la herramienta: ").strip()
    
            if nueva_cantidad.isdigit():
                herramientas.append(nuevo_herramienta)
                existencias.append(int(nueva_cantidad))
                
            else:
                print("Error: la cantidad debe ser un numero enterto positivo")


    elif opcion == "5":
        producto = input("Ingresa el nombre de la herramienta: ").strip()

        if producto in herramientas:
            i = 0  

        
            while i < len(herramientas):
                if herramientas[i] == producto:

                    print("1. Venta")
                    print("2. Ingreso")
                    cual = input("Seleccione una opcion: ").strip()

                    if cual == "1" or cual == "2":

                        can = input("Ingrese la cantidad: ").strip()

                        if can.isdigit():
                            can = int(can)

                            if cual == "1":
                                if existencias[i] >= can:
                                   existencias[i] -= can
                                   print("Venta realizada")
                                else:
                                    print("Error: stock insuficiente")

                            else:
                                    existencias[i] += can
                                    print("Ingreso realizado")

                        else:
                            print("Error: debe ingresar un numero entero positivo")

                    else:
                        print("Opcion invalida")

                    break
                i = i + 1
        else:
            print("La herramienta no se encuentra en el inventario")
                       
    elif opcion == "6":
        break

    else:
        print("Opcion invalida")

        