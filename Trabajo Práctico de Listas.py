#Ejercicio 1:
'''
notas= [7,5,6,4,8,9,10,7,6,8]

print(f"las notas de 10 estudiantes: {notas} ")

prom = sum(notas)/len(notas)
print(f"promedio de las notas: {prom}")
print(f"la nota mas baja es: {min(notas)}")
print(f"la nota mas  alta es: {max(notas)}")
'''

#Ejercicio 2:
'''
productos = []
for i in range(5):
    producto= input("Por favor cargue 5 productos: ")
    productos.append(producto)

ord = sorted(productos)
print(f"lista de producto ordenada: {ord}")

elim=input(" qué producto desea eliminar?: ")
if elim in productos:
    productos.remove(elim)
    print(f"Lista actualizada: {productos}")
else:
    print("el producto no se encuentra en la lista")
'''

#Ejercicio 3:
'''

import random

numeros = []

for i in range(15):
    num = random.randint(1,100)
    numeros.append(num)

print(f"Lista de numeros: {numeros}")

par = []
impar = []

for num in numeros:
    if num % 2 == 0:
        par.append(num)
    else:
        impar.append(num)

print(f"Numeros pares: {par}")
print(f"Numeros impares: {impar}")

print(f"Cantidad de pares: {par}")
print(f"Cantidad de impares: {impar}")
'''
#Ejercicio 4:
'''
datos = [1, 3, 5, 3, 7, 1, 9, 5, 3]
sin_repetidos = []

for num in datos:
    if num not in sin_repetidos:
        sin_repetidos.append(num)

print(sin_repetidos)
'''

#Ejercicio 5:
'''
estudiantes = ["juan","carlos","ana","roberto","maria","nicolas","martina","lola"]

print(estudiantes)
nuevo = input("desea agregar un nuevo estudiante(responde con si o no): ")

if nuevo == "si" or nuevo == "SI":
    nuevo_estudiante = input("Ingrese el nombre del estudiante que desea agregar: ")
    estudiantes.append(nuevo_estudiante)
    print(estudiantes)

elim = input("Desea eliminar algun estudiante(responde con si o no): ")

if elim == "si" or elim == "SI":
    eliminar_estudiante = input("Ingrese el nombre del estudiante que desee eliminar: ")
    if eliminar_estudiante in estudiantes:
        estudiantes.remove(eliminar_estudiante)
    else:
        print("el estudiante no esta en la lista")
'''

#Ejercicio 6
'''
numeros = [2,1,6,5,7,3,4]

ultimo = numeros.pop()
numeros.insert(0, ultimo)

print(numeros)
'''

#Ejercicio 7: 
'''
temperatura = [
    [5,10],
    [7,14],
    [2,8],
    [9,20],
    [2,5],
    [10,23],
    [14,30]
]

suma_min = 0
suma_max = 0

for  dia in temperatura:
    suma_min += dia[0]
    suma_max += dia[1]

prom_min = suma_min / len(temperatura)
prom_max = suma_max / len(temperatura)

print(f"promedio minima: {prom_min}")
print(f"promedio maxiam: {prom_max}")

mayor_amplitud = 0
dia_mayor = 0

for i in range(len(temperatura)):
    amplitud  = temperatura[i][1] - temperatura[i][0]

    if amplitud > mayor_amplitud:
        mayor_amplitud = amplitud
        dia_mayor = i 

print(f"mayor amplitud termica en el dia: {dia_mayor + 1}")
'''

#Ejercicio 8:
'''
notas = [
    [10,8,9],
    [10,9,5],
    [3,7,2],
    [9,8,7],
    [5,6,4]
]

print("Promedio de cada estudiante: ")
for i in range(len(notas)):
    promedio = sum(notas[i]) / len(notas[i])
    print(f"estudiante {i+1}: {promedio}")
 

print("Promedio de cada materia: ")
for j in range(3):
    suma = 0
    for i in range(5):
        suma += notas[i][j]

    promedio = suma / 5
    print(f"materia {j+1}: {promedio}")
'''


#Ejercicio 9:
'''
# Crear tablero 3x3 con "-"
tablero = [
    ["-", "-", "-"],
    ["-", "-", "-"],
    ["-", "-", "-"]
]

def mostrar_tablero():
    for fila in tablero:
        print(" ".join(fila))
    print()

jugador = "X"

mostrar_tablero()

for turno in range(9):
    while True:
        print(f"Turno del jugador {jugador}")
        fila = int(input("Ingrese fila (0-2): "))
        col = int(input("Ingrese columna (0-2): "))

        # Validar jugada
        if tablero[fila][col] == "-":
            tablero[fila][col] = jugador
            break
        else:

            print("Casilla ocupada, intente de nuevo")

    # Mostrar SIEMPRE después de una jugada válida
    mostrar_tablero()

    # Cambiar jugador
    jugador = "O" if jugador == "X" else "X"

print("Juego terminado")
'''

#Ejercicio 10:

'''
ventas = [
    [10, 12, 8, 15, 9, 11, 14],   # Producto 1
    [7, 9, 10, 6, 8, 7, 9],       # Producto 2
    [5, 6, 7, 8, 9, 10, 11],      # Producto 3
    [20, 18, 22, 25, 19, 17, 21]  # Producto 4
]

productos = ["Pan", "Leche", "Queso", "Huevos"]

print("Total por producto:")
totales_productos = []

for i in range(len(ventas)):
    total = sum(ventas[i])
    totales_productos.append(total)
    print(productos[i], total)

mayor_venta = 0
dia_mayor = 0

for j in range(7):
    suma_dia = 0
    for i in range(4):
        suma_dia += ventas[i][j]
    
    if suma_dia > mayor_venta:
        mayor_venta = suma_dia
        dia_mayor = j

print("Día con mayores ventas:", dia_mayor + 1)


max_ventas = max(totales_productos)
producto_mas_vendido = totales_productos.index(max_ventas)

print("Producto más vendido:", producto_mas_vendido + 1)
'''

#Ejercicio 11:
'''
estudiantes = ["juan","carlos","ana","roberto","maria","nicolas","martina","lola","martin","jorge"]

nombre= input("ingrese el nombre que quiere buscar: ")

if nombre in estudiantes:
    print(f"el nombre si se encuentra {nombre}")
    posicion = estudiantes.index(nombre)
    print(f"el estudiante se encuentra en la posicion: {posicion+1}")
else:
    print("El nombre no se encuentra en la lista de estudiantes")
'''


#Ejericio 12:
'''
lista=[]
for i in range(8):
    numeros = int(input("ingrese 8 numeros: "))
    lista.append(numeros)
print(lista)

ordenado_mayor = sorted(lista)

print(f"Ordenado de mayor a menor: {ordenado_mayor}")

ordenado_menor = sorted(lista, reverse=True)
print(f"ordenado de menor a mayor: {ordenado_menor}")
'''

#Ejercicio 13:

puntaje = [450, 1200, 875, 990, 300, 1500, 640]

print(f"puntaje mas alto: {max(puntaje)}")
print(f"puntaje mas bajo: {min(puntaje)}")

ranking = sorted(puntaje, reverse=True)
print(f"Ranking: {ranking}")

posicion = ranking.index(990) + 1 
print(f"el puntaje 990 se encuentra en la posicion: {posicion}")
