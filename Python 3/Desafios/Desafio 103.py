"""Faça um programa que tenha uma função chamada ficha(), que receba dois parâmentros opcionais: o nome de um jogador e
quantos gols ele marcou.
O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha sido informado corretamente."""


def ficha(nome='<desconhecido>', gols=0):
    
    print(f'O jogador {nome} fez {gols} gol(s) no campeonato.')


# Programa Principal
nome_jogador = input('Nome do Jogador: ')
gols_jogador = input('Número de Gols: ')

if nome_jogador.strip() != '' and gols_jogador.strip() != '':
    if gols_jogador.strip().isnumeric():
        ficha(nome_jogador, int(gols_jogador))
    else:
        ficha(nome=nome_jogador)
elif nome_jogador.strip() == '' and gols_jogador.strip() != '':
    if gols_jogador.strip().isnumeric():
        ficha(gols=int(gols_jogador))
    else:
        ficha()
elif nome_jogador.strip() != '' and gols_jogador.strip() == '':
    ficha(nome=nome_jogador)
else:
    ficha()



# Forma do Guanabara
def ficha_g(jog='<desconhecido>', gol=0):
    print(f'O jogador {jog} fez {gol} gol(s) no campeonato.')

# Programa Principal
n = str(input("Nome do Jogador: "))
g = str(input("Número de Gols: "))
if g.isnumeric():
    g = int(g)
else:
    g = 0
if n.strip() == '':
    ficha_g(gol=g)
else:
    ficha_g(n, g)
