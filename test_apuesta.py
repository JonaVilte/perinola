import pytest   
from apuesta import Apuesta

def test_prueba():
    assert(True)

def test_constructor():
    a = Apuesta()
    assert(a.ficha == 0)

def test_repr():
    a = Apuesta()
    a.ficha = 4
    msj = a.__repr__()
    assert("Apuesta: " in msj)
    assert("4" in msj)
    assert("fichas" in msj)

def test_ponerFichas():
    a = Apuesta()
    a.ponerFichas(2)
    assert(a.ficha == 2)
    
    a = Apuesta()
    a.ponerFichas(4)
    assert(a.ficha == 4)
    a.ponerFichas(2)
    assert(a.ficha == 6)

def test_ponerFichas_sin_argumento():
    a = Apuesta()
    a.ficha = 6
    a.ponerFichas()
    assert(a.ficha == 7)

def test_tomarFichas():
    a = Apuesta()
    a.ficha = 6
    a.tomarFicha(2)
    assert(a.ficha == 4)

def test_tomarFichas_sin_argumento():
    a = Apuesta()
    a.ficha = 6
    a.tomarFicha()
    assert(a.ficha == 5)

def test_tomarFichas_error():
    with pytest.raises(ValueError):
        a = Apuesta()
        a.ficha = 5
        a.tomarFicha(6)  
        
    a = Apuesta()
    a.ficha = 5
    a.tomarFicha(5)  

def test_tomarTodo():
    a = Apuesta()
    a.ponerFichas(1)
    a.tomarTodas()
    assert(a.ficha == 0) 

def test_tomarTodo_error():
    with pytest.raises(ValueError):
        a=Apuesta()
        a.ponerFichas()
        a.tomarTodas()
    assert(a.ficha == 0)
        

def test_tieneFicha():
    a = Apuesta()
    a.ponerFichas(4)
    a.tieneFicha(4)
    assert(a.ficha == 4)
    