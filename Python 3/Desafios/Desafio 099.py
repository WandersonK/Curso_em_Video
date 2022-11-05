"""Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros.
Seu programa tem que analisar todos os valores e dizer qual deles é maior.
"""

from time import sleep


def maior(*nums):
    contador = 0
    maior_num = 0

    print('-=' * 30)
    print('Analisando os valores passados...')

    for n in nums:
        print(n, end=' ', flush=True)
        sleep(0.3)
        if contador == 0:
            maior_num = n
        if maior_num < n:
            maior_num = n
        contador += 1

    print(f'Foram informados {len(nums)} valores ao todo.')
    print(f'O maior valor informado foi {maior_num}.')


# Programa principal
maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()


# Forma do Guanabara

def maior_g(* núm):
    cont = maior = 0
    print('-=' * 30)
    print('Analisando os valores passados...')
    for valor in núm:
        print(f'{valor} ', end='', flush=True)
        sleep(0.3)
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont += 1
    print(f'Foram informados {cont} valores ao todo.')
    print(f'O maior valor informado foi {maior}.')


# Programa principal
maior_g(2, 9, 4, 5, 7, 1)
maior_g(4, 7, 0)
maior_g(1, 2)
maior_g(6)
maior_g()
