from jugadores import Jugador

class Ronda:
    def __init__(self):
        self.jugadores = []

    def __repr__(self):
        return f"{self.jugadores}"
    
    def agregarJugador(self, jugador):
        jugador = Jugador()
        if jugador.ficha == 0:
            raise ValueError("No puedes agregar a un jugador que no tiene fichas")
        self.jugadores.append(jugador)

    def sacarJugadoresSinFichas(self):
        for jugador in self.jugadores:
            if jugador[1] == 0:
                self.jugadores.pop(jugador)

    def jugadorEnTurno(self):
        print(f"{self.jugadores[0]}")

    def pasarTurno(self):
        j = self.jugadores.pop[0]
        self.jugadores.append[j]

    def quedaUnSoloJugador(self):
        return len(self.jugadores) == 1

        