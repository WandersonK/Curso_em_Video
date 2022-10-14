"""Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta.
No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.
"""

lista_geral = []

while True:
    temp_nome = []
    temp_notas = []
    
    temp_nome.append(str(input('Nome: ')))
    temp_notas.append(float(input('Nota 1: ')))
    temp_notas.append(float(input('Nota 2: ')))
    
    temp_nome.append(temp_notas[:])
    lista_geral.append(temp_nome[:])

    continuar = str(input('Quer continuar? [S/N] '))[0].strip()
    
    if continuar in 'Nn':
        break
    
print('-=' * 35)

print('No. NOME         MÉDIA')
print('-' * 25)

for indice, dado in enumerate(lista_geral):
    soma = 0
    
    print(f'{indice: <4}', end='')
    print(f'{dado[0]: <15}', end='')
    
    for notas in dado[1]:
        soma += notas
        
    print(f'{soma/2:.1f}')
    
while True:
    print('-' * 35)
    mostra_nota = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    
    if mostra_nota == 999:
        print('FINALIZANDO...')
        print('<<< VOLTE SEMPRE >>>')
        break
    
    if mostra_nota in range(0, len(lista_geral)):
        print(f'Notas de {lista_geral[mostra_nota][0]} são {lista_geral[mostra_nota][1]}')
    else:
        print('Por favor, informe um índice válido!')


# Forma do Guanabara

ficha = list()
while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    ficha.append([nome, [nota1, nota2], media])
    resp = str(input('Quer continuar? [S/N] '))
    if resp in 'Nn':
        break
print('-=' * 30)
print(f'{"No.":<4}{"NOME":<10}{"MÉDIA":>8}')
print('-' * 26)
for i, a in enumerate(ficha):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
while True:
    print('-' * 35)
    opc = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    if opc == 999:
        print('FINALIZANDO...')
        break
    if opc <= len(ficha) - 1:
        print(f'Notas de {ficha[opc][0]} são {ficha[opc][1]}')
print('<<< VOLTE SEMPRE >>>')