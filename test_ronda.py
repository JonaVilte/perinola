import pytest
from rondas import Ronda
from jugadores import Jugador

def test_constructor():
    r = Ronda()
    assert(len(r.jugadores) == 0)

def test_repr():
    r = Ronda()
    msj = r.__repr__()
    assert(f"{r.jugadores}" in msj)

def test_agregarJugador():
    j = Jugador()
    with pytest.raises(ValueError):
        j.ficha = 0
