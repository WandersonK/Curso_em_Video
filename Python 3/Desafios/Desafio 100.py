"""Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteio() e somaPar().
A primeira função vai sortear 5 números e vai colocá-los dentro da lista e a segunda função vai mostrar a soma entre
todos os valores PARES sorteados pela função anterior."""

from random import randint
from time import sleep

números = list()


def soma_par(lista):
    par_sum = 0

    for num in lista:
        if num % 2 == 0:
            par_sum += num

    print(f'Somando os valores pares de {lista}, temos {par_sum}')


def sorteio():
    print('Sorteando 5 valores da lista: ', end='')

    for num in range(0, 5):
        números.append(randint(1, 10))
        print(números[num], end=' ', flush=True)
        sleep(0.4)

    print('PRONTO!')

    soma_par(números)


sorteio()


# Forma do Guanabara
def sorteia(lista):
    print('Sorteando 5 valores da lista: ', end='')
    for cont in range(0, 5):
        n = randint(1, 10)
        lista.append(n)
        print(f'{n} ', end='', flush=True)
        sleep(0.3)
    print('PRONTO!')


def somaPar(lista):
    soma = 0
    for valor in lista:
        if valor % 2 == 0:
            soma += valor
    print(f'Somando os valores pares de {lista}, temos {soma}')


números = list()
sorteia(números)
somaPar(números)
