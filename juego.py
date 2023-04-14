from itertools import combinations
##calendario para jugar play

jugadores = ["Dani", "David", "Enano", "Cocinera", "Alexis", "Gafas", "Mauricio", "Jaimito"]

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
    jugadores.insert(1, jugadores.pop())

for i in range(num_jugadores - 1):
    jornada = []
    for j in range(num_partidos_por_jornada):
        if i % 2 == 0:
            jornada.append(partidos_por_jugador[j])
        else:
            jornada.append(partidos_por_jugador[num_partidos_por_jornada - 1 - j])
    jornadas.append(jornada)
    
print("Calendario de partidos por jornada:")
for i, jornada in enumerate(jornadas):
    print("Jornada", i+1, ":")
    for partido in jornada:
        print(partido[0][0], "vs.", partido[0][1])
        print(partido[1][0], "vs.", partido[1][1])
    print()
