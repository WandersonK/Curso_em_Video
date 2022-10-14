"""Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios.
Guarde esses resultados em um dicionário. No final, coloque esse dicionário em ordem,
sabendo que o vencedor tirou o maior número no dado.
"""

from random import randint
from time import sleep
jogadas = dict()

print('Valores sorteados:')

for i in range(1, 5):
    jogadas[f'jogador{i}'] = randint(1, 6)
    print(f'   O jogador{i} tirou {jogadas[f"jogador{i}"]}')
    sleep(0.9)

print('-=' * 30)
print('Ranking dos jogadores:')

for indice, jogada in enumerate(sorted(jogadas.values())):
    contador = 0
    while contador < len(jogadas.items()):
        if jogada == list(jogadas.items())[contador][1]:
            print(f'   {indice + 1}º lugar: {list(jogadas.items())[contador][0]} com {jogada}')
            sleep(0.9)
            del jogadas[f'{list(jogadas.items())[contador][0]}']
        contador += 1

print()
# Forma do Guanabara
from operator import itemgetter
jogo = {'jogador1': randint(1, 6),
        'jogador2': randint(1, 6),
        'jogador3': randint(1, 6),
        'jogador4': randint(1, 6)}
ranking = list()
print('Valores sorteados:')
for k, v in jogo.items():
    print(f'   {k} tirou {v} no dado.')
    sleep(1)
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
print('-=' * 30)
print('  == RANKING DOS JOGADORES == ')
for i, v in enumerate(ranking):
    print(f'   {i + 1}º lugar: {v[0]} com {v[1]}.')
    sleep(1)
