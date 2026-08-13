from wordfreq import top_n_list

ACENTOS = str.maketrans("áàâãäéèêëíìîïóòôõöúùûüç", "aaaaaeeeeiiiiooooouuuuc")


def remover_acentos(texto):
    return texto.translate(ACENTOS)


palavras = set(top_n_list("pt", 50000))
palavras = {p for p in palavras if 4 <= len(p) <= 10}
palavraFiltrada = list({remover_acentos(p).lower() for p in palavras})
