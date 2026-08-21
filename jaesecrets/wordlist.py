from wordfreq import top_n_list

ACENTOS = str.maketrans(
    "áàâãäéèêëíìîïóòôõöúùûüç",
    "aaaaaeeeeiiiiooooouuuuc",
)


def remover_acentos(texto: str) -> str:
    return texto.translate(ACENTOS)


_palavras_cache: list[str] | None = None


def carregar_palavras(
    min_len: int = 4, max_len: int = 10, top_n: int = 50000
) -> list[str]:
    global _palavras_cache
    if _palavras_cache is not None:
        return _palavras_cache

    palavras = top_n_list("pt", top_n)
    filtradas = {
        remover_acentos(p).lower()
        for p in palavras
        if min_len <= len(p) <= max_len and p.isalpha()
    }
    _palavras_cache = list(filtradas)
    return _palavras_cache


@property
def palavraFiltrada():
    return carregar_palavras()
