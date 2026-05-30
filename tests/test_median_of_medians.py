import pytest
from app.median_of_medians import selecionar_kesimo, calcular_p50


def test_selecionar_kesimo_lista_pequena():
    valores = [3, 1, 4, 1, 5, 9, 2, 6]
    for k in range(len(valores)):
        assert selecionar_kesimo(list(valores), k) == sorted(valores)[k]


def test_selecionar_kesimo_elemento_unico():
    assert selecionar_kesimo([42], 0) == 42


def test_selecionar_kesimo_ja_ordenada():
    valores = list(range(20))
    for k in range(len(valores)):
        assert selecionar_kesimo(list(valores), k) == k


def test_selecionar_kesimo_ordem_inversa():
    valores = list(range(20, 0, -1))
    for k in range(len(valores)):
        assert selecionar_kesimo(list(valores), k) == sorted(valores)[k]


def test_selecionar_kesimo_com_duplicatas():
    valores = [5, 5, 5, 1, 1, 2, 3]
    for k in range(len(valores)):
        assert selecionar_kesimo(list(valores), k) == sorted(valores)[k]