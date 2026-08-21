
import secrets
from .mutation import mutacoes
from .wordlist import carregar_palavras


def gerar_receita(
    minimo: int = 1, teto_min: int = 1, teto_max: int = 2
) -> list[tuple[str, int]]:
    teto = teto_min + secrets.randbelow(teto_max - teto_min + 1)
    receita: list[tuple[str, int]] = []
    intensidade = 0

    while len(receita) < minimo or intensidade < teto:
        sorteio = secrets.randbelow(100)

        for nome, ((lo, hi), qmin, qmax) in mutacoes.items():
            if lo <= sorteio <= hi:
                qtd = max(1, qmin + secrets.randbelow(qmax - qmin + 1))
                receita.append((nome, qtd))
                intensidade += qtd
                break

    return receita


def lista_palavras(minimo: int = 5, maximo: int = 7) -> list[str]:
    palavras = carregar_palavras()
    numero = minimo + secrets.randbelow(maximo - minimo + 1)
    return [palavras[secrets.randbelow(len(palavras))] for _ in range(numero)]
