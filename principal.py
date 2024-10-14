from apuesta import Apuesta
from perinola import Perinola
from jugadores import Jugador
from rondas import Ronda

ronda = Ronda()
nombres = ("j1", "j2", "j3", "j4")
for n in nombres:
    j = Jugador(n, 3)
    ronda.agregarJugador(j)
apuesta = Apuesta()
perinola = Perinola()

def ponerTodos():
    print("Ponen todos")
    for j in ronda.jugadores:
        j.sacarFicha()
        apuesta.ponerFichas()    

ponerTodos()

while not (ronda.quedaUnSoloJugador() or ronda.noQuedanJugador()):
    print(ronda)
    print(apuesta)

    if apuesta.estaVacia():
        ponerTodos()
    ronda.sacarJugadoresSinFichas()

    if ronda.quedaUnSoloJugador() or ronda.noQuedanJugador():
        break

    jt = ronda.jugadorEnTurno()
    print("le toca a: ", end="")
    print(jt)

    p = perinola.tirar()
    print(p)

    if p == "Pon 1":
        jt.sacarFicha()
        apuesta.ponerFichas()
    elif p == "Pon 2":
        if jt.ficha == 1:
            jt.sacarFicha()
            apuesta.ponerFichas()
        else:
            jt.sacarFicha(2)
            apuesta.ponerFichas(2)
    elif p == "Toma 1":
        apuesta.tomarFicha()
        jt.darFicha()
    elif p == "Toma 2":
        if apuesta.ficha == 1:
            apuesta.tomarFicha()
            jt.darFicha()
        else:
            apuesta.tomarFicha(2)
            jt.darFicha(2)
    elif p == "Toma Todo":
        fichas = apuesta.tomarTodas()
        jt.darFicha(fichas)
    elif p == "Todos Ponen":
        ponerTodos()
    else:
        raise ValueError("Valor inesperado")



    print(apuesta)
    print(ronda)
    ronda.sacarJugadoresSinFichas()
    ronda.pasarTurno()
    print()

if ronda.quedaUnSoloJugador():
    print(f"Terminó el juego, ganó: {ronda.jugadorEnTurno()}")
else:
    print(f"Terminó el juego, perdieron todos")