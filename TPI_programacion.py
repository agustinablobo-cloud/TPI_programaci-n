# TPI - Programacion I - Gestion de Datos de Paises

def cargar_paises(nombre_archivo):

    # Lista donde se guardan todos los paises
    paises = []

    try:
        # Se abre el archivo CSV en modo lectura
        with open(nombre_archivo, "r") as archivo:

            lineas = archivo.readlines()

            # Recorre cada fila del archivo (saltea el encabezado)
            for i in range(1, len(lineas)):

                linea = lineas[i].strip()
                datos = linea.split(",")

                pais = {
                    "nombre":     datos[0],
                    "poblacion":  int(datos[1]),   # Convierte a entero
                    "superficie": int(datos[2]),   # Convierte a entero
                    "continente": datos[3]
                }

                # Agrega el pais a la lista
                paises.append(pais)

    except FileNotFoundError:
        print("Error: No se encontro el archivo")

    except ValueError as e:
        print(f"ValueError: {e}")

    except IndexError:
        print("Error: Faltan columnas en el CSV")

    except Exception as e:
        print("Ocurrio el siguiente error: ", type(e).__name__)
        print(e)

    # Devuelve la lista de paises cargados
    return paises


# --------------------------------------------
# FUNCION 2: Guardar paises en el CSV
# --------------------------------------------
def guardar_paises(nombre_archivo, paises):

    # Se abre el archivo en modo escritura (sobrescribe el archivo)
    with open(nombre_archivo, "w") as archivo:

        # Se escribe el encabezado
        archivo.write("nombre,poblacion,superficie,continente\n")

        # Escribe cada pais como una fila
        for pais in paises:
            linea = pais["nombre"] + "," + str(pais["poblacion"]) + "," + str(pais["superficie"]) + "," + pais["continente"] + "\n"
            archivo.write(linea)


# --------------------------------------------
# FUNCION 3: Agregar pais
# --------------------------------------------
def agregar_pais(paises):

    # Validacion del nombre
    while True:
        try:
            nombre = input("Ingrese el nombre del pais: ").strip()

            if not nombre:
                raise ValueError("El nombre no puede estar vacio")

            # Verifica duplicados
            for pais in paises:
                if pais["nombre"].lower() == nombre.lower():
                    raise ValueError("El pais ya existe")

            break

        except ValueError as e:
            print(e)

    # Validacion poblacion
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

    # Validacion superficie
    while True:
        try:
            superficie = input("Ingresa la superficie en km2: ")

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

    # Validacion continente
    while True:
        try:
            continente = input("Ingresa el continente: ").strip()

            if not continente:
                raise ValueError("El continente no puede estar vacio")

            break

        except ValueError as e:
            print(e)

    # Se crea el nuevo pais
    nuevo_pais = {
        "nombre":     nombre,
        "poblacion":  poblacion_a_cargar,
        "superficie": superficie_a_cargar,
        "continente": continente
    }

    # El nuevo pais se agrega a la lista
    paises.append(nuevo_pais)

    # Se guarda en el CSV
    guardar_paises("paises.csv", paises)

    print("Pais agregado correctamente")


# --------------------------------------------
# FUNCION 4: Actualizar pais
# --------------------------------------------
def actualizar_pais(paises):

    # Busca el pais por nombre
    while True:
        try:
            nombre_buscado = input("Ingrese el nombre del pais a actualizar: ").strip()

            if not nombre_buscado:
                raise ValueError("El nombre no puede estar vacio")

            break

        except ValueError as e:
            print(e)

    # Busca en la lista
    for pais in paises:

        if pais["nombre"].lower() == nombre_buscado.lower():

            # Actualiza la poblacion
            while True:
                try:
                    poblacion = input("Ingresa la nueva poblacion: ")

                    if not poblacion:
                        raise ValueError("La poblacion no puede estar vacia")

                    if not poblacion.isdigit():
                        raise ValueError("Debe ingresar un numero entero")

                    poblacion_a_cargar = int(poblacion)

                    if poblacion_a_cargar <= 0:
                        raise ValueError("La poblacion debe ser mayor a 0")

                    break

                except ValueError as e:
                    print(e)

            # Actualiza la superficie
            while True:
                try:
                    superficie = input("Ingrese la nueva superficie: ")

                    if not superficie:
                        raise ValueError("La superficie no puede estar vacia")

                    if not superficie.isdigit():
                        raise ValueError("Debe ingresar un numero entero")

                    superficie_a_cargar = int(superficie)

                    if superficie_a_cargar <= 0:
                        raise ValueError("La superficie debe ser mayor a 0")

                    break

                except ValueError as e:
                    print(e)

            # Guarda los cambios
            pais["poblacion"]  = poblacion_a_cargar
            pais["superficie"] = superficie_a_cargar

            guardar_paises("paises.csv", paises)

            print("Pais actualizado correctamente")
            return

    print("No se encontro el pais")


# --------------------------------------------
# FUNCION 5: Buscar pais por nombre
# --------------------------------------------
def buscar_pais(paises):

    # Se solicita el nombre o parte del nombre
    nombre_buscar = input("Ingresa el nombre del pais que desea buscar: ").strip()

    # Validacion que no puede estar vacio
    if not nombre_buscar:
        print("Error: el nombre no puede estar vacio")
        return

    encontrados = []

    # Recorre la lista buscando coincidencias parciales
    for pais in paises:
        if nombre_buscar.lower() in pais["nombre"].lower():
            encontrados.append(pais)

    if len(encontrados) == 0:
        print("Error: no se encontraron paises con ese nombre")
        return

    print("------------ RESULTADOS ------------")

    for pais in encontrados:
        print(f"Nombre:     {pais['nombre']}")
        print(f"Poblacion:  {pais['poblacion']}")
        print(f"Superficie: {pais['superficie']} km2")
        print(f"Continente: {pais['continente']}")
        print("------------------------------------")


# --------------------------------------------
# FUNCION 6: Filtrar por continente
# --------------------------------------------
def filtrar_por_continente(paises):

    continente_buscar = input("Ingresa el continente que desea buscar: ").strip()

    if not continente_buscar:
        print("Error: el continente no puede estar vacio")
        return

    encontrados = []

    # Filtra los paises que coinciden con el continente ingresado
    for pais in paises:
        if pais["continente"].lower() == continente_buscar.lower():
            encontrados.append(pais)

    if len(encontrados) == 0:
        print("Error: no se encontraron paises en ese continente")
        return

    print("------------ RESULTADOS ------------")

    for pais in encontrados:
        print(f"Nombre:     {pais['nombre']}")
        print(f"Poblacion:  {pais['poblacion']}")
        print(f"Superficie: {pais['superficie']} km2")
        print(f"Continente: {pais['continente']}")
        print("------------------------------------")


# --------------------------------------------
# FUNCION 7: Filtrar por rango de poblacion
# --------------------------------------------
def filtrar_por_poblacion(paises):

    # Se solicita rango minimo y maximo de poblacion
    while True:
        try:
            minimo = input("Ingrese poblacion minima: ").strip()
            maximo = input("Ingrese poblacion maxima: ").strip()

            if not minimo or not maximo:
                raise ValueError("Los valores no pueden estar vacios")

            if not minimo.isdigit() or not maximo.isdigit():
                raise ValueError("Debe ingresar numeros enteros")

            # Conversion a enteros
            minimo_a_cargar = int(minimo)
            maximo_a_cargar = int(maximo)

            if minimo_a_cargar < 0 or maximo_a_cargar < 0:
                raise ValueError("Los valores no pueden ser menores a 0")

            if minimo_a_cargar > maximo_a_cargar:
                raise ValueError("El minimo no puede ser mayor que el maximo")

            break

        except ValueError as e:
            print(e)

    encontrados = []

    for pais in paises:
        if minimo_a_cargar <= pais["poblacion"] <= maximo_a_cargar:
            encontrados.append(pais)

    if len(encontrados) == 0:
        print("Error: no se encontraron paises en ese rango de poblacion")
        return

    print("------------ RESULTADOS ------------")

    for pais in encontrados:
        print(f"Nombre:     {pais['nombre']}")
        print(f"Poblacion:  {pais['poblacion']}")
        print(f"Superficie: {pais['superficie']} km2")
        print(f"Continente: {pais['continente']}")
        print("------------------------------------")


# --------------------------------------------
# FUNCION 8: Filtrar por rango de superficie
# --------------------------------------------
def filtrar_por_superficie(paises):

    # Se solicita rango minimo y maximo de superficie
    while True:
        try:
            minimo = input("Ingrese superficie minima en km2: ").strip()
            maximo = input("Ingrese superficie maxima en km2: ").strip()

            if not minimo or not maximo:
                raise ValueError("Los valores no pueden estar vacios")

            if not minimo.isdigit() or not maximo.isdigit():
                raise ValueError("Debe ingresar numeros enteros")

            # Conversion a enteros
            minimo_a_cargar = int(minimo)
            maximo_a_cargar = int(maximo)

            if minimo_a_cargar < 0 or maximo_a_cargar < 0:
                raise ValueError("Los valores no pueden ser menor a 0")

            if minimo_a_cargar > maximo_a_cargar:
                raise ValueError("El minimo no puede ser mayor que el maximo")

            break

        except ValueError as e:
            print(e)

    encontrados = []

    for pais in paises:
        if minimo_a_cargar <= pais["superficie"] <= maximo_a_cargar:
            encontrados.append(pais)

    if len(encontrados) == 0:
        print("Error: no se encontraron paises en ese rango de superficie")
        return

    print("------------ RESULTADOS ------------")

    for pais in encontrados:
        print(f"Nombre:     {pais['nombre']}")
        print(f"Poblacion:  {pais['poblacion']}")
        print(f"Superficie: {pais['superficie']} km2")
        print(f"Continente: {pais['continente']}")
        print("------------------------------------")


# --------------------------------------------
# FUNCION 9: Ordenar por nombre
# --------------------------------------------
def ordenar_por_nombre(paises):

    if len(paises) == 0:
        print("No hay paises cargados")
        return

    while True:
        try:
            orden = input("Ingrese 'A' para ascendente o 'D' para descendente: ").strip().upper()

            if orden != "A" and orden != "D":
                raise ValueError("Debe ingresar A o D")

            break

        except ValueError as e:
            print(e)

    # Ordenamiento por burbuja segun nombre
    n = len(paises)
    for i in range(n - 1):
        for j in range(n - 1 - i):

            nombre_actual    = paises[j]["nombre"].lower()
            nombre_siguiente = paises[j + 1]["nombre"].lower()

            if orden == "A":
                condicion = nombre_actual > nombre_siguiente
            else:
                condicion = nombre_actual < nombre_siguiente

            if condicion:
                paises[j], paises[j + 1] = paises[j + 1], paises[j]

    print("------------ PAISES ORDENADOS ------------")

    for pais in paises:
        print(f"Nombre: {pais['nombre']} | Poblacion: {pais['poblacion']} | Superficie: {pais['superficie']} km2 | Continente: {pais['continente']}")


# --------------------------------------------
# FUNCION 10: Ordenar por poblacion
# --------------------------------------------
def ordenar_por_poblacion(paises):

    if len(paises) == 0:
        print("No hay paises cargados")
        return

    while True:
        try:
            orden = input("Ingrese 'A' para ascendente o 'D' para descendente: ").strip().upper()

            if orden != "A" and orden != "D":
                raise ValueError("Debe ingresar A o D")

            break

        except ValueError as e:
            print(e)

    # Ordenamiento por burbuja segun poblacion
    n = len(paises)
    for i in range(n - 1):
        for j in range(n - 1 - i):

            if orden == "A":
                condicion = paises[j]["poblacion"] > paises[j + 1]["poblacion"]
            else:
                condicion = paises[j]["poblacion"] < paises[j + 1]["poblacion"]

            if condicion:
                paises[j], paises[j + 1] = paises[j + 1], paises[j]

    print("------------ PAISES ORDENADOS ------------")

    for pais in paises:
        print(f"Nombre: {pais['nombre']} | Poblacion: {pais['poblacion']} | Superficie: {pais['superficie']} km2 | Continente: {pais['continente']}")


# --------------------------------------------
# FUNCION 11: Ordenar por superficie
# --------------------------------------------
def ordenar_por_superficie(paises):

    if len(paises) == 0:
        print("No hay paises cargados")
        return

    while True:
        try:
            orden = input("Ingrese 'A' para ascendente o 'D' para descendente: ").strip().upper()

            if orden != "A" and orden != "D":
                raise ValueError("Debe ingresar A o D")

            break

        except ValueError as e:
            print(e)

    # Ordenamiento por burbuja segun superficie
    n = len(paises)
    for i in range(n - 1):
        for j in range(n - 1 - i):

            if orden == "A":
                condicion = paises[j]["superficie"] > paises[j + 1]["superficie"]
            else:
                condicion = paises[j]["superficie"] < paises[j + 1]["superficie"]

            if condicion:
                paises[j], paises[j + 1] = paises[j + 1], paises[j]

    print("------------ PAISES ORDENADOS ------------")

    for pais in paises:
        print(f"Nombre: {pais['nombre']} | Poblacion: {pais['poblacion']} | Superficie: {pais['superficie']} km2 | Continente: {pais['continente']}")


# --------------------------------------------
# FUNCION 12: Mostrar estadisticas
# --------------------------------------------
def mostrar_estadisticas(paises):

    if len(paises) == 0:
        print("No hay paises cargados")
        return

    # --- Mayor y menor poblacion ---
    # Arrancamos asumiendo que el primero es el mayor y el menor
    pais_mayor_poblacion = paises[0]
    pais_menor_poblacion = paises[0]

    for pais in paises:
        if pais["poblacion"] > pais_mayor_poblacion["poblacion"]:
            pais_mayor_poblacion = pais

        if pais["poblacion"] < pais_menor_poblacion["poblacion"]:
            pais_menor_poblacion = pais

    # --- Promedio de poblacion ---
    total_poblacion = 0
    for pais in paises:
        total_poblacion = total_poblacion + pais["poblacion"]

    promedio_poblacion = total_poblacion // len(paises)

    # --- Promedio de superficie ---
    total_superficie = 0
    for pais in paises:
        total_superficie = total_superficie + pais["superficie"]

    promedio_superficie = total_superficie // len(paises)

    # --- Cantidad de paises por continente ---
    continentes = []
    cantidades  = []

    for pais in paises:
        continente = pais["continente"]
        encontrado = False

        for i in range(len(continentes)):
            if continentes[i] == continente:
                cantidades[i] = cantidades[i] + 1
                encontrado = True

        if not encontrado:
            continentes.append(continente)
            cantidades.append(1)

    # --- Muestra todo ---
    print("------------ ESTADISTICAS ------------")
    print(f"Pais con mayor poblacion: {pais_mayor_poblacion['nombre']} ({pais_mayor_poblacion['poblacion']})")
    print(f"Pais con menor poblacion: {pais_menor_poblacion['nombre']} ({pais_menor_poblacion['poblacion']})")
    print(f"Promedio de poblacion:    {promedio_poblacion}")
    print(f"Promedio de superficie:   {promedio_superficie} km2")
    print("Cantidad de paises por continente:")

    for i in range(len(continentes)):
        print(f"  {continentes[i]}: {cantidades[i]}")


# ============================================
# PROGRAMA PRINCIPAL
# ============================================

paises = cargar_paises("paises.csv")

opcion = ""
while opcion != "11":
    try:
        print("\n------------------- MENU -------------------")
        print("1.  Agregar pais")
        print("2.  Actualizar pais")
        print("3.  Buscar pais por nombre")
        print("4.  Filtrar por continente")
        print("5.  Filtrar por rango de poblacion")
        print("6.  Filtrar por rango de superficie")
        print("7.  Ordenar por nombre")
        print("8.  Ordenar por poblacion")
        print("9.  Ordenar por superficie")
        print("10. Mostrar estadisticas")
        print("11. Salir")

        opcion = input("Seleccione una opcion (1 al 11): ").strip()

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
            filtrar_por_superficie(paises)

        elif opcion == "7":
            ordenar_por_nombre(paises)

        elif opcion == "8":
            ordenar_por_poblacion(paises)

        elif opcion == "9":
            ordenar_por_superficie(paises)

        elif opcion == "10":
            mostrar_estadisticas(paises)

        elif opcion == "11":
            print("Saliendo del sistema....")
            break

        else:
            print("Opcion fuera del rango 1-11")

    except ValueError:
        print("Ingresa un numero valido")
