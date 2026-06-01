"""Gerador de latencias simuladas para o dashboard."""

from __future__ import annotations

import random


def gerar_latencias(
    quantidade: int = 1_000,
    base_ms: float = 120.0,
    variacao_ms: float = 35.0,
    probabilidade_outlier: float = 0.02,
) -> list[float]:
    if quantidade < 0:
        raise ValueError("quantidade deve ser maior ou igual a zero")
    if base_ms <= 0:
        raise ValueError("base_ms deve ser positivo")
    if variacao_ms < 0:
        raise ValueError("variacao_ms nao pode ser negativa")
    if not 0 <= probabilidade_outlier <= 1:
        raise ValueError("probabilidade_outlier deve estar entre 0 e 1")

    latencias = []
    for _ in range(quantidade):
        if random.random() < probabilidade_outlier:
            latencia = random.uniform(900.0, 2_500.0)
        else:
            latencia = random.gauss(base_ms, variacao_ms)
        latencias.append(round(max(1.0, latencia), 2))
    return latencias
