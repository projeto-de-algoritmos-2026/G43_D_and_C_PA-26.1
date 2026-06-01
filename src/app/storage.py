"""Armazenamento em memoria das latencias recentes."""

from __future__ import annotations

from collections import deque
from threading import Lock
from typing import Iterable


class LatencyStore:
    """Mantem uma janela limitada das latencias mais recentes."""

    def __init__(self, max_size: int = 10_000) -> None:
        if max_size <= 0:
            raise ValueError("max_size must be positive")
        self._latencies: deque[float] = deque(maxlen=max_size)
        self._lock = Lock()

    def add_many(self, latencies: Iterable[float]) -> int:
        """Adiciona latencias e retorna quantos valores foram inseridos."""
        values = [float(latency) for latency in latencies]
        with self._lock:
            self._latencies.extend(values)
        return len(values)

    def list_all(self) -> list[float]:
        """Retorna um snapshot seguro da janela atual."""
        with self._lock:
            return list(self._latencies)

    def reset(self) -> None:
        """Remove todas as latencias armazenadas."""
        with self._lock:
            self._latencies.clear()
