"""Rotas da API de metricas e simulacao."""

from __future__ import annotations

from fastapi import APIRouter, Query

from .metrics import resumir_latencias
from .simulator import gerar_latencias
from .storage import LatencyStore

router = APIRouter(prefix="/api", tags=["metricas"])
store = LatencyStore(max_size=10_000)


@router.get("/metrics")
def obter_metricas() -> dict[str, object]:
    latencias = store.list_all()
    return {
        **resumir_latencias(latencias),
        "recent_ms": latencias[-60:],
    }


@router.post("/simulate")
def simular_requisicoes(
    count: int = Query(default=1_000, ge=1, le=10_000),
    outlier_probability: float = Query(default=0.02, ge=0, le=1),
) -> dict[str, object]:
    geradas = gerar_latencias(
        quantidade=count,
        probabilidade_outlier=outlier_probability,
    )
    inseridas = store.add_many(geradas)
    latencias = store.list_all()
    return {
        "inserted": inseridas,
        **resumir_latencias(latencias),
        "recent_ms": latencias[-60:],
    }


@router.post("/reset")
def limpar_metricas() -> dict[str, object]:
    store.reset()
    return resumir_latencias([])
