def _ordenacao_insercao(arr):
    for i in range(1, len(arr)):
        chave = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > chave:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = chave
    return arr


def _mediana_do_grupo(grupo):
    grupo_ordenado = _ordenacao_insercao(list(grupo))
    return grupo_ordenado[len(grupo_ordenado) // 2]


def selecionar_kesimo(valores, k):
    if len(valores) == 1:
        return valores[0]

    grupos = [valores[i:i+5] for i in range(0, len(valores), 5)]
    medianas = [_mediana_do_grupo(g) for g in grupos]

    if len(medianas) == 1:
        pivo = medianas[0]
    else:
        pivo = selecionar_kesimo(medianas, len(medianas) // 2)

    menores = [x for x in valores if x < pivo]
    maiores = [x for x in valores if x > pivo]
    iguais = [x for x in valores if x == pivo]

    if k < len(menores):
        return selecionar_kesimo(menores, k)
    elif k < len(menores) + len(iguais):
        return pivo
    else:
        return selecionar_kesimo(maiores, k - len(menores) - len(iguais))


def calcular_p50(valores):
    if not valores:
        return None
    n = len(valores)
    if n % 2 == 1:
        return selecionar_kesimo(list(valores), n // 2)
    else:
        inferior = selecionar_kesimo(list(valores), n // 2 - 1)
        superior = selecionar_kesimo(list(valores), n // 2)
        return (inferior + superior) / 2