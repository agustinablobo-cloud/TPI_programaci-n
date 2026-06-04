# ============================================
# TPI - Gestion de Datos de Paises
# Programacion 1 - UTN
# ============================================

import csv

# --------------------------------------------
# FUNCION 1: Cargar paises desde el CSV
# --------------------------------------------
def cargar_paises(nombre_archivo):
    paises = []

    try:
        with open(nombre_archivo, "r", encoding="utf-8") as archivo:
            lector = csv.DictReader(archivo, delimiter=";")
        

            for fila in lector:
            
                pais = {
                    "nombre":     fila["nombre"],
                    "poblacion":  int(fila["poblacion"]),
                    "superficie": int(fila["superficie"]),
                    "continente": fila["continente"]
                }
                
                paises.append(pais)     

    except FileNotFoundError:
        print("Error: No se encontro el archivo")

    except ValueError as e:
       print(f"ValueError: {e} ")

    except KeyError:
       print("Error: Faltan columnas en el CSV")

    except Exception as e:
        print("Ocurrió el siguiente error: ", type(e).__name__ )

    return paises


# --------------------------------------------
# FUNCION 2: Guardar paises en el CSV
# --------------------------------------------

def guardar_paises(nombre_archivo, paises):

    with open(nombre_archivo, "w", newline="") as archivo:
       
       escritor = csv.writer(archivo)

       escritor.writerow(["nombre", "poblacion", "superficie", "continente"])

       for pais in paises:
          escritor.writerow([
             pais["nombre"],
             pais["poblacion"],
             pais["superficie"],
             pais["continente"]
          ])

def agregar_pais(paises):
    
    while True:
       try:
          
            nombre = input("Ingrese el nombre del pais: ").strip()

            if not nombre:
                raise ValueError("Error: el nombre no puede estar vacio")
        
            for pais in paises:
             if pais["nombre"].lower() == nombre.lower():
                raise ValueError("Error: el pais ya existe")
           
            break
       
       except ValueError as e:
          print(e)

    while True:
       try:
          poblacion = input("Ingresa la poblacion: ")

          if poblacion == "":
             raise ValueError("Error: no puede estar vacio")
          
          if not poblacion.isdigit():
             raise ValueError("Error: debe ingresar un numero entero")
          
          poblacion_a_cargar = int(poblacion)

          if poblacion_a_cargar <= 0:
             raise ValueError("Error: la poblacion debe ser mayor a 0")
          
          break
       
       except ValueError as e:
          print(e)


    while True:
       try:
          superficie = input("Ingresa la superficie en km²: " )

          if superficie == "":
             raise ValueError("Error: no puede estar vacio")
          
          if not superficie.isdigit():
             raise ValueError("Error: debe ingresar un numero entero")
          
          superficie_a_cargar = int(superficie)

          if superficie_a_cargar <= 0:
             raise ValueError("Error: la superficie debe ser mayor a 0")
          
          break
       
       except ValueError as e:
          print(e)
       

    while True:
       try:
            continente = input("Ingresa el continente: ").strip()

            if not continente:
                raise ValueError("Error: el continente no puede estar vacio")
        
            
            break
       
       except ValueError as e:
          print(e)

    nuevo_pais = {
        "nombre": nombre,
        "poblacion": poblacion_a_cargar,
        "superficie": superficie_a_cargar,
        "continente": continente
    }

    paises.append(nuevo_pais)

    guardar_paises("paises.csv", paises)

    print("Pais agregado correctamente")
          



def actualizar_pais():
   pass
   
def buscar_pais():
   pass

def filtrar_por_continente():
   pass

def filtrar_por_poblacion():
   pass

def filtrar_por_nombre():
   pass

def ordenar_por_nombre():
   pass

def ordenar_por_poblacion():
    pass

def ordenar_por_superficie():
    pass

def mostrar_estadisticas():
   pass


paises = cargar_paises("paises.csv")


#Deberia estar el menu 
