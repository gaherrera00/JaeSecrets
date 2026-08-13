import os


def carregar_blacklist(caminho):
    palavras = set()
    for arquivo in os.listdir(caminho):
        if not arquivo.endswith(".txt"):
            continue
        with open(
            os.path.join(caminho, arquivo), encoding="utf-8", errors="ignore"
        ) as f:
            for linha in f:
                linha = linha.strip().lower()
                if linha:
                    palavras.add(linha)
    return palavras


blacklist = carregar_blacklist("listaNegra")


def palavra_proibida(palavra_mutada):
    return palavra_mutada.lower() in blacklist
