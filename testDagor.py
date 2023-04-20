from dagor1 import JuegoOrugas, JugadorOrugasAleatorio, JugadorOrugasInteractivo
from jugadorOrugasEquipo9 import JugadorOrugasEquipo9v1, JugadorOrugasEquipo9v2
from equipo9 import JugadorOrugasEquipo9
import time
import random



def probarAlgoritmos(jugador1, jugador2):
    ganados2, ganados1 = 0, 0
    for i in range(4, 11):
        for a in range(4, 11):
            juego = JuegoOrugas(jugador1('Jugador 1'), jugador2('Jugador 2'),
                                i, a)
            resultados = juego.inicia(veces=100, delta_max=2)
            ganados1 += resultados[0]
            ganados2 += resultados[1]
    print("Jugador 1 gano: ", ganados1, "\nJugador 2 gano: ", ganados2)


if __name__ == '__main__':
    n = random.randint(4, 10)
    m = random.randint(4, 10)
    tiempo_inicio = time.time() # Tiempo de inicio
    # probarAlgoritmos(JugadorOrugasEquipo9v1, JugadorOrugasEquipo9v2) 
    juego = JuegoOrugas(JugadorOrugasEquipo9('Jugador 1'), JugadorOrugasAleatorio('Jugador 2'), 4, 7)
    juego.inicia(veces=100, delta_max=2)
    tiempo_fin = time.time()
    delta = tiempo_fin - tiempo_inicio
    print("Tiempo: ", delta, "s\n")
