"""Crie um programa que gerencie o aproveitamento de um jogador de futebol.
O programa vai ler o nome do jogador e quantas partidas ele jogou.
Depois vai ler a quantidade de gols feitos em cada partida.
No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato."""

gols = []
total_gols = 0
informacoes = dict()
separador = '-=' * 30

informacoes['nome'] = str(input('Qual nome do Jogador? '))
n_partidas = int(input(f'Informe quantas partidas {informacoes["nome"]} jogou: '))

for i in range(0, n_partidas):
    gols.append(int(input(f'Quantos gols foram feitos na {i + 1}º partida? ')))
    total_gols += gols[i]

informacoes['gols'] = gols
informacoes['total'] = total_gols

print(separador)
print(informacoes)
print(separador)

for chave, valor in informacoes.items():
    print(f'O campo {chave} tem o valor {valor}.')

print(separador)

print(f'O jogador {informacoes["nome"]} jogou {n_partidas} partidas.')

for chave, gol in enumerate(gols):
    print(f'    => Na partida {chave + 1}, fez {gol} gols.')

print(f'Foi um total de {informacoes["total"]} gols.')


# Forma do Guanabara

jogador = dict()
partidas = list()
jogador['nome'] = str(input('Nome do Jogador: '))
tot = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
for c in range(0, tot):
    partidas.append(int(input(f'    Quantos gols na partida {c}? ')))
jogador['gols'] = partidas[:]
jogador['total'] = sum(partidas)
print('-=' * 30)
print(jogador)
print('-=' * 30)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}')
print('-=' * 30)
print(f'O jogador {jogador["nome"]} jogou {len(jogador["gols"])} partidas.')
for i, v in enumerate(jogador['gols']):
    print(f'    => Na partida {i}, fez {v} gols.')
print(f'Foi um total de {jogador["total"]} gols.')
