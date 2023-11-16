#Pytest sirve para hacer pruebas unitarias. El assert devuelve un valor logico. 
#def test_prueba():
    #assert 10<20

from main import entero_a_romano

valor_romano4 = entero_a_romano(1994)

def test_prueba_entero_a_romano4():
    assert valor_romano4 == 'MCMXCIV'


valor_romano3 = entero_a_romano(837)

def test_prueba_entero_a_romano3():
    assert valor_romano3 == 'DCCCXXXVII'


valor_romano2 = entero_a_romano(64)

def test_prueba_entero_a_romano2():
    assert valor_romano2 == 'LXIV'


valor_romano1 = entero_a_romano(7)

def test_prueba_entero_a_romano1():
    assert valor_romano1 == 'VII'