import pytest
from src.operaciones import (
    es_palindromo,
    capitalizar_palabras,
    contar_vocales,
    caesar_cipher,
)


def test_es_palindromo_true():
    assert es_palindromo("ana") is True
    assert es_palindromo("Anita lava la tina") is True


def test_es_palindromo_false():
    assert es_palindromo("hola") is False


def test_capitalizar_palabras():
    assert capitalizar_palabras("hola mundo") == "Hola Mundo"
    assert capitalizar_palabras("python es genial") == "Python Es Genial"


def test_contar_vocales():
    assert contar_vocales("hola mundo") == 4
    assert contar_vocales("AEIOU") == 5


def test_caesar_cipher():
    assert caesar_cipher("abc", 1) == "bcd"
    assert caesar_cipher("xyz", 1) == "yza"
    assert caesar_cipher("ABC", 2) == "CDE"
    assert caesar_cipher("Hola, mundo!", 3) == "Krod, pxqgr!"
