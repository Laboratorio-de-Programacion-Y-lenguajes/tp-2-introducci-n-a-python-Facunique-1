import pytest
from src.loops import (
    contar_hasta,
    tabla_multiplicar,
    suma_digitos,
    es_primo,
    fibonacci,
)


def test_contar_hasta():
    assert contar_hasta(5) == [1, 2, 3, 4, 5]
    assert contar_hasta(1) == [1]


def test_tabla_multiplicar():
    assert tabla_multiplicar(3) == [3, 6, 9, 12, 15, 18, 21, 24, 27, 30]


def test_suma_digitos():
    assert suma_digitos(123) == 6
    assert suma_digitos(0) == 0


def test_es_primo_true():
    assert es_primo(2) is True
    assert es_primo(7) is True
    assert es_primo(13) is True


def test_es_primo_false():
    assert es_primo(1) is False
    assert es_primo(4) is False
    assert es_primo(9) is False


def test_fibonacci():
    assert fibonacci(6) == [0, 1, 1, 2, 3, 5]
    assert fibonacci(1) == [0]
