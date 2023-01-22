"""Crie um programa que tenha uma função fatorial() que receba dois parâmetros: o primeiro que indique o número a calcular
e o outro chamado show, que será um valor lógico (opcional) indicado se será mostrado ou não na tela o processo de cálculo do
fatorial."""

print('-' * 30)


def fatorial(num, show=False):
    """
    -> Calcula o Fatorial de um número.
    :param num: O número a ser calculado.
    :param show: (opcional) Mostra ou não a conta.
    :return: O valor do Fatorial de um número num.
    """
    
    f = 1
    for i in range(num, 0, -1):
        f *= i
        if show:
            if i != 1:
                print(f'{i}', end=' x ')
            else:
                print(f'{i}', end=' = ')

    return f


# Programa Principal
print(fatorial(5, True))
help(fatorial)



# Forma do Guanabara
def fatorial_g(n, show=False):
    """
    -> Calcula o Fatorial de um número.
    :param n: O número a ser calculado.
    :param show: (opcional) Mostra ou não a conta.
    :return: O valor do Fatorial de um número n.
    """
    f = 1
    for c in range(n, 0, -1):
        if show:
            print(c, end='')
            if c > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
        f *= c
    return f

# Programa Principal
print(fatorial_g(5, show=True))
help(fatorial_g)
