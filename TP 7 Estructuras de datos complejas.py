while True: 
    opcion = input("selecciona la actividad entre 1 al 10, con el 0 termina el programa: ")

    #Actividad 1:
    if opcion == "1":
        precios_frutas = {
            'Banana': 1200, 
            'Ananá': 2500, 
            'Melón': 3000, 
            'Uva': 1450}
        
        #Agrego frutas al diccionario
        precios_frutas["Naranja"] = 1200
        precios_frutas["Manzana"] = 1500
        precios_frutas["Pera"] = 2300 
     

    #Actividad 2:
    elif opcion == "2":
        precios_frutas = {
            'Banana': 1200, 
            'Ananá': 2500, 
            'Melón': 3000, 
            'Uva': 1450}
        
    
        precios_frutas["Naranja"] = 1200
        precios_frutas["Manzana"] = 1500
        precios_frutas["Pera"] = 2300 

        print(precios_frutas)

        #Actualizo los precios de las siguientes frutas
        precios_frutas["Banana"] = 1330 
        precios_frutas["Manzana"] = 1700
        precios_frutas["Melón"] = 2800


        print(precios_frutas)

    
    #Actividad 3:
    elif opcion == "3":
        precios_frutas = {
            'Banana': 1200, 
            'Ananá': 2500, 
            'Melón': 3000, 
            'Uva': 1450}
        
    
        precios_frutas["Naranja"] = 1200
        precios_frutas["Manzana"] = 1500
        precios_frutas["Pera"] = 2300 

        print(precios_frutas)

        
        precios_frutas["Banana"] = 1330 
        precios_frutas["Manzana"] = 1700
        precios_frutas["Melón"] = 2800

        print(precios_frutas)

        #La conversión de keys a una lista
        lista = list(precios_frutas)

        print(lista)


    #Actividad 4:
    elif opcion == "4":

        #Creamos el diccionario de contactos
        contactos = {}
        #Usamon for para pedir 5 veces al usuario los datos
        for n in range (5):
            #Le pedimos al usuario el nombre y numero
            nombre = input("Ingrese el nombre: ")
            numero = input("Ingrese el numero: ")

            #Agregamos el nombre y numero al diccionario de contactos
            contactos[nombre] = numero

        #Pedimos un nombre para buscar
        buscar = input("Ingrese el nombre que busca: ")

        ## Verificamos si existe
        if buscar in contactos:
            print(f"El numero es: {contactos[buscar]}")

        else:
            print("Error: el nombre no existe")


    #Actividad 5:
    elif opcion == "5":

        #Le pide al usuario que ingrese palabras
        palabra_unicas = input("Ingrese palabras: ")

        #Uso el split() para que separe el texto en palabras y las guarda en una lista
        texto = palabra_unicas.split()

        #set() elimina las palabras repetidas
        frases = set(texto)

        #Agregue un diccionario vacio para que guarde cada palabra y la cantidad de veces que aparece
        contador = {} 

        #Recorre cada palabra unica
        for palabra in frases:
            #count() cuenta cuanta veces aparece la palabra en la lista original
            contador[palabra] = texto.count(palabra)

        
        print(contador)



    elif opcion == "6":

        #Creamos un diccionario vacio para guardar las notas
        alumnos = {}

        #usamos for para pedir 3 veces el dato
        for n in range(3):

            #Pedimos el nombre del alumno
            nombre = input("Ingresa el nombre del alumno: ")

            #Pedimos la nota del alumno
            nota1 = float(input("Ingresa la primera nota: "))
            nota2 = float(input("Ingresa la segunda nota: "))
            nota3 = float(input("Ingrese la tercera nota: "))

            #Guradamos las notas en una tupla
            notas = (nota1, nota2, nota3)

            #Guradamos el alumno y sus notas en el diccionario
            alumnos[nombre] = notas

        #Recorremos el diccionario
        for nombre, notas in alumnos.items(): 

            #Calculamos el promedio
            promedio = sum(notas) / len(notas)

            print(f"{nombre} tiene promedio de: {promedio}")


    #Actividad 7:
    elif opcion == "7":

        #Creamos una lista de la asistencias con algunos nombres repetidos
        asistencias = ["juan", "ana", "pedro", "carlos", "juan", "pedro"]

        #Mostramos la lista original
        print("Lista original:")
        print(asistencias)


        #Creamos un set para eliminar repetidos
        empleados = set(asistencias)

        #Mostramos los empleados que asistieron al menos una vez
        print("Empleados que asistieron al menos una vez:")
        print(empleados)


        #Creamos un diccionario vacio para guardar cuantas veces asistieron
        contador = {}
        
        #Recorremos los empleados unicos
        for trabajadores in empleados:

            #Agregue count() para saber cuantas veces aparece el empleado en la lista original
            contador[trabajadores] = asistencias.count(trabajadores)

        print("Cantidad de asistencias:")
        
        #Recorre el diccionario contador y .items() devuelve la key y el value juntos
        for trabajadores, cantidad in contador.items():
            print(f"{trabajadores} asistio {cantidad} de veces")


    #Actividad 8:
    elif opcion == "8":

        #Creamos el diccionario con el nombre y el valor
        stock_ropa = {
            "remera" : 12,
            "pantalon" : 16,
            "zapatilla" : 20
        }

        print(stock_ropa)

        #Pedimos al usuario un producto
        producto = input("Ingrese un producto: ")

        #Verificamos si el producto existe
        if producto in stock_ropa:

            #Mostramos el stock actual
            print(f"Stock actual: {stock_ropa[producto]}")

            #Pedimos cuantas unidades desea agregar
            agregar = int(input("Ingrese las unidades que desea agregar: "))

            #Sumamos las unidades al stock 
            stock_ropa[producto] += agregar

            #Mostramos el nuevo stock
            print(f"Nuevo stock {stock_ropa[producto]}")

        
        else:
            #Si el producto no existe
            print("El producto no existe")

            #Pedimos el stock inicial del nuevo producto
            nuevo_stock = int(input("Ingresa el stock del nuevo producto: "))

            #Agregamos el nuevo producto al diccionario
            stock_ropa[producto] = nuevo_stock

            print("Producto agregado correctamente")

        print(stock_ropa)

    #Actividad 9:
    elif opcion == "9":
        #Creamos un diccionario para la agenda
        agenda = {
            ("lunes", "10:00") : "Reunion",
            ("martes", "17:00") : "Clase de programación",
            ("viernes", "20:00") : "Tomar la pastilla"
        }

        #Pedimos al usuario el dia
        dia = input("Ingresa un dia: ")

        #Pedimos la hora
        hora = input("Ingresa una hora: ")

        #Creamos una tupla con el dia y la hora
        consulta = (dia, hora)

        #Verficamos si esa tupla existe en el diccionario
        if consulta in agenda:
            print(f"Actividad: {agenda[consulta]}")

        else:
            print("No hay actividades programadas")


    #Actividad 10: 
    elif opcion == "10":

        #Creamos el diccionario original con pais : capital
        paises = {
            "Argentina" : "Buenos Aires",
            "Brasil" : "Brasilia",
            "Chile" : "Santiago"
        }

        print(f"original {paises}")

        #Creamos un diccionario vacio para guardar capital : pais
        capitales = {}

        #Recorremos el diccionario original
        for pais, capital in paises.items():

            #Invertimos key y value
            capitales[capital] = pais

        #Mostramos el el nuevo diccionario
        print(f"Invertido {capitales}")



    elif opcion == "0":
        break
