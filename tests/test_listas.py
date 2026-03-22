import pytest
from src.listas import (
    suma_lista,
    filtrar_pares,
    invertir_lista,
    eliminar_duplicados,
    aplanar_lista,
)


def test_suma_lista():
    assert suma_lista([1, 2, 3, 4]) == 10
    assert suma_lista([]) == 0


def test_filtrar_pares():
    assert filtrar_pares([1, 2, 3, 4, 5, 6]) == [2, 4, 6]
    assert filtrar_pares([1, 3, 5]) == []


def test_invertir_lista_no_modifica_original():
    original = [1, 2, 3]
    resultado = invertir_lista(original)
    assert resultado == [3, 2, 1]
    assert original == [1, 2, 3]


def test_eliminar_duplicados():
    assert eliminar_duplicados([1, 2, 2, 3, 1]) == [1, 2, 3]
    assert eliminar_duplicados([1, 1, 1]) == [1]


def test_eliminar_duplicados_orden():
    assert eliminar_duplicados([3, 1, 2, 1, 3]) == [3, 1, 2]


def test_aplanar_lista():
    assert aplanar_lista([[1, 2], [3, 4]]) == [1, 2, 3, 4]
    assert aplanar_lista([[1], [2], [3]]) == [1, 2, 3]
