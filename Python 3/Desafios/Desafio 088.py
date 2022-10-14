"""Faça um programa que ajude um jogador da MEGA SENA a criar palpites.
O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.
"""

from time import sleep
from random import randint

lista_palpites = []

print('-' * 30)
print(f'{"JOGA NA MEGA SENA":^30}')
print('-' * 30)

qtd_jogos = int(input('Quantos jogos você quer que eu sorteie? '))

print(f'-=-=-=  SORTEANDO {qtd_jogos} JOGOS  -=-=-=')

for i in range(0, qtd_jogos):
    
    while len(lista_palpites) < 6:
        num = randint(1, 60)
        if num not in lista_palpites:
            lista_palpites.append(num)
    
    print(f'Jogo {i + 1}: {sorted(lista_palpites)}')
    
    lista_palpites.clear()
    
    sleep(1)

print('-=-=-=-=-= < BOA SORTE! > -=-=-=-=-=')


# Forma do Guanabara

lista = list()
jogos = list()
print('-' * 30)
print('      JOGA NA MEGA SENA      ')
print('-' * 30)
quant = int(input('Quantos jogos você quer que eu sorteie? '))
tot = 1
while tot <= quant:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot += 1
print('-=' * 3, f' SORTEANDO {quant} JOGOS ', '-=' * 3)
for i, l in enumerate(jogos):
    print(f'Jogo {i+1}: {l}')
    sleep(1)
print('-=' * 5, '< BOA SORTE! >', '-=' * 5)
