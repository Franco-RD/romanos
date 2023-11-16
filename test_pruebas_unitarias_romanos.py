#Pytest sirve para hacer pruebas unitarias. El assert devuelve un valor logico. 
#def test_prueba():
    #assert 10<20

from main import entero_a_romano

def test_prueba_entero_a_romano4():
    assert entero_a_romano(1994) == 'MCMXCIV'

def test_prueba_entero_a_romano3():
    assert entero_a_romano(837) == 'DCCCXXXVII'

def test_prueba_entero_a_romano2():
    assert entero_a_romano(64) == 'LXIV'

def test_prueba_entero_a_romano1():
    assert entero_a_romano(7) == 'VII'