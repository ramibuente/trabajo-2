#ejercicio 10
from src import diccionario #importo el archivo diccionarios.py para poder usar las funciones
rounds = [
{
'Shadow': {'kills': 2, 'assists': 1, 'deaths': True},
'Blaze': {'kills': 1, 'assists': 0, 'deaths': False},
'Viper': {'kills': 1, 'assists': 2, 'deaths': True},
'Frost': {'kills': 0, 'assists': 1, 'deaths': False},
'Reaper': {'kills': 1, 'assists': 1, 'deaths': False}
},
{
'Shadow': {'kills': 0, 'assists': 2, 'deaths': False},
'Blaze': {'kills': 2, 'assists': 0, 'deaths': True},
'Viper': {'kills': 1, 'assists': 1, 'deaths': False},
'Frost': {'kills': 2, 'assists': 1, 'deaths': True},
'Reaper': {'kills': 0, 'assists': 1, 'deaths': False}
},
{
'Shadow': {'kills': 1, 'assists': 0, 'deaths': False},
'Blaze': {'kills': 2, 'assists': 2, 'deaths': True},
'Viper': {'kills': 1, 'assists': 1, 'deaths': True},
'Frost': {'kills': 0, 'assists': 1, 'deaths': False},
'Reaper': {'kills': 1, 'assists': 1, 'deaths': False}
},
{
'Shadow': {'kills': 2, 'assists': 1, 'deaths': False},
'Blaze': {'kills': 1, 'assists': 0, 'deaths': True},
'Viper': {'kills': 0, 'assists': 2, 'deaths': False},
'Frost': {'kills': 1, 'assists': 1, 'deaths': True},
'Reaper': {'kills': 1, 'assists': 1, 'deaths': False}
},
{
'Shadow': {'kills': 1, 'assists': 2, 'deaths': True},
'Blaze': {'kills': 0, 'assists': 1, 'deaths': False},
'Viper': {'kills': 2, 'assists': 0, 'deaths': True},
'Frost': {'kills': 1, 'assists': 1, 'deaths': False},
'Reaper': {'kills': 1, 'assists': 1, 'deaths': True}
}
]
rondas=1

jugadores = {} #creo el diccionario el cual voy a guardar mis datos globales de la partida
diccionario.crear(jugadores,rounds)
for i in rounds: #creo el esquema de la tabla de posiciones de cada ronda
    print("-" * 50)
    print('Ranking ronda: ',rondas)
    print(f"{'Jugador':<10} {'Kills':<6} {'Asistencias':<10} {'Muertes':<7} {'Puntos':<6}")
    print("-" * 50)
    rondas+=1
    puntos_ronda={}
    for jugador in i:
        points = i[jugador]['kills'] * 3 + i[jugador]['assists'] - i[jugador]['deaths']  #sistema de puntos utilizado en este juego
       #guardo sus estadisticas en el diccionario global creado anteriormente
        jugadores[jugador]['kills']+=i[jugador]['kills']
        jugadores[jugador]['assists']+=i[jugador]['assists']
        if i[jugador]['deaths']:
            jugadores[jugador]['deaths']+=1
        jugadores[jugador]['puntos']+=points

        puntos_ronda[jugador]=points
        print(f"{jugador:<10} {i[jugador]['kills']:<6} {i[jugador]['assists']:<10} {i[jugador]['deaths']:<7} {points:<6}") #imprimo las estadisticas de esa ronda
    mvp_nombre= max(puntos_ronda, key=puntos_ronda.get)  #consigo cual fue el que mas puntos tuvo en la ronda
    jugadores[mvp_nombre]['MVP']+=1 #le sumo 1 mvp a su estadistica global
ranking_final_ordenado=diccionario.ordenarP(jugadores)   #ordeno el ranking final por puntos con la funcion anteriormente creada
print("-" * 50)
print('Ranking ronda final')
print("Jugador   Kills   Asistencias   Muertes  MVP   Puntos")
print("-" * 50)
diccionario.imprimir(ranking_final_ordenado) #imprimo el ranking final
print("-" * 50)
