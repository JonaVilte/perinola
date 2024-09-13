import pytest
from apuesta import Fichas

def test_prueba():
    assert(True)

def test_constructor():
    a = Fichas()
    assert(a.ficha == 0)

def test_repr():
    a = Fichas()
    msj = a.__repr__()
    assert("Apuesta: " in msj)
    assert("4" in msj)
    assert("fichas" in msj)

def test_ponerFichas():
    a = Fichas()
    a.ponerFichas(2)
    assert(a.ficha == 2)
    
    a = Fichas()
    a.ponerFichas(4)
    assert(a.ficha == 4)
    a.ponerFichas(2)
    assert(a.ficha == 6)

def test_tomarFichas():
    a = Fichas()
    a.ficha = 6
    a.tomarFicha(2)
    assert(a.ficha == 4)


def test_tomarFichas_error():
    a = Fichas()
    with pytest.raises(ValueError):
        a =     