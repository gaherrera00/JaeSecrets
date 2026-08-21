import secrets

SIMBOLOS = "!@#$&*-_"
_rand = secrets.SystemRandom()


def MaiusculoAleatorio(palavra: str, qtd: int = 1) -> str:
    if not palavra:
        return palavra
    qtd = min(qtd, len(palavra))
    idx = set(_rand.sample(range(len(palavra)), qtd))
    return "".join(c.upper() if i in idx else c for i, c in enumerate(palavra))


def InserirNumero(palavra: str, qtd: int = 1) -> str:
    for _ in range(qtd):
        if not palavra:
            break
        pos = _rand.randrange(1, len(palavra) + 1)
        palavra = palavra[:pos] + str(_rand.randrange(10)) + palavra[pos:]
    return palavra


def InserirSimbolo(palavra: str, qtd: int = 1) -> str:
    for _ in range(qtd):
        if not palavra:
            break
        pos = _rand.randrange(1, len(palavra) + 1)
        palavra = palavra[:pos] + _rand.choice(SIMBOLOS) + palavra[pos:]
    return palavra


def LetraPraNumero(palavra: str, qtd: int = 1) -> str:
    mapa = {"a": "4", "e": "3", "i": "1", "o": "0", "s": "5", "g": "9", "b": "8"}
    alvos = [i for i, c in enumerate(palavra) if c.lower() in mapa]
    if not alvos:
        return palavra
    escolhidos = set(_rand.sample(alvos, min(qtd, len(alvos))))
    return "".join(
        mapa[c.lower()] if i in escolhidos else c for i, c in enumerate(palavra)
    )


def CamelCase(palavra: str, qtd: int = 1) -> str:
    if not palavra:
        return palavra
    idx = set(_rand.sample(range(len(palavra)), min(qtd, len(palavra))))
    return "".join(c.upper() if i in idx else c.lower() for i, c in enumerate(palavra))


def PalavraMaiuscula(palavra: str, qtd: int = 1) -> str:
    if not palavra:
        return palavra
    idx = set(_rand.sample(range(len(palavra)), min(qtd, len(palavra))))
    return "".join(c.upper() if i in idx else c.lower() for i, c in enumerate(palavra))


def InverteLetras(palavra: str, qtd: int = 1) -> str:
    lista = list(palavra)
    n = min(qtd, len(lista) // 2)
    for _ in range(n):
        if len(lista) < 2:
            break
        i, j = _rand.sample(range(len(lista)), 2)
        lista[i], lista[j] = lista[j], lista[i]
    return "".join(lista)


def DuplicarLetra(palavra: str, qtd: int = 1) -> str:
    for _ in range(qtd):
        if not palavra:
            break
        pos = _rand.randrange(len(palavra))
        palavra = palavra[:pos] + palavra[pos] + palavra[pos:]
    return palavra


def LetraParaSimbolo(palavra: str, qtd: int = 1) -> str:
    mapa = {"a": "@", "s": "$", "i": "!", "o": "*", "e": "€"}
    alvos = [i for i, c in enumerate(palavra) if c.lower() in mapa]
    if not alvos:
        return palavra
    escolhidos = set(_rand.sample(alvos, min(qtd, len(alvos))))
    return "".join(
        mapa[c.lower()] if i in escolhidos else c for i, c in enumerate(palavra)
    )


# Registro de funções
mutacoes_funcoes = {
    "MaiusculoAleatorio": MaiusculoAleatorio,
    "InserirNumero": InserirNumero,
    "InserirSimbolo": InserirSimbolo,
    "LetraPraNumero": LetraPraNumero,
    "CamelCase": CamelCase,
    "PalavraMaiuscula": PalavraMaiuscula,
    "InverteLetras": InverteLetras,
    "DuplicarLetra": DuplicarLetra,
    "LetraParaSimbolo": LetraParaSimbolo, 
}

# Intervalos de sorteio (0-99) e faixa de quantidade (min, max)
mutacoes = {
    "MaiusculoAleatorio": ((0, 29), 1, 6),
    "InserirNumero": ((30, 49), 1, 3),
    "InserirSimbolo": ((50, 64), 0, 2),
    "LetraPraNumero": ((65, 74), 0, 2),
    "CamelCase": ((75, 84), 1, 1),
    "PalavraMaiuscula": ((85, 89), 1, 1),
    "InverteLetras": ((90, 93), 0, 1),
    "DuplicarLetra": ((94, 96), 0, 1),
    "LetraParaSimbolo": ((97, 99), 0, 1),
}
