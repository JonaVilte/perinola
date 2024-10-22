import pytest
from jugadores import Jugador

def test_constructor():
    j = Jugador('j1')
    assert j.nombre == 'j1'
    assert j.ficha == 5

def test_repr():
    j = Jugador('j1')
    msj = j.__repr__()
    assert(j.nombre)
    assert("," in msj)
    assert(j.ficha)
    assert("fichas" in msj)

def test_darFicha():
    j = Jugador("j3")
    j.darFicha(3)
    assert j.ficha == 8

def test_sacarFicha():
    j = Jugador("j4")
    j.sacarFicha(2)
    assert j.ficha == 3

    with pytest.raises(ValueError):
        j.sacarFicha(5)

def test_tieneFicha():
    j = Jugador("j5")
    assert j.tieneFicha(5)  
    assert j.tieneFicha(4)  
    assert not j.tieneFicha(6)

def test_sinFichas():
    j = Jugador("j6", 0)
    assert j.sinFichas()  
    j.darFicha(1)
    assert not j.sinFichas()