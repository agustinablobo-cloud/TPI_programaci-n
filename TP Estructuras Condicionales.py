#Actividad 1:
'''
edad = int(input("ingrese su edad:"))

if edad > 18:
    print("Es mayor de edad")
'''


#Actividad 2:
'''
nota = int(input("ingrese su nota:"))

if nota >= 6:
    print("Aprobado")
else:
    print("Desaprobado")
'''


#Actividad 3:
'''
numero = int(input("ingrese un numero par:"))

if numero %2 == 0:
    print("Ha ingresado un número par")
else:
    print("Por favor, ingrese un número par")
'''


#Actividad 4:
'''
edad = int(input("ingrese su edad:"))

if edad < 12:
    print("Niño/a")
elif edad >= 12 and edad < 18:
    print("Adolescente")
elif edad >= 18 and edad < 30:
    print("Adulto/a joven")
else:
    print("Adulto/a")
'''


#Actividad 5:
'''
contraseña = input("introducir contraseñas de entre 8 y 14 caracteres: ")

if len(contraseña) >= 8 and len(contraseña) >= 14:
    print("Ha ingresado una contraseña correcta")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caractere")
'''


#Actividad 6:
'''
energia = float(input("ingrese el consumo mensual de energía eléctrica ne kilovatios(kWh): "))

if energia < 150:
    print("Consumo bajo.")
elif energia <= 300:
    print("Consumo medio")
else:
    print("Consumo alto")

if energia > 500:
    print("Considere medidas de ahorro energético")
'''


#Actividad 7:
'''
frase = input("ingrese una frase o palabra: ")

if frase[-1].lower() in "aeiou":
    print(f"{frase}!")
else:
    print(frase)
'''

#Actividad 8:
'''
nombre = input("ingrese su nombre: ")
print("1. Si quiere su nombre en mayúsculas")
print("2. Si quiere su nombre en minúsculas")
print("3. Si quiere su nombre con la primera letra mayúscula.")
opcion= int(input("ingrese 1, 2 o 3 para la opción que desee: "))

if opcion == 1:
    print(nombre.upper())
elif opcion == 2:
    print(nombre.lower())
elif opcion == 3:
    print(nombre.title())
'''


#Actividad 9:
'''
magnitud = float(input("ingrese la magnitud de un terremoto: "))

if magnitud < 3:
    print("Muy leve (imperceptible)")
elif magnitud >= 3 and magnitud < 4:
    print("Leve (ligeramente perceptible)")
elif magnitud >= 4 and magnitud < 5:
    print("Moderado (sentido por personas, pero generalmente no causa daños)")
elif magnitud >= 5 and magnitud <6:
    print("Fuerte (puede causar daños en estructuras débiles)")
elif magnitud >= 6 and magnitud < 7:
    print("Muy fuerte (puede causar daños significativos)")
else:
    print("Extremo (puede causar gravaes daños a gran escala)")
'''

#Actividad 10:
hemisferio =input("En cuál hemisferio se encuntra (N/S)")
dia = int(input("En que dia se encuentra: "))
mes = int(input("En que mes se encuentra: "))


if hemisferio == "N" or hemisferio == "n":
    if (mes == 12 and dia >= 21) or (mes in [1, 2]) or (mes == 3 and dia <= 20):
       
        print("usted se encuentra en invierno")

    elif (mes == 3 and dia >= 21 ) or (mes in [4,5]) or (mes == 6 and dia <= 20):
        
        print("usted se encuentra en primavera")
    
    elif (mes == 6 and dia >= 21) or (mes in [7,8]) or (mes == 9 and dia <= 20):
        print("usted se encuentra en verano")
    
    else: 
        print("usted se encuentra en otoño")

elif hemisferio == "S" or hemisferio == "s":
    if (mes == 12 and dia >= 21) or (mes in [1, 2]) or (mes == 3 and dia <= 20):
        print("usted se encuentra en verano")
    elif  (mes == 3 and dia >= 21 ) or (mes in [4,5]) or (mes == 6 and dia <= 20):
        print("usted se encuentra en otoño")
    elif (mes == 6 and dia >= 21) or (mes in [7,8]) or (mes == 9 and dia <= 20):
        print("usted se encuentra en invierno")
    else:
        print("usted se encuentra en primavera")