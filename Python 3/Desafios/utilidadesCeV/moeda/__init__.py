def aumentar(n, p, formatar=False):
    resultado = n * (1 + (p / 100))
    return verifica_formatacao(resultado, formatar)


def diminuir(n, p, formatar=False):
    resultado = n * (1 - (p / 100))
    return verifica_formatacao(resultado, formatar)


def dobro(n, formatar=False):
    resultado =  n * 2
    return verifica_formatacao(resultado, formatar)

def metade(n, formatar=False):
    resultado = n / 2
    return verifica_formatacao(resultado, formatar)


def moeda(n):
    return f'R${n:.2f}'.replace('.', ',')


def verifica_formatacao(resultado, formatar):
    if formatar:
        return moeda(resultado)
    else:
        return resultado


def resumo(n=0, mais=10, menos=5):
    print(f'{"-" * 30}\n{"RESUMO DO VALOR":^30}\n{"-" * 30}')
    print(f'{"Preço analisado:":<18} {moeda(n)}')
    print(f'{"Dobro do preço:":<18} {dobro(n, True)}')
    print(f'{"Metade do preço:":<18} {metade(n, True)}')
    print(f'{f"{mais}% de aumento:":<18} {aumentar(n, mais, True)}')
    print(f'{f"{menos}% de redução:":<18} {diminuir(n, menos, True)}')
    print('-' * 30)
