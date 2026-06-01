import random

from src.app.median_of_medians import calcular_p50, selecionar_kesimo


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


def test_p50_lista_vazia():
    assert calcular_p50([]) is None


def test_p50_elemento_unico():
    assert calcular_p50([7]) == 7


def test_p50_quantidade_impar():
    assert calcular_p50([3, 1, 4, 1, 5]) == 3


def test_p50_quantidade_par():
    assert calcular_p50([1, 2, 3, 4]) == 2.5


def test_p50_estavel_com_outliers():
    base = [100] * 98
    outliers = [10000, 20000]
    valores = base + outliers
    p50 = calcular_p50(valores)
    media = sum(valores) / len(valores)
    assert p50 < media


def test_selecionar_kesimo_lista_grande_aleatoria():
    random.seed(42)
    valores = [random.randint(0, 10000) for _ in range(2000)]
    posicoes = [0, 1, len(valores) // 4, len(valores) // 2, len(valores) - 2, len(valores) - 1]
    for k in posicoes:
        assert selecionar_kesimo(list(valores), k) == sorted(valores)[k]
