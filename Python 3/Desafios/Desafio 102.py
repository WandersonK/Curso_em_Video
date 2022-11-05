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
# print(fatorial(5))
help(fatorial)
