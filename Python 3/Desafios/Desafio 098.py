"""Faça um programa que tenha uma função chamada contador(),
que receba três parâmetros: início, fim e passo e realize a contagem.
Seu programa tem que realizar três contagens através da função criada:
a) De 1 até 10, de 1 em 1
b) De 10 até 0, de 2 em 2
c) Uma contagem personalizada.
"""

from time import sleep


def contador(i, f, p):
    print('-=' * 30)
    print(f'Contagem de {i} até {f} de ', end='')

    if p == 0 and i < f:
        p = 1
    elif p == 0 and i > f:
        p = -1

    if p < 0:
        print(f'{-p} em {-p}')

    else:
        print(f'{p} em {p}')

    if i < f:
        f += 1
        if p < 0:
            p = -p
    elif i > f:
        f -= 1
        if p > 0:
            p = -p

    for cont in range(i, f, p):
        print(cont, end=' ', flush=True)
        sleep(0.1)
    print('FIM!')


# Programa Principal

contador(1, 10, 1)
contador(10, 0, 2)

print('-=' * 30)
print('Agora é a sua vez de personalizar a contagem!')
ini = int(input(f'{"Início:":<8}'))
fim = int(input(f'{"Fim:":<8}'))
passo = int(input(f'{"Passo:":<8}'))

contador(ini, fim, passo)


# Forma do Guanabara

def contador_g(i, f, p):
    if p < 0:
        p *= -1
    if p == 0:
        p = 1
    print('-=' * 20)
    print(f'Contagem de {i} até {f} de {p} em {p}')
    sleep(2.5)

    if i < f:
        cont = i
        while cont <= f:
            print(f'{cont} ', end='', flush=True)
            sleep(0.5)
            cont += p
        print('FIM!')
    else:
        cont = i
        while cont >= f:
            print(f'{cont} ', end='', flush=True)
            sleep(0.5)
            cont -= p
        print('FIM!')


# Programa Principal
contador_g(1, 10, 1)
contador_g(10, 0, 2)
print('-=' * 20)
print('Agora é a sua vez de personalizar a contagem!')
ini = int(input('Início: '))
fim = int(input('Fim:    '))
pas = int(input('Passo:  '))
contador_g(ini, fim, pas)
