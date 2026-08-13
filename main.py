import secrets
from mutation import mutacoes, mutacoes_funcoes
from wordlist import palavraFiltrada


def gerarReceita(minimo=2, teto_min=2, teto_max=3):
    teto = teto_min + secrets.randbelow(teto_max - teto_min + 1)
    receitaMutacoes = []
    intensidade = 0

    while len(receitaMutacoes) < minimo or intensidade < teto:
        sorteio = secrets.randbelow(100)

        for nome, ((lo, hi), qmin, qmax) in mutacoes.items():
            if lo <= sorteio <= hi:
                qtd = max(1, qmin + secrets.randbelow(qmax - qmin + 1))
                receitaMutacoes.append((nome, qtd))
                intensidade += qtd
                break
    return receitaMutacoes


def listaPalavras(minimo=5, maximo=7):
    receitaPalavras = []
    numeroPalavras = minimo + secrets.randbelow(maximo - minimo + 1)
    for i in range(numeroPalavras):
        indice = secrets.randbelow(len(palavraFiltrada))
        palavra = palavraFiltrada[indice]
        receitaPalavras.append(palavra)
    return receitaPalavras


def aplicarReceita(palavra, receita):
    for nome, qtd in receita:
        palavra = mutacoes_funcoes[nome](palavra, qtd)
    return palavra


def gerarSenhaFinal():
    palavras = listaPalavras()

    mutadas = []
    for palavra in palavras:
        receita = gerarReceita()
        mutadas.append(aplicarReceita(palavra, receita))

    print("".join(mutadas))


gerarSenhaFinal()

"""
loop final pra mutacao do string global
def sortear_mutacoes_globais():
    # teto mais baixo para não bagunçar tudo de novo
    return {nome: rng.randint(0, 2) for nome in MUTACOES if rng.randint(0, 99) < 20}
"""
