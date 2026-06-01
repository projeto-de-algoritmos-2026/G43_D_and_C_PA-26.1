"""Funcoes para calculo das metricas de latencia."""

from __future__ import annotations

from typing import Sequence

from .median_of_medians import calcular_p50


def calcular_media(latencias: Sequence[float]) -> float | None:
    if not latencias:
        return None
    return sum(latencias) / len(latencias)


def resumir_latencias(latencias: Sequence[float]) -> dict[str, float | int | None]:
    if not latencias:
        return {
            "count": 0,
            "p50_ms": None,
            "average_ms": None,
            "min_ms": None,
            "max_ms": None,
        }

    return {
        "count": len(latencias),
        "p50_ms": round(calcular_p50(latencias), 2),
        "average_ms": round(calcular_media(latencias), 2),
        "min_ms": round(min(latencias), 2),
        "max_ms": round(max(latencias), 2),
    }
