

while True:
    opcion = input("selecciona la actividad entre 1 al 6, con el 0 termina el programa: ")

    #Actividad 1:
    if opcion == "1":
        #Creamos el archivo productos.txt en modo de escribir con "w" y use with que cierra el archivo automaricamente
        with open("productos.txt", "w") as archivo:
            
            #Escribo los productos con el formato de nombre, precio, cantidad
            archivo.write("remera,20000,10\n")
            archivo.write("pantalon,50000,5\n")
            archivo.write("gorro,15000,12\n")

    #Actividad 2: 
    elif opcion == "2":

        #Abrimos el archivo en modo lectura "r"
        with open("productos.txt", "r") as archivo:

            #Recorremos cada linea del archivo
            for linea in archivo:
                #Eliminamos el salto de linea (\n) al final
                partes = linea.strip().split(",")
                
                #Limpiamos y separamos los datos
                nombre, precio, cantidad = partes

                #Muestra los datos
                print(f"Producto: {nombre} | Precio: ${precio} | Cantidad: {cantidad}")

    #Actividad 3:
    elif opcion == "3":
        #Primero le mostramos los productos guardados:
        with open("productos.txt", "r") as archivo:

            print("LISTA DE PRODUCTOS")
            for linea in archivo:
                #Eliminamos el salto de linea (\n) al final
                partes = linea.strip().split(",")
                
                #Limpiamos y separamos los datos
                nombre, precio, cantidad = partes

                #Muestra los datos
                print(f"Producto: {nombre} | Precio: ${precio} | Cantidad: {cantidad}")

        #Pedimos los datos del nuevo producto
        nombre = input("Ingresa nombre del producto: ")
        precio = input("Ingresa el precio: ")
        cantidad = input("Ingresa la cantidad: ")

        #Abrimos el archivo en modo agregado "a" para añadir informacion sin sobreescribir lo que ya existian
        with open("productos.txt", "a") as archivo:

            #Guardamos el nuevo producto en una nueva linea
            archivo.write(f"{nombre},{precio},{cantidad}\n")
        
        print("Producto agregado correctamente")

    #Actividad 4:
    elif opcion == "4":

        #creamos una lista vacia para guardar los productos 
        lista_productos = []

        #Abrimos el archivo en modo lectura
        with open("productos.txt", "r") as archivo:

            #Recorremos cada linea del archivo
            for linea in archivo:

                #Eliminamos el salto de linea (\n) al final
                partes = linea.strip().split(",")
                
                #Limpiamos y separamos los datos
                nombre, precio, cantidad = partes

                #Creamos un diccionario para el producto
                producto = {
                    "nombre": nombre,
                    "precio": float(precio),
                    "cantidad": int(cantidad)
                }

                #Agregamos el diccionario a la lista 
                lista_productos.append(producto)

        #Mostramos la lista completa
        for producto in lista_productos:
            print(producto)

    #Actividad 5:
    elif opcion == "5":

        #Pedimos al usuario que ingrese el nombre del producto que busca
        buscar = input("Ingresa el nombre del producto que busca: ")

        #Variable para saber si se encontro el producto
        encontrado = False

        #Recorremos la lista de producto
        for producto in lista_productos:

            #Comparamos el nombre ingresado con el nombre del producto
            if producto["nombre"].lower() == buscar.lower():

                #Mostramos los datos del producto
                print("\nProducto encontrado:")
                print(f"Nombre: {producto['nombre']}")
                print(f"Precio ${producto["precio"]}")
                print(f"Cantidad: {producto["cantidad"]}")

                encontrado = True
                break

            #Si no se encontro el producto 
        if not encontrado:
            print("Error: el producto no existe")

    
    #Actividad 6:
    elif opcion == "6":

        #Agrego la lista 
        lista_productos = []
        
        #Abrimos el archivo en modod escritura "w", esto borra el contenido anterior y escribe el nuevo
        with open("productos.txt", "w") as archivo:

            #Recorremos la lista de productos
            for producto in lista_productos:

                #Escribimos cada producto en una línea
                linea =  f"{producto["nombre"]},{producto["precio"]},{producto["cantidad"]}\n"
                archivo.write(linea)

        print("Productos guardados correctamente.")


    elif opcion == "0":
        break