while True:
    opcion = input("selecciona la actividad entre 1 al 10, con el 0 termina el programa: ")
    
    #Actividad 1
    if opcion == "1":
        def imprimir_hola_mundo():
            print("Hola Mundo!")
        imprimir_hola_mundo()

    #Actividad 2
    elif opcion == "2":
        def saludar_usuario(nombre):
            return f"Hola {nombre}!"
        nombre = input("Ingresa tu nombre: ")
        saludo = saludar_usuario(nombre)
        print(saludo)

    #Actividad
    elif opcion == "3":
        def  informacion_personal(nombre, apellido, edad, residencia):
            return f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}"
        
        nombre = input("Ingresa tu nombre: ")
        apellido = input("Ingresa tu apellido: ")
        edad = input("Ingresa tu edad: ")
        residencia = input("Ingresa tu residencia: ")
        informacion = informacion_personal(nombre, apellido, edad, residencia)
        print(informacion)

    #Actividad 4:
    elif opcion == "4":
        import math
        def calcular_area_circulo(radio):
            return math.pi * radio**2
        
        def calcular_perimetro_circulo(radio):
            return 2 * math.pi * radio
        
        radio = float(input("Ingresá el radio: "))

        area = calcular_area_circulo(radio)
        perimetro = calcular_perimetro_circulo(radio)

        print(f"Área del círculo: {area}")
        print(f"Perímetro del círculo: {perimetro}")


    #Actividad 5:
    elif opcion == "5":
        def segundos_a_horas(segundos):
            return segundos / 3600
        
        segundos = int(input("Ingresa segundos: "))
        horas = segundos_a_horas(segundos)
        print(f"tus segundos: {segundos} a horas: {horas}")

    #Actividad 6:
    elif opcion == "6":
        def tabla_multiplicar(numero):
            for i in range(1, 11):
                print(f"{numero} x {i} = {numero * i}")
        
        numero = int(input("Ingresá un número: "))
        tabla_multiplicar(numero)


    #Actividad 7:
    elif opcion == "7":
        def operaciones_basicas(a, b):
            suma = a + b
            resta = a - b
            multiplicacion = a * b

            if b != 0:
                division = a / b
            else:
                division = None
            return (suma, resta, multiplicacion, division)
        a = float(input("Ingresá el primer numero: "))
        b = float(input("Ingresá el segundo numero: "))

        
        resultados = operaciones_basicas(a, b)

        print("Suma:", resultados[0])
        print("Resta:", resultados[1])
        print("Multiplicacion:", resultados[2])

        if resultados[3] is not None:
            print("División:", resultados[3])
        else:
            print("División: no se puede dividir por cero")

    #Actividad 8:
    elif opcion == "8":
        def calcular_imc(peso, altura):
            return peso / (altura**2)
        
        peso = float(input("Ingresa tu peso(kg): "))
        altura = float(input("Ingresa tu altura(m): "))
        imc = calcular_imc(peso, altura)
        print(f"Tu IMC es: {imc}")


    #Actividad 9:
    elif opcion == "9":
        def celsius_a_fahrenheit(celsius):
            return (9/5) * celsius + 32
        
        celsius = float(input("Ingresa la temperatura en celsius: "))
        fahrenheit = celsius_a_fahrenheit(celsius)
        print(f"grados de celsius {celsius} a fahrenheit {fahrenheit} ")
        

    elif opcion == "10":
        def calcular_promedio(a, b, c):
            return (a + b + c) / 3
        
        a = float(input("Ingresa el primer numero: "))
        b= float(input("Ingresa el segundo numero: "))
        c= float(input("Ingresa el tercer numero: "))
        promedio = calcular_promedio(a, b, c)
        print(f"el promedio es: {promedio}")

    elif opcion == "0":
        break