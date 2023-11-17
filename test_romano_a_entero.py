from main import romano_a_entero

def test_romano_a_entero():
    assert romano_a_entero('I') == 1

def test_romano_a_entero_MDCCCXIII():
    assert romano_a_entero('MDCCCXIII') == 1713

def test_romano_a_entero_IV():
    assert romano_a_entero('IV') == 4

