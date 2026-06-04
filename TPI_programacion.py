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
# --------------------------------------------
# FUNCION 3: Agregar pais al CSV
# --------------------------------------------

def agregar_pais(paises):
    
    while True:
       try:
          
            nombre = input("Ingrese el nombre del pais: ").strip()

            if not nombre:
                raise ValueError("El nombre no puede estar vacio")
        
            for pais in paises:
             if pais["nombre"].lower() == nombre.lower():
                raise ValueError("El pais ya existe")
           
            break
       
       except ValueError as e:
          print(e)

    while True:
       try:
          poblacion = input("Ingresa la poblacion: ")

          if poblacion == "":
             raise ValueError("No puede estar vacio")
          
          if not poblacion.isdigit():
             raise ValueError("Debe ingresar un numero entero")
          
          poblacion_a_cargar = int(poblacion)

          if poblacion_a_cargar <= 0:
             raise ValueError("La poblacion debe ser mayor a 0")
          
          break
       
       except ValueError as e:
          print(e)


    while True:
       try:
          superficie = input("Ingresa la superficie en km²: " )

          if superficie == "":
             raise ValueError("No puede estar vacio")
          
          if not superficie.isdigit():
             raise ValueError("Debe ingresar un numero entero")
          
          superficie_a_cargar = int(superficie)

          if superficie_a_cargar <= 0:
             raise ValueError("La superficie debe ser mayor a 0")
          
          break
       
       except ValueError as e:
          print(e)
       

    while True:
       try:
            continente = input("Ingresa el continente: ").strip()

            if not continente:
                raise ValueError("El continente no puede estar vacio")
        
            
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
          
# --------------------------------------------
# FUNCION 4: Actualizar pais al CSV
# --------------------------------------------


def actualizar_pais(paises):

    while True:
       try:
       
        nombre_buscado = input("Inrgese el nombre del pais a actulizar: ").strip()

        if not nombre_buscado:
           raise ValueError("El nombre buscado no puede estar vacio")
        
        break
       except ValueError as e:
          print(e)

    for pais in paises:
       
       if pais["nombre"].lower() == nombre_buscado.lower():
          
          while True:
             try:

                poblacion = input("Ingresa la nueva poblacion: ")

                if not poblacion:
                   raise ValueError("La poblacion no puede estar vacio")
                
                if not poblacion.isdigit():
                   raise ValueError("Debe ingresar un numero entero")
                
                poblacion_a_cargar = int(poblacion)

                if poblacion_a_cargar <= 0:
                   raise ValueError("La poblacion debe ser mayor a 0")
                
                break
             
             except ValueError as e:
                print(e)


          while True:
             try:
                superficie = input("Ingrese la nueva superficie: ")

                if not superficie:
                   raise ValueError("Error: la superficie no puede estar vacio")
                
                if not superficie.isdigit():
                   raise ValueError("Debe ingresar un numero entero")
                
                superficie_a_cargar = int(superficie)

                if superficie_a_cargar <= 0:
                   raise ValueError("La superficie debe ser mayor a 0")
                
                break
             
             except ValueError as e:
                print(e)

          pais["poblacion"] = poblacion_a_cargar
          pais["superficie"] = superficie_a_cargar

          guardar_paises("paises.csv",paises)

          print("Pais actualizado correctamente")
          return
       
    print("No se encontro el pais")

             
# --------------------------------------------
# FUNCION 5: Buscar un pais
# --------------------------------------------
            
   
def buscar_pais(paises):
   
   nombre_buscar = input("Ingresa el nombre del pais que desea buscar: ").strip()

   if not nombre_buscar:
      print("Error: el nombre no puede estar vacio")
      return
    
   encontrados = []
   
   for pais in paises:
      
      if nombre_buscar.lower() in pais["nombre"].lower():
         encontrados.append(pais)

   if len(encontrados) == 0:
      print("Error: no se encontraron paises con ese nombre")
      return
   
   print("------------ RESULTADOS ------------")
   
   for pais in encontrados:
      print(f"Nombre: {pais['nombre']}")
      print(f"Población: {pais['poblacion']}")
      print(f"Superficies: {pais['superficie']}")
      print(f"Continente: {pais['continente']}")

   

def filtrar_por_continente(paises):
   
   continente_buscar = input("Ingresa el continente que desea buscar: ").strip()

   if not continente_buscar:
      print("Error: el continente no puede estar vacio")
      return
   
   encontrados = []

   for pais in paises:
      
      if pais["continente"].lower() == continente_buscar.lower():
         encontrados.append(pais)

   if len(encontrados) == 0:
      print("Error: no se encontraron paises en ese continente")
      return
   
   print("------------ RESULTADOS ------------")

   for pais in encontrados:
      print(f"Nombre: {pais['nombre']}")
      print(f"Población: {pais['poblacion']}")
      print(f"Superficies: {pais['superficie']}")
      print(f"Continente: {pais['continente']}")
   

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
