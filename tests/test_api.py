from fastapi.testclient import TestClient

from src.app.api import store
from src.app.main import app

client = TestClient(app)


def setup_function():
    store.reset()


def test_metricas_iniciam_vazias():
    response = client.get("/api/metrics")

    assert response.status_code == 200
    data = response.json()
    assert data["count"] == 0
    assert data["p50_ms"] is None
    assert data["recent_ms"] == []


def test_simulacao_adiciona_latencias():
    response = client.post("/api/simulate?count=25&outlier_probability=0")

    assert response.status_code == 200
    data = response.json()
    assert data["inserted"] == 25
    assert data["count"] == 25
    assert len(data["recent_ms"]) == 25
    assert data["p50_ms"] is not None


def test_reset_limpa_metricas():
    client.post("/api/simulate?count=10")
    response = client.post("/api/reset")

    assert response.status_code == 200
    assert response.json()["count"] == 0
