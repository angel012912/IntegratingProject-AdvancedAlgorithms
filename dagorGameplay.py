from dagor import JuegoOrugas, JugadorOrugasAleatorio
from equipo9 import JugadorOrugasEquipo9

if __name__ == '__main__':
    juego = JuegoOrugas(
        JugadorOrugasEquipo9('Pablo'),
        JugadorOrugasAleatorio('Random'),
        10, 10)
    juego.inicia(veces=100, delta_max=2)
