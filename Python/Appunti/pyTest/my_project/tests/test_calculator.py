from my_project.calculator import Calculator
import pytest

@pytest.fixture
def calcolo():
    return Calculator(10,5)

def test_addizione(calcolo):
    assert calcolo.addition() == 13, 'The sum is wrong'

def test_sottrazione(calcolo):
    assert calcolo.subtraction() == 5, 'The substracting is wrong'

def test_moltiplicazione(calcolo):
    assert calcolo.multiplication() == 50, 'The multiplication is wrong'

def test_divisione(calcolo):
    assert calcolo.division() == 2.00, 'The division is wrong'