import pytest
from src.diccionarios import (
    contar_palabras,
    invertir_diccionario,
    merge_diccionarios,
    filtrar_por_valor,
)


def test_contar_palabras():
    assert contar_palabras("hola mundo hola") == {"hola": 2, "mundo": 1}


def test_contar_palabras_case_insensitive():
    assert contar_palabras("Hola hola") == {"hola": 2}


def test_invertir_diccionario():
    assert invertir_diccionario({"a": 1, "b": 2}) == {1: "a", 2: "b"}


def test_merge_diccionarios_sin_conflicto():
    assert merge_diccionarios({"a": 1}, {"b": 2}) == {"a": 1, "b": 2}


def test_merge_diccionarios_con_conflicto():
    assert merge_diccionarios({"a": 1}, {"a": 99}) == {"a": 99}


def test_filtrar_por_valor():
    assert filtrar_por_valor({"a": 5, "b": 10, "c": 3}, 5) == {"a": 5, "b": 10}
