from apuesta import Apuesta

class Ronda:
    def __init__(self):
        self.jugadores = []

    def __repr__(self):
        return "\n".join(str(jugador) for jugador in self.jugadores)
    
    def agregarJugador(self, jugador):
        if jugador.ficha <= 0:
            raise ValueError("No puedes agregar a un jugador que no tiene fichas")
        self.jugadores.append(jugador)
    def sacarJugadoresSinFichas(self):
        self.jugadores = [jugador for jugador in self.jugadores if jugador.ficha >  0]
    def jugadorEnTurno(self):
        if len(self.jugadores) > 0:
            return self.jugadores[0]

    def pasarTurno(self):
        if len(self.jugadores) > 0:
            j = self.jugadores.pop(0)
            self.jugadores.append(j)

    def quedaUnSoloJugador(self):
        return len(self.jugadores) == 1

    def noQuedanJugador(self):
        return len(self.jugadores) == 0
        