while True: 
    opcion = input("selecciona la actividad entre 1 al 7, con el 0 termina el programa: ")

    #Actividad 1:
    if opcion == "1":

        a = 10
        b = input("Introduce un número: ")
        result = a / b
        print(f"Resultado: {result}")
        #TypeError: b pide un numero pero es tipo string y no se puede dividir los tipos int y str

        numbers = [1, 2, 3]
        print(numbers[5])
        #IndexError: el indice 5 esta fuera del rango de la lista que llega al 2 

    #Actividad 2:
    elif opcion == "2":
    
        a = 10
        #Convertimos el input a numero
        b = int(input("Introduce un número: "))
        result = a / b
        print(f"Resultado: {result}")
        
        #Usamos un indice valido
        numbers = [1, 2, 3]
        print(numbers[2])

    #Actividad 3:
    elif opcion == "3":

        a = 10
        #Agregue el try para que pueda ejecutarse
        try:
            b = input("Introduce un número: ")
            result = a / b
            print(f"Resultado: {result}")
        
        #Agregue el except para mostrar el error
        except TypeError:
            print("Error: no se puede dividir un tipo string con un numero")
        
        numbers = [1, 2, 3]
        #Agregue el try para que pueda ejecutarse
        try:
            print(numbers[5])

        #Agregue el except para mostrar el error
        except IndexError:
            print("Error: el indice 5 esta fuera del rango de la lista")

    #Actividad 4:
    elif opcion == "4":

        a = 10
        #Agregue el try para que pueda ejecutarse
        try:
            b = input("Introduce un número: ")
            result = a / b
            print(f"Resultado: {result}")
        
        #Agregue el except para mostrar el error
        except TypeError:
            print("Error: no se puede dividir un tipo string con un numero")

        except ZeroDivisionError:
            print("Error: no se puede dividir por cero")
        
        numbers = [1, 2, 3]
        #Agregue el try para que pueda ejecutarse
        try:
            print(numbers[5])

        #Agregue el except para mostrar el error
        except IndexError:
            print("Error: el indice 5 esta fuera del rango de la lista")


    elif opcion == "5":
         
         a = 10
        #Agregue el try para que pueda ejecutarse
         try:
            b = input("Introduce un número: ")
            result = a / b
            print(f"Resultado: {result}")
        
        #Agregue el except para mostrar el error
         except TypeError:
            print("Error: no se puede dividir un tipo string con un numero")

         except ZeroDivisionError:
            print("Error: no se puede dividir por cero")

         else:
            print('La ejecución fue exitosa.')

         finally:
          print("Fin del bucle.")
        
         numbers = [1, 2, 3]
        #Agregue el try para que pueda ejecutarse
         try:
            print(numbers[5])

        #Agregue el except para mostrar el error
         except IndexError:
            print("Error: el indice 5 esta fuera del rango de la lista")

        # Se ejecuta solo si no ocurrió ningún error
         else:
            print('La ejecución fue exitosa.')
        # Siempre se ejecuta, haya errores o no
         finally:
          print("Fin del bucle.")
        
        
    elif opcion == "6":
        
        
        try:
            #Pedimos un numero al usuario
            numero = int(input("Ingresa un numero: "))
            #Mostramos tu numero
            print(f"Tu numero es: {numero}")
                
            
        # Error si el usuario ingresa texto u otro valor no numérico
        except ValueError:
            print("Debe ingresar un número válido")

        #Sirve para algun error inesperado
        except Exception as e:
            print("Ocurrió el siguiente error: ", type(e).__name__ )

    elif opcion == "7":
        while True:
            try:
                #Pedimos un numero al usuario
                numero = int(input("Ingresa un numero: "))
                #Mostramos tu numero
                print(f"Tu numero es: {numero}")
                #Salimos del bucle si todo salio bien
                break
            
            # Error si el usuario ingresa texto u otro valor no numérico
            except ValueError:
                print("Debe ingresar un número válido")

            #Sirve para algun error inesperado
            except Exception as e:
                print("Ocurrió el siguiente error: ", type(e).__name__ )

    elif opcion == "0":
        break
