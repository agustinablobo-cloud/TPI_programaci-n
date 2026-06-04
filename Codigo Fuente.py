def pedir_numero_positivo(mensaje):
    #Solicita un numero entero positivo, repite la solicitud hasta que el usuario ingrese un numero valido
    while True:
        try:
            numero = int(input(mensaje))

            if numero < 0:
                raise ValueError("La cantidad debe ser un numero mayor a 0")
            else: 
                return numero
            
            
            
        except ValueError:
            print("Error: debe ingresar un numero entero")

def pedir_nombre(mensaje):
    #Solicita un nombre que no este vacio y que no sea un numero

    while True:
        
        nombre = input(mensaje).strip()

        if nombre == "":
            raise ValueError("Error: el nombre no puede estar vacio")
            
        elif nombre.isdigit():
                raise ValueError("Error: el nombre no puede ser numero")
            
        else:
            return nombre
            
        
print("---------------------------------------")
print("-------- CALCULO DE CONJUNTOS ---------")
print("---------------------------------------")

#Universo
universo = pedir_numero_positivo("Ingresa la cantida total de elementos del universo: ")

#Nombre de los conjuntos
nombre_A = pedir_nombre("Ingresa el nombre del conjunto A: ")
nombre_B = pedir_nombre("Ingresa el nombre del conjunto B: ")
nombre_C = pedir_nombre("Ingresa el nombre del conjunto C: ")

#Cantidad de elementos de cada conjuntos
cantidad_A = pedir_numero_positivo(f"Inrgesa la cantidad de elemento de {nombre_A}: ")

cantidad_B = pedir_numero_positivo(f"Ingresa al cantidad de elemntos de {nombre_B}: ")

cantidad_C = pedir_numero_positivo(f"Ingresa la cantida de elemento de {nombre_C}: ")

#Interseccion A ∩ B
while True:
    interseccion_AB = pedir_numero_positivo(f"Ingresa la cantidad de elementos de {nombre_A} ∩ {nombre_B}: ")

    if interseccion_AB > cantidad_A or interseccion_AB > cantidad_B:
        print("Error: la interseccion A∩B no puede ser mayor que A o B ")
    else:
        break

#Interseccion A ∩ C
while True:
    interseccion_AC = pedir_numero_positivo(f"Ingresa la cantidad de elementos de {nombre_A} ∩ {nombre_C}: ")

    if interseccion_AC > cantidad_A or interseccion_AC > cantidad_C:
        print("Error: la interseccion A∩C no puede ser mayor que A o C")
    else:
        break

#Interseccion B ∩ C
while True:
    interseccion_BC = pedir_numero_positivo(f"Ingresa la cantidad de elemntos de {nombre_B} ∩ {nombre_C}: ")

    if interseccion_BC > cantidad_B or interseccion_BC > cantidad_C:
        print("Error: la interseccion B∩C no puede ser mayor que B o c")
    else:
        break

#Interseccion triple
while True:
    interseccion_ABC = pedir_numero_positivo(f"Ingresa la cantidad de elementos de {nombre_A} ∩ {nombre_B} ∩ {nombre_C}: ")

    if (interseccion_ABC > interseccion_AB or interseccion_ABC > interseccion_AC or interseccion_ABC > interseccion_BC):
        print("Error: la interseccion triple no peude ser mayor que las intersecciones dobles")
    else: 
        break

#Calculo de intersecciones exclusivas

solo_AB = interseccion_AB - interseccion_ABC
solo_AC = interseccion_AC - interseccion_ABC
solo_BC =interseccion_BC - interseccion_ABC

#Calculos de elementos exclusivos

solo_A = cantidad_A - solo_AB - solo_AC - interseccion_ABC
solo_B = cantidad_B - solo_AB - solo_BC - interseccion_ABC
solo_C = cantidad_C - solo_AC - solo_BC - interseccion_ABC

#Validacion final

if( solo_A < 0 or solo_B <0 or solo_C < 0 or solo_AB < 0 or solo_AC < 0 or solo_BC < 0):
    raise ValueError("Error: los datos ingresados son inconsistentes")

else:
    #Cantidad de elementos en al menso un cojunto
    union = (solo_A + solo_B + solo_C + solo_AB + solo_AC + solo_BC + interseccion_ABC)

    #Cantidad de elementos que no pertenecen a ningun conjunto
    ninguno = universo - union

    if ninguno < 0:
        raise ValueError("Erorr: la union de los conjuntos supera al universo")
    
    else:
        print("--------- RESULTADOS ---------")

        print(f"Solo {nombre_A}: {solo_A}")
        print(f"Solo {nombre_B}: {solo_B}")
        print(f"Solo {nombre_C}: {solo_C}")

        print(f"Solo {nombre_A} ∩ {nombre_B}: {solo_AB}")
        print(f"Solo {nombre_A} ∩ {nombre_C}: {solo_AC}")
        print(f"Solo {nombre_B} ∩ {nombre_C}: {solo_BC}")

        print(f"{nombre_A} ∩ {nombre_B} ∩ {nombre_C}: {interseccion_ABC}")

        print(f"Elementos que pertenecen al menos a un conjunto: {union}")
        print(f"Elementos que no pertenecen a ningún conjunto: {ninguno}")

