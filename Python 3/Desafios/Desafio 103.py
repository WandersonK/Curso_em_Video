"""Faça um programa que tenha uma função chamada ficha(), que receba dois parâmentros opcionais: o nome de um jogador e
quantos gols ele marcou.
O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha sido informado corretamente."""

def ficha(nome='<desconhecido>', gols=0):
    
    print(f'O jogador {nome} fez {gols} gol(s) no campeonato.')


nome_jogador = input('Nome do Jogador: ')
gols_jogador = input('Número de Gols: ')

if nome_jogador.strip() != '' and gols_jogador.strip() != '':
    ficha(nome_jogador, int(gols_jogador))
elif nome_jogador.strip() == '' and gols_jogador.strip() != '':
    ficha(gols=int(gols_jogador))
elif nome_jogador.strip() != '' and gols_jogador.strip() == '':
    ficha(nome=nome_jogador)
else:
    ficha()
