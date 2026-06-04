# ============================================
# TPI - Gestion de Datos de Paises
# Programacion 1 - UTN
# ============================================

#Libreria para manejar archivos CSV
import csv

# --------------------------------------------
# FUNCION 1: Cargar paises desde el CSV
# --------------------------------------------
def cargar_paises(nombre_archivo):

    #Lista donde se guardan todos los paises
    paises = []

    try:
        #Se abre el archivo CSV en modo lectura
        with open(nombre_archivo, "r", encoding="utf-8") as archivo:

            #DictReader convierte cada fila en un diccionario
            lector = csv.DictReader(archivo, delimiter=";")
        
            #Recorre cada fila del archivo
            for fila in lector:
                
                #Se crea un diccionario por pais
                pais = {
                    "nombre":     fila["nombre"],
                    #Convierte a entero
                    "poblacion":  int(fila["poblacion"]),
                    "superficie": int(fila["superficie"]),
                    "continente": fila["continente"]
                }
                
                #Agrega el pais a la lista
                paises.append(pais)     

    except FileNotFoundError:
        print("Error: No se encontro el archivo")

    except ValueError as e:
       print(f"ValueError: {e} ")

    except KeyError:
       print("Error: Faltan columnas en el CSV")

    except Exception as e:
        print("Ocurrió el siguiente error: ", type(e).__name__ )

    #Devuelve la lista de paises cargados
    return paises


# --------------------------------------------
# FUNCION 2: Guardar paises en el CSV
# --------------------------------------------

def guardar_paises(nombre_archivo, paises):

    #Se abre el archivo en modo escritura (sobrescribe el archivo)
    with open(nombre_archivo, "w", newline="") as archivo:
       
       escritor = csv.writer(archivo)

        #Se escribe encabezados
       escritor.writerow(["nombre", "poblacion", "superficie", "continente"])

        #Escribe cada pais como una fila
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
    
    #Validación del nombre
    while True:
       try:
          
            nombre = input("Ingrese el nombre del pais: ").strip()

            if not nombre:
                raise ValueError("El nombre no puede estar vacio")

            #Verifica duplicados
            for pais in paises:
             if pais["nombre"].lower() == nombre.lower():
                raise ValueError("El pais ya existe")
           
            break
       
       except ValueError as e:
          print(e)

    #Validación población
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

    #Validación superficie
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
       
    #Validación continente
    while True:
       try:
            continente = input("Ingresa el continente: ").strip()

            if not continente:
                raise ValueError("El continente no puede estar vacio")
        
            
            break
       
       except ValueError as e:
          print(e)

    #Se crea el nuevo pais
    nuevo_pais = {
        "nombre": nombre,
        "poblacion": poblacion_a_cargar,
        "superficie": superficie_a_cargar,
        "continente": continente
    }

    #El nuevo pais se agrega a la lista
    paises.append(nuevo_pais)

    #Se guarda en el CSV
    guardar_paises("paises.csv", paises)

    print("Pais agregado correctamente")
          
# --------------------------------------------
# FUNCION 4: Actualizar pais al CSV
# --------------------------------------------


def actualizar_pais(paises):

    #Busca el pais por nombre
    while True:
       try:
       
        nombre_buscado = input("Inrgese el nombre del pais a actulizar: ").strip()

        if not nombre_buscado:
           raise ValueError("El nombre buscado no puede estar vacio")
        
        break
       except ValueError as e:
          print(e)

    #Busca en la lista
    for pais in paises:
       
       if pais["nombre"].lower() == nombre_buscado.lower():
          
          #Actualiza la población
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

          
          #Actualiza la superficie
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

          #Guarda los cambios  
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
   
   #Se solicita el nombre o parte del nombre del pais a buscar
   nombre_buscar = input("Ingresa el nombre del pais que desea buscar: ").strip()

    #Validación que no puede estar vacio
   if not nombre_buscar:
      print("Error: el nombre no puede estar vacio")
      return
    
   encontrados = []
   
   #Recorre la lista de paises buscanod coincidencias parciales
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


# --------------------------------------------
# FUNCION 6: Filtrar por continente
# --------------------------------------------
   

def filtrar_por_continente(paises):
   
   continente_buscar = input("Ingresa el continente que desea buscar: ").strip()

   if not continente_buscar:
      print("Error: el continente no puede estar vacio")
      return
   
   encontrados = []

   #Filtra por los paises que coinciden con el continente ingresado
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
   
# --------------------------------------------
# FUNCION 7: Filtrar por población
# --------------------------------------------


def filtrar_por_poblacion(paises):

    #Se solicita rango minimo y maximo de población
    while True:
       try:
          minimo = input("Ingrese población minima: ").strip()
          maximo = input("Ingrese población maxima: ").strip()

          if not minimo or not maximo:
             raise ValueError("Los valores no pueden estar vacios")
            
          if not minimo.isdigit() or not maximo.isdigit():
             raise ValueError("Debe ingresar numeros enteros")
          
          #Conversión a enteros
          minimo_a_cargar = int(minimo)
          maximo_a_cargar = int(maximo)

          if minimo_a_cargar < 0 or maximo_a_cargar < 0:
             raise ValueError("Los valores no pueden ser menor a 0")
          
          if minimo_a_cargar > maximo_a_cargar:
             raise ValueError("El minimo no puede ser mayor que al maximo")
          
          break
       
       except ValueError as e:
          print(e)

    encontrados = []

    for pais in paises:
       
       if minimo_a_cargar <= pais["poblacion"] <= maximo_a_cargar:
          encontrados.append(pais)

    if len(encontrados) == 0:
       print("Error: no se encontraron paises en ese rango de población")
       return
    
    print("------------ RESULTADOS ------------")

    for pais in encontrados:
      print(f"Nombre: {pais['nombre']}")
      print(f"Población: {pais['poblacion']}")
      print(f"Superficies: {pais['superficie']}")
      print(f"Continente: {pais['continente']}")
   
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
opcion = 0
while opcion != "6":
   try:
      
      print("------------------- MENU -------------------")
      print("1. Agregar pais")
      print("2. Actualizar pais")
      print("3. Buscar pais")
      print("4. Filtrar por continente")
      print("5. Filtrar por población")
      print("6. Salir")

      opcion = input("Seleccione una opción (entre el 1 al 6): ").strip()

      if opcion == "1":
         agregar_pais(paises)

      elif opcion == "2":
         actualizar_pais(paises)

      elif opcion == "3":
         buscar_pais(paises)

      elif opcion == "4":
         filtrar_por_continente(paises)

      elif opcion == "5":
         filtrar_por_poblacion(paises)

      elif opcion == "6":
         print("Saliendo del sistema....")

      else:
         print("Opción fuera del rango 1-6")

   except ValueError:
      print("Ingresa un numero valido")
      

