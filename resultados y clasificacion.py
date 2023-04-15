from itertools import combinations
import random

jugadores = ["Dani", "David", "Enano", "Cocinera", "Alexis", "Gafas", "Mauricio", "Jaimito"]

# Variables para almacenar los partidos y las posiciones
partidos = []
posiciones = {jugador: {"Puntos": 0, "PG": 0, "PE": 0, "PP": 0, "GF": 0, "GC": 0} for jugador in jugadores}

# Generamos los partidos
jornadas = []
num_jugadores = len(jugadores)
num_partidos_por_jornada = num_jugadores // 2
partidos_por_jugador = []

if num_jugadores % 2 == 1:
    jugadores.append("Descansa")

for i in range(num_jugadores - 1):
    partidos_por_jugador.append([])

for i in range(num_jugadores - 1):
    for j in range(num_partidos_por_jornada):
        partido = (jugadores[j], jugadores[num_jugadores - 1 - j])
        partidos_por_jugador[i].append(partido)
        partidos.append(partido)
    jugadores.insert(1, jugadores.pop())

for i in range(num_jugadores - 1):
    jornada = []
    for j in range(num_partidos_por_jornada):
        if i % 2 == 0:
            jornada.append(partidos_por_jugador[j])
        else:
            jornada.append(partidos_por_jugador[num_partidos_por_jornada - 1 - j])
    jornadas.append(jornada)

# Simulamos los resultados de los partidos (para este ejemplo, los resultados son aleatorios)
# Simulamos los resultados de los partidos (para este ejemplo, los resultados son ingresados por el usuario)
for partido in partidos:
    goles_local = int(input("Ingrese los goles del equipo local en el partido {}: {} vs {}: ".format(partidos.index(partido)+1, partido[0], partido[1])))
    goles_visitante = int(input("Ingrese los goles del equipo visitante en el partido {}: {} vs {}: ".format(partidos.index(partido)+1, partido[0], partido[1])))
    
    posiciones[partido[0]]["GF"] += goles_local
    posiciones[partido[1]]["GF"] += goles_visitante
    posiciones[partido[0]]["GC"] += goles_visitante
    posiciones[partido[1]]["GC"] += goles_local
    
    if goles_local > goles_visitante:
        posiciones[partido[0]]["Puntos"] += 3
        posiciones[partido[0]]["PG"] += 1
        posiciones[partido[1]]["PP"] += 1
    elif goles_local < goles_visitante:
        posiciones[partido[1]]["Puntos"] += 3
        posiciones[partido[1]]["PG"] += 1
        posiciones[partido[0]]["PP"] += 1
    else:
        posiciones[partido[0]]["Puntos"] += 1
        posiciones[partido[1]]["Puntos"] += 1
        posiciones[partido[0]]["PE"] += 1
        posiciones[partido[1]]["PE"] += 1

# Ordenamos las posiciones
posiciones_ordenadas = sorted(posiciones.items(), key=lambda x: x[1]["Puntos"], reverse=True)

# Imprimimos el calendario de partidos y las posiciones
# Imprimimos las posiciones
# Ordenamos las posiciones
posiciones_ordenadas = sorted(posiciones.items(), key=lambda x: (x[1]["Puntos"], x[1]["GF"]-x[1]["GC"]), reverse=True)

# Imprimimos la tabla de posiciones
print("Tabla de posiciones:\n")
print("{:<10s}{:<5s}{:<5s}{:<5s}{:<5s}{:<5s}{:<5s}".format("Jugador", "Pts", "PG", "PE", "PP", "GF", "GC"))
for jugador, stats in posiciones_ordenadas:
    print("{:<10s}{:<5d}{:<5d}{:<5d}{:<5d}{:<5d}{:<5d}".format(jugador, stats["Puntos"], stats["PG"], stats["PE"], stats["PP"], stats["GF"], stats["GC"]))
