import pytest  
from rondas import Ronda
from jugadores import Jugador

def test_constructor():
    r = Ronda()
    assert len(r.jugadores) == 0

def test_repr():
    r = Ronda()
    jugador1 = Jugador("j1", 10)
    r.agregarJugador(jugador1)
    msj = r.__repr__()
    assert f"{jugador1}" in msj  

def test_agregarJugador():
    r = Ronda()
    j = Jugador("JugadorSinFichas", 0)
    with pytest.raises(ValueError):
        r.agregarJugador(j)  

    j2 = Jugador("JugadorConFichas", 10)
    r.agregarJugador(j2)  
    assert j2 in r.jugadores  

def test_sacarJugadoresSinFichas():
    r = Ronda()
    j1 = Jugador("j1", 10)
    j2 = Jugador("j2", 0)
    j3 = Jugador("j3", 5)
    
    r.agregarJugador(j1)
    r.agregarJugador(j2)
    r.agregarJugador(j3)
    
    r.sacarJugadoresSinFichas()
    
    assert len(r.jugadores) == 2  
    assert j2 not in r.jugadores  

def test_jugadorEnTurno():
    r = Ronda()
    j1 = Jugador("j1", 10)
    j2 = Jugador("j2", 5)
    
    r.agregarJugador(j1)
    r.agregarJugador(j2)
    
    assert r.jugadorEnTurno() == j1  

def test_pasarTurno():
    r = Ronda()
    j1 = Jugador("j1", 10)
    j2 = Jugador("j2", 5)
    
    r.agregarJugador(j1)
    r.agregarJugador(j2)
    
    r.pasarTurno()
    assert r.jugadorEnTurno() == j2  

def test_quedaUnSoloJugador():
    r = Ronda()
    j1 = Jugador("j1", 10)
    j2 = Jugador("j2", 0)
    
    r.agregarJugador(j1)
    r.agregarJugador(j2)
    r.sacarJugadoresSinFichas()  
    
    assert r.quedaUnSoloJugador()  

def test_noQuedanJugadores():
    r = Ronda()
    j1 = Jugador("j1", 0)
    r.agregarJugador(j1)  
    r.sacarJugadoresSinFichas() 

    assert r.noQuedanJugador()  
