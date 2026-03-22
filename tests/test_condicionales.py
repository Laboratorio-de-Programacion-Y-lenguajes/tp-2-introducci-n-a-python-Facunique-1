import pytest
from src.condicionales import (
    clasificar_numero,
    mayor_de_tres,
    clasificar_nota,
    es_bisiesto,
)


def test_clasificar_numero_positivo():
    assert clasificar_numero(5) == "positivo"


def test_clasificar_numero_negativo():
    assert clasificar_numero(-3) == "negativo"


def test_clasificar_numero_cero():
    assert clasificar_numero(0) == "cero"


def test_mayor_de_tres():
    assert mayor_de_tres(1, 2, 3) == 3
    assert mayor_de_tres(5, 3, 4) == 5
    assert mayor_de_tres(2, 7, 1) == 7


def test_clasificar_nota_sobresaliente():
    assert clasificar_nota(9) == "Sobresaliente"
    assert clasificar_nota(10) == "Sobresaliente"


def test_clasificar_nota_bueno():
    assert clasificar_nota(7) == "Bueno"
    assert clasificar_nota(8) == "Bueno"


def test_clasificar_nota_aprobado():
    assert clasificar_nota(6) == "Aprobado"


def test_clasificar_nota_desaprobado():
    assert clasificar_nota(5) == "Desaprobado"
    assert clasificar_nota(0) == "Desaprobado"


def test_es_bisiesto_true():
    assert es_bisiesto(2000) is True
    assert es_bisiesto(2024) is True


def test_es_bisiesto_false():
    assert es_bisiesto(1900) is False
    assert es_bisiesto(2023) is False
