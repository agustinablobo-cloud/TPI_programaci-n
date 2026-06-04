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
        with open(nombre_archivo, "r") as archivo:
         lector = csv.DictReader(archivo)
        

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

    except ValueError:
       print("Error: Formato numerico incorrecto en el CSV")

    except KeyError:
       print("Error: Faltan columnas en el CSV")

    except Exception as e:
        print("Ocurrió el siguiente error: ", type(e).__name__ )

    return paises