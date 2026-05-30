# Motor de Metricas e Dashboard APM P50

Projeto da disciplina Projeto de Algoritmos para demonstrar o calculo do P50 de latencias usando o algoritmo Mediana das Medianas.

## Objetivo

Construir uma API em Python com interface web integrada para simular requisicoes de servidores e acompanhar metricas de performance, com foco na mediana como alternativa robusta a media quando existem outliers.

## Estrutura inicial

```text
src/app/
  main.py
  api.py
  metrics.py
  median_of_medians.py
  simulator.py
  storage.py
  static/
    index.html
    styles.css
    app.js
tests/
  test_median_of_medians.py
  test_metrics.py
```

## Como executar futuramente

```bash
pip install -r requirements.txt
uvicorn src.app.main:app --reload
```

## Status

Estrutura inicial criada para o desenvolvimento do MVP.
