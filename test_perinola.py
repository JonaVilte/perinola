import pytest
from perinola import Perinola

def test_constructor():
    p = Perinola()
    assert p.cara_visible == 'Pon 1'

def test_repr():
    p = Perinola()
    p.cara_visible = 'Pon 1'
    msj = p.__repr__()
    assert("Salio: " in msj)
    assert("Pon 1" in msj)

def test_tirar():
    p = Perinola()
    caras = p.tirar()
    assert caras in ("Pon 1", "Toma 2", "Todos Ponen",
     "Toma 1", "Pon 2", "Toma Todo")
    assert p.cara_visible == caras 
