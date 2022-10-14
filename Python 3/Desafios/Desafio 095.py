"""Aprimore o DESAFIO 093 para que ele funcione com vários jogadores, incluindo um sistema de visualização de detalhes do
aproveitamento de cada jogador."""

informacoes = dict()
lista_geral = list()
separador = '-=' * 30

while True:
    gols = []
    total_gols = 0
    
    print('-' * 33)
    informacoes['nome'] = str(input('Qual nome do Jogador? '))
    n_partidas = int(input(f'Quantas partidas {informacoes["nome"]} jogou? '))

    for i in range(0, n_partidas):
        gols.append(int(input(f'Quantos gols na {i + 1}º partida? ')))
        total_gols += gols[i]

    informacoes['gols'] = gols[:]
    informacoes['total'] = total_gols

    lista_geral.append(informacoes.copy())
    informacoes.clear()
    
    while True:
        continuar = input('Deseja continuar? [S/N] ').strip()[0]
        
        if continuar in 'NnSs':
            break
        print('ERRO! Responda apenas S ou N.')
        
    if continuar in 'Nn':
        break
    
print(separador)

print(f'cod {"nome":<17} {"gols":<17} total')
print('-' * 45)

for chave, valor in enumerate(lista_geral):
    print(f'{chave:>3} {valor["nome"]:17} {str(valor["gols"]):17} {valor["total"]}')

while True:
    print('-' * 45)
    escolha_jogador = int(input('Mostrar dados de qual jogador? (999 para sair) '))
    
    if escolha_jogador == 999:
        break
    
    elif escolha_jogador in range(0, len(lista_geral)):
        print(f'-- LEVANTAMENTO DO JOGADOR {lista_geral[escolha_jogador]["nome"]}:')
        for chave, valor_gol in enumerate(lista_geral[escolha_jogador]['gols']):
            print(f'   No jogo {chave + 1} fez {valor_gol} gols.')
    else:
        print(f'ERRO! Não existe jogador com o código {escolha_jogador}! Tente novamente')
    
print('<< VOLTE SEMPRE >>')


# Forma do Guanabara

time = list()
jogador = dict()
partidas = list()

while True:
    jogador.clear()
    jogador['nome'] = str(input('Nome do Jogador: '))
    tot = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    partidas.clear()
    for c in range(0, tot):
        partidas.append(int(input(f'    Quantos gols na partida {c}? ')))
    jogador['gols'] = partidas[:]
    jogador['total'] = sum(partidas)
    time.append(jogador.copy())
    while True:
        resp = str(input('Quer continuar? [S/N] ')).upper()[0]
        if resp in 'SN':
            break
        print('ERRO! Responda apenas S ou N.')
    if resp == 'N':
        break
print('-=' * 30)
print('cod ', end='')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()
print('-' * 40)
for k, v in enumerate(time):
    print(f'{k:>3} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('-' * 40)
while True:
    busca = int(input('Mostrar dados de qual jogador? (999 para parar) '))
    if busca == 999:
        break
    if busca >= len(time):
        print(f'ERRO! Não existe jogador com código {busca}!')
    else:
        print(f' -- LEVANTAMENTO DO JOGADOR {time[busca]["nome"]}:')
        for i, g in enumerate(time[busca]['gols']):
            print(f'    No jogo {i + 1} fez {g} gols.')
    print('-' * 40)
print('<< VOLTE SEMPRE >>')
