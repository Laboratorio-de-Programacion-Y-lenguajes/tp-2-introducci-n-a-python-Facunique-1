import pytest
from src.funciones import aplicar_funcion, componer, memoizar, reducir


def test_aplicar_funcion():
    assert aplicar_funcion([1, 2, 3], lambda x: x * 2) == [2, 4, 6]


def test_componer():
    doble = lambda x: x * 2
    sumar_uno = lambda x: x + 1
    doble_luego_sumar = componer(sumar_uno, doble)
    assert doble_luego_sumar(3) == 7  # sumar_uno(doble(3)) = 7


def test_memoizar():
    llamadas = []

    def costosa(n):
        llamadas.append(n)
        return n * 2

    func_memo = memoizar(costosa)
    assert func_memo(5) == 10
    assert func_memo(5) == 10
    assert len(llamadas) == 1  # solo se ejecutó una vez


def test_reducir():
    assert reducir([1, 2, 3, 4], lambda a, b: a + b, 0) == 10
    assert reducir([1, 2, 3], lambda a, b: a * b, 1) == 6
