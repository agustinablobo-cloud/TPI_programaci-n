#Funcion para la carga inicial de herramientas
def carga_inicial(inventario):

    #Verificamo si el inventario ya tiene herramientas cargadas
    if len(inventario) > 0:
        print("\nYa existen herramientas cargadas")
        print("Para cargar nuevas herramientas utilice la opción 5")
        return
    
    #Solicita la cantidad de herramientas a cargar
    while True:
        try:
            can = input("\nIngresa la cantidad de herramientas a cargar: ")

            #Si esta vacio muestra el error
            if can == "":
                raise ValueError("No puede estar vacio")

            if not can.isdigit():
                raise ValueError("Debe ingresar un número entero")

            
            cantidad_a_cargar = int(can)

            if cantidad_a_cargar <= 0:
                    raise ValueError("La cantidad debe ser un numero mayor a 0")
            
            break
                    
        except ValueError as e:
            print(f"Error: {e}")
            


    #Cargar la herramientas
    contador = 0

    while contador < cantidad_a_cargar:
         
         while True:
            try:

            #Solicita y valida el nombre
                nombre = input(f"\nIngrese el nombre de la herramienta: ").strip()

                #Verifica que no este vacio
                if not nombre:
                    raise ValueError("El nombre no puede estar vacio")

                #Verifica que no este repetido
                for producto in inventario:
                    if producto["herramienta"].lower() == nombre.lower():
                        raise ValueError("Esta herramienta ya existe en el inventario")
                
                break
            
            except ValueError as e:
                print(f"Error: {e}")

                
         while True:
                
                try:
                    #Solicita y la valida el stock inicial        
                    sto = input("Ingrese la cantidad de la herramienta: ")

                    if sto == "":
                        raise ValueError("La cantidad no puede estar vacio")
                    
                    if not sto.isdigit():
                        raise ValueError("Debe ingresar un número entero")

                    
                    stock = int(sto)

                    if stock < 0:
                        raise ValueError("La cantidad inicial no puede ser negativo")
                    
                    break

                except ValueError as e:
                    print(f"Error: {e}")


        #Guarda la herramienta en el inventario
         nueva_herramienta = {
            'herramienta': nombre,
            'cantidad': stock}
         inventario.append(nueva_herramienta)

         contador += 1
            

         

#Visualizacion de inventario
def visualizacio_de_inventario(inventario):
    
    #Verificamos si el inventario esta vacio
    if not inventario:
        print("\nNo hay herramientas cargadas")
        return
    
    print("\n----------INVENTARIO----------")

    #Recorre la lista de inventario
    for producto in inventario:

        
        print(f"Herramienta: {producto['herramienta']}")
        print(f"Stock: {producto['cantidad']}")
        print("-----------------------------")

#Consulta de stock
def consulta_de_stock(inventario):

    #Verificamos si hay herramientas cargadas
    if not inventario:
        print("\nNo hay herramientas cargadas")
        return
    
    #Solicita el nombre a buscar
    buscar = input("Ingresa el nombre de la herramienta que desea buscar: ").strip().lower()

    #Recorre el inventario buscando la herramienta
    for producto in inventario:

        #producto["herramienta"] es el nombre
        if producto["herramienta"].lower() == buscar:

            #producto[cantidad] es el stock
            print(f"{producto['herramienta']}: {producto['cantidad']} unidades")
            return
        
    # Si termina el recorrido y no la encuentra
    print("La herramienta no se encuentra en el catalogo")    

#Reporte de agotados
def agotados(inventario):
    if not inventario:
        print("\nNo hay herramientas cargadas")
        return
    
    print("\n-------HERRAMIENTAS AGOTADAS-------")

    #Variable para saber si se encontro alguna herramienta agotada
    hay_agotadas = False

    #Recorre el inventario
    for producto in inventario:

        
        if producto["cantidad"] == 0:
            print(producto["herramienta"])
            hay_agotadas = True

    #Si no encontro ninguna herramienta agotada
    if not hay_agotadas:
        print("No hay herramientas agotadas")

#Alta de nuevo producto
def nuevo_producto(inventario):
    
    try:
        #Solicita el nombre de la herramienta
        nombre = input("Ingrese el nombre de la nueva herramienta: ").strip()

        #Verificamos que no este vacio
        if not nombre:
            raise ValueError("El nombre no puede estar vacio")
    
    
        #Verfica que no este cargado anteriormente
        for producto in inventario:
            if producto["herramienta"].lower() == nombre.lower():
                print("Error: la herramienta ya exite en el inventario")
                return

        #Solicita el stock del producto 
        sto = input("Ingresa el stock del producto: ").strip()

        if sto == "":
            raise ValueError("El stock no puede estar vacio")
        
        if not sto.isdigit():
            raise ValueError("Debe ingresar un número entero")

        
        stock = int(sto)

        #Verifica que no sea negativo
        if stock < 0:
            raise ValueError("El stock no puede ser negativo")
        
        inventario.append({'herramienta': nombre, 'cantidad': stock})
        print("Producto agregado con exito")
        
    except ValueError as e:
        print(f"Error: {e}")
        return
    

#Actualizacion de stock (venta/ingreso)
def actualizacion_de_stock(inventario):

    if not inventario:
        print("\nNo hay herramientas cargadas")
        return
    
    #Solicita el nombre de la herramienta
    nombre_buscar = input("Ingresa el nombre de la herramienta: ").strip().lower()

    #Busca la herramienta
    for producto in inventario:

        if producto["herramienta"].lower() == nombre_buscar.lower():

            try:
                print("1.Venta")
                print("2.Ingreso")

                opcion = input("seleccione una opcion: ")

                if opcion == "":
                    raise ValueError("Debe seleccionar una opcion")
                
                elif opcion not in ["1", "2"]:
                    raise ValueError("Opcion invalida")

                cantidad_ingresada = input("Ingrese la cantidad: ").strip()

                if cantidad_ingresada == "":
                    raise ValueError("La cantidad no puede estar vacia ")
                
                if not cantidad_ingresada.isdigit():
                    raise ValueError("Debe ingresar un número entero")

                
                cantidad = int(cantidad_ingresada)

                if cantidad <= 0:
                    raise ValueError("La cantidad debe ser mayor a 0")

                #Venta
                if opcion == "1":
                    
                    if producto["cantidad"] - cantidad < 0:
                        raise ValueError("Stock insuficiente")
                    producto["cantidad"] -= cantidad
                    print("Venta registrada")

                

                #Ingreso
                elif opcion == "2":

                    producto["cantidad"] += cantidad
                    print("Ingreso registrado")

                else:
                    print("Opcion invalida")
                return
            
            except ValueError as e:
                    print(f"Error: {e}")
                    return

                
                    
        
    #Si no encuentra la herramienta
    print("La herramienta no se encuentra")


#Menu principal
inventario = []   
opcion = 0
while opcion != 7:
        try:

            print("-----------Menu-----------")
            print("1. Carga de Herramientas")
            print("2. Visualización de Inventario")
            print("3. Consulta de Stock")
            print("4. Reporte de Agotados")
            print("5. Alta de Nuevo Producto")
            print("6. Actualización de Stock (Venta / Ingreso)")
            print("7. Salir")

        

            #Le pedimos a usuario que seleccione una opcion
            opcion = int(input("Seleccione un opción: "))

            if opcion == 1:
                carga_inicial(inventario)

            elif opcion == 2:
                visualizacio_de_inventario(inventario)

            elif opcion == 3:
                consulta_de_stock(inventario)

            elif opcion == 4:
                agotados(inventario)

            elif opcion == 5:
                nuevo_producto(inventario)

            
            elif opcion == 6:
                actualizacion_de_stock(inventario)



            elif opcion == 7:
                print("Saliendo del sistema")

            else:
                print("Opcion fuera del rango 1-7")

        except ValueError:
            print("Error: Ingrese un numero valido")