from .mutation import mutacoes_funcoes
from .recipe import gerar_receita, lista_palavras
from .blacklist import palavra_proibida


def aplicar_receita(palavra: str, receita: list[tuple[str, int]]) -> str:
    for nome, qtd in receita:
        palavra = mutacoes_funcoes[nome](palavra, qtd)
    return palavra


def mutar_com_seguranca(palavra: str) -> str:
    while True:
        receita = gerar_receita()
        mutada = aplicar_receita(palavra, receita)
        if not palavra_proibida(mutada):
            return mutada


def gerar_senha() -> str:
    while True:
        palavras = lista_palavras()
        mutadas = [mutar_com_seguranca(p) for p in palavras]
        senha = "".join(mutadas)
        if not palavra_proibida(senha):
            return senha
