import secrets
from mutation import mutacoes, mutacoes_funcoes
from wordlist import palavraFiltrada
from blacklist import palavra_proibida


def gerarReceita(minimo=1, teto_min=1, teto_max=2):
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


def mutarComSeguranca(palavra):
    while True:
        receita = gerarReceita()
        mutada = aplicarReceita(palavra, receita)
        if not palavra_proibida(mutada):
            return mutada


def gerarSenha():
    while True:
        palavras = listaPalavras()
        mutadas = [mutarComSeguranca(palavra) for palavra in palavras]
        senha = "".join(mutadas)
        if not palavra_proibida(senha):
            return senha


if __name__ == "__main__":
    print(gerarSenha())