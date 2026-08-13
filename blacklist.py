import os

diretorioAtual = os.path.dirname(os.path.abspath(__file__))
caminhoPadrao = os.path.join(diretorioAtual, "listaNegra")


def carregar_blacklist(caminho=caminhoPadrao):
    if not os.path.isdir(caminho):
        raise FileNotFoundError(f"Pasta de blacklist não encontrada: '{caminho}'.")

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

    if not palavras:
        raise ValueError(f"A blacklist em '{caminho}' está vazia.")

    return palavras


blacklist = carregar_blacklist()


def palavra_proibida(palavra_mutada):
    return palavra_mutada.lower() in blacklist