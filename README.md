# TPI - Gestión de Datos de Países en Python

Programación 1  
Integrantes: LOBO, Agustina Brenda (comision 16) / ALTAVISTA, Lucio E.(comision 18)

## Descripción

Sistema de gestión de información sobre países desarrollado en Python. Permite realizar operaciones sobre un dataset almacenado en un archivo CSV: agregar, actualizar, buscar, filtrar, ordenar y obtener estadísticas de los países cargados.

## Requisitos

- Python 3.x
- No requiere librerías externas

## Archivos del proyecto

| Archivo | Descripción |
|---|---|
| `TPI_programacion.py` | Código fuente principal |
| `paises.csv` | Dataset base con 12 países |
| `README.md` | Este archivo |

## Cómo ejecutar el programa

1. Asegurarse de que `TPI_programacion.py` y `paises.csv` estén en la **misma carpeta**
2. Abrir una terminal en esa carpeta
3. Ejecutar:

python TPI_programacion.py


## Funcionalidades del sistema

El programa presenta un menú con 11 opciones:

------------------- MENU -------------------
1.  Agregar pais
2.  Actualizar pais
3.  Buscar pais por nombre
4.  Filtrar por continente
5.  Filtrar por rango de poblacion
6.  Filtrar por rango de superficie
7.  Ordenar por nombre
8.  Ordenar por poblacion
9.  Ordenar por superficie
10. Mostrar estadisticas
11. Salir

## Ejemplos de uso

### Buscar un país (opción 3)

Entrada:
Seleccione una opcion (1 al 11): 3
Ingresa el nombre del pais que desea buscar: arg

Salida:
------------ RESULTADOS ------------
Nombre:     Argentina
Poblacion:  45376763
Superficie: 2780400 km2
Continente: America
------------------------------------

### Filtrar por continente (opción 4)

Entrada:

Seleccione una opcion (1 al 11): 4
Ingresa el continente que desea buscar: Asia

Salida:
------------ RESULTADOS ------------
Nombre:     Japon
Poblacion:  125800000
Superficie: 377975 km2
Continente: Asia
------------------------------------
Nombre:     China
Poblacion:  1412600000
Superficie: 9596960 km2
Continente: Asia
------------------------------------
Nombre:     India
Poblacion:  1380004385
Superficie: 3287263 km2
Continente: Asia
------------------------------------

### Mostrar estadísticas (opción 10)

Salida:
------------ ESTADISTICAS ------------
Pais con mayor poblacion: China (1412600000)
Pais con menor poblacion: Australia (25690000)
Promedio de poblacion:    384327521
Promedio de superficie:   3907722 km2
Cantidad de paises por continente:
  America: 4
  Asia: 3
  Europa: 2
  Africa: 2
  Oceania: 1

## Ordenar por población (opción 8)

Entrada:
Seleccione una opcion (1 al 11): 8
Ingrese 'A' para ascendente o 'D' para descendente: A

Salida:
------------ PAISES ORDENADOS ------------
Nombre: Australia | Poblacion: 25690000 | Superficie: 7692024 km2 | Continente: Oceania
Nombre: Canada | Poblacion: 38005238 | Superficie: 9984670 km2 | Continente: America

## Formato del CSV

nombre,poblacion,superficie,continente
Argentina,45376763,2780400,America
Brasil,213993437,8515767,America

> **Importante:** el separador debe ser coma (`,`). No usar punto y coma.

## Links

- Video demostrativo:https://drive.google.com/file/d/1ZQ1lSfsm6YJLV-ZA5NZkGDmD5Lbh9TbM/view

- Documentación PDF:https://docs.google.com/document/d/1uPostbizA9R97jEiBG2e0nsqBmv59yo_z_uxZWTANOo/edit?pli=1&tab=t.0

## Participación de los integrantes

| Integrante | 
| LOBO, Agustina Brenda |
| ALTAVISTA, Lucio Enrique |
