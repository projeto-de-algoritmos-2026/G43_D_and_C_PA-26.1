from src.app.metrics import calcular_media, resumir_latencias
from src.app.median_of_medians import calcular_p50


def test_calcular_p50_com_outlier_permanece_estavel():
    valores = [100, 101, 102, 103, 104, 2500]

    assert calcular_p50(valores) == 102.5
    assert calcular_media(valores) > 480


def test_resumir_latencias_vazio():
    assert resumir_latencias([]) == {
        "count": 0,
        "p50_ms": None,
        "average_ms": None,
        "min_ms": None,
        "max_ms": None,
    }


def test_resumir_latencias_arredonda_valores():
    resumo = resumir_latencias([10.123, 20.456, 30.789])

    assert resumo["count"] == 3
    assert resumo["p50_ms"] == 20.46
    assert resumo["average_ms"] == 20.46
    assert resumo["min_ms"] == 10.12
    assert resumo["max_ms"] == 30.79
