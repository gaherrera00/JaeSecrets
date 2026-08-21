import os
from pathlib import Path
from .wordlist import remover_acentos

_DIRETORIO_PROJETO = Path(__file__).resolve().parent.parent
CAMINHO_PADRAO = _DIRETORIO_PROJETO / "data" / "blacklist"


def carregar_blacklist(caminho: str | Path = CAMINHO_PADRAO) -> set[str]:
    caminho = Path(caminho)
    if not caminho.is_dir():
        raise FileNotFoundError(f"Pasta de blacklist não encontrada: '{caminho}'.")

    palavras: set[str] = set()
    for arquivo in caminho.glob("*.txt"):
        with open(arquivo, encoding="utf-8", errors="ignore") as f:
            for linha in f:
                linha = linha.strip().lower()
                if linha:
                    palavras.add(remover_acentos(linha))

    if not palavras:
        raise ValueError(f"A blacklist em '{caminho}' está vazia.")

    return palavras


_blacklist_cache: set[str] | None = None


def _get_blacklist() -> set[str]:
    global _blacklist_cache
    if _blacklist_cache is None:
        _blacklist_cache = carregar_blacklist()
    return _blacklist_cache


def palavra_proibida(palavra: str) -> bool:
    return remover_acentos(palavra.lower()) in _get_blacklist()
