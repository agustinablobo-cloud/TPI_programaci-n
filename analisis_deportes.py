import pandas as pd

# Leer CSV
df = pd.read_csv("resultados_deportes.csv", sep=";")

# Limpiar nombres de columnas
df.columns = df.columns.str.strip()

print(df.columns)

equipos = {}

# Recorrer cada partido
for _, fila in df.iterrows():

    local = fila["Local"]
    visitante = fila["Visitantes"]

    goles_local = fila["Goles_local"]
    goles_visitante = fila["Goles_visitantes"]

    # Crear equipos si no existen
    for equipo in [local, visitante]:

        if equipo not in equipos:

            equipos[equipo] = {
                "PJ": 0,
                "PG": 0,
                "PE": 0,
                "PP": 0,
                "GF": 0,
                "GC": 0,
                "PTS": 0
            }

    # Partidos jugados
    equipos[local]["PJ"] += 1
    equipos[visitante]["PJ"] += 1

    # Goles
    equipos[local]["GF"] += goles_local
    equipos[local]["GC"] += goles_visitante

    equipos[visitante]["GF"] += goles_visitante
    equipos[visitante]["GC"] += goles_local

    # Resultado
    if goles_local > goles_visitante:

        equipos[local]["PG"] += 1
        equipos[local]["PTS"] += 3

        equipos[visitante]["PP"] += 1

    elif goles_local < goles_visitante:

        equipos[visitante]["PG"] += 1
        equipos[visitante]["PTS"] += 3

        equipos[local]["PP"] += 1

    else:

        equipos[local]["PE"] += 1
        equipos[visitante]["PE"] += 1

        equipos[local]["PTS"] += 1
        equipos[visitante]["PTS"] += 1

# Crear DataFrame
tabla = pd.DataFrame(equipos).T

# Diferencia de gol
tabla["DG"] = tabla["GF"] - tabla["GC"]

# Promedio de goles
tabla["Promedio_Goles"] = tabla["GF"] / tabla["PJ"]

# Ordenar tabla
tabla = tabla.sort_values(
    by=["PTS", "DG", "GF"],
    ascending=False
)

print("\nTABLA DE POSICIONES")
print(tabla)

print("\nPARTIDOS GANADOS")
print(tabla["PG"].to_string(index=True))

print("\nPROMEDIO DE GOLES")
print(tabla["Promedio_Goles"].to_string(index=True))

