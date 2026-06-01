# Motor de Metricas e Dashboard APM P50

Projeto da disciplina Projeto de Algoritmos para demonstrar o calculo do P50 de latencias usando o algoritmo **Mediana das Medianas**.

## Objetivo

Construir uma API em Python com interface web integrada para simular requisicoes de servidores e acompanhar metricas de performance. O foco e mostrar por que a mediana e mais robusta que a media em cenarios de Application Performance Monitoring(APM), onde poucos timeouts podem distorcer a media.

## Funcionalidades

- API FastAPI com endpoints para metricas, simulacao e reset.
- Dashboard web servido pela propria aplicacao.
- Simulador de latencias com outliers configuraveis.
- Calculo de P50 usando Mediana das Medianas, sem ordenar a lista completa.
- Testes automatizados para algoritmo, metricas e rotas principais.

## Estrutura

```text
main.py
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
  test_api.py
  test_median_of_medians.py
  test_metrics.py
```

## Requisitos

- Python 3.10 ou superior
- pip

## Instalacao

```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

## Como executar

O jeito mais simples e pela raiz do projeto:

```bash
python main.py
```

Depois acesse:

```text
http://127.0.0.1:8000
```

Tambem e possivel executar diretamente com Uvicorn:

```bash
uvicorn src.app.main:app --reload
```

A documentacao automatica da API fica em:

```text
http://127.0.0.1:8000/docs
```

## Como o dashboard funciona

1. A tela inicial e servida pelo FastAPI em `/`.
2. Os arquivos de interface ficam em `src/app/static/`.
3. Ao clicar em `Simular 1k` ou `Simular 10k`, o JavaScript chama `POST /api/simulate`.
4. A API gera latencias simuladas, guarda em memoria e recalcula as metricas.
5. O dashboard busca `GET /api/metrics` a cada 5 segundos para atualizar P50, media, total, maximo e grafico.

## Endpoints principais

- `GET /api/metrics`: retorna metricas da janela atual.
- `POST /api/simulate?count=1000`: gera latencias simuladas.
- `POST /api/reset`: limpa os dados em memoria.

## Como testar

Execute na raiz do projeto:

```bash
pytest
```

Se o comando `pytest` nao for reconhecido, use:

```bash
python -m pytest
```

## Observacao sobre o algoritmo

A media simples e sensivel a outliers: uma unica requisicao com timeout pode elevar muito o resultado. O P50 representa o ponto central das latencias e, neste projeto, e calculado com selecao deterministica por Mediana das Medianas, que encontra a estatistica de ordem desejada em tempo linear no pior caso.
