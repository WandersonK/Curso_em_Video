"""Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista.
No final, mostre:
A) Quantas pessoas foram cadastradas.
B) A média de idade do grupo.
C) Uma lista com todas as mulheres.
D) Uma lista com todas as pessoas com idade acima da média.
"""

pessoa = dict()
pessoas_lista = list()
media_idade = 0

while True:
    pessoa['nome'] = str(input('Nome: '))
    
    while True:
        pessoa['sexo'] = str(input('Sexo: [M/F] ')).upper()[0]
        
        if pessoa['sexo'] in 'MF':
            break
        print('ERRO! Por favor, digite apenas M ou F.')
    
    pessoa['idade'] = int(input('Idade: '))
    
    pessoas_lista.append(pessoa.copy())
    pessoa.clear()
    
    while True:
        continuar = input('Deseja continuar? [S/N] ').strip()[0]
        
        if continuar in 'NnSs':
            break
        print('ERRO! Responda apenas S ou N.')
    
    if continuar in 'Nn':
        break

print('-=' * 30)
print(f'- Foram cadastradas {len(pessoas_lista)} pessoas.')

for idade in pessoas_lista:
    media_idade += idade['idade']

media_idade = media_idade / len(pessoas_lista)

print(f'- A idade média do grupo é {media_idade:.2f} anos.')

print(f'- As mulheres cadastradas foram: ', end='')

for mulheres in pessoas_lista:
    if mulheres['sexo'] == 'F':
        print(mulheres['nome'], end=' ')
print()

print(f'- As pessoas acima da média são:')

for acima_media in pessoas_lista:
    if acima_media['idade'] > media_idade:
        for chave, valor in acima_media.items():
            print(f'{chave} = {valor};', end=' ')
        print()
        
print('<< ENCERRADO >>')


# Forma do Guanabara

galera = list()
pessoa = dict()
soma = média = 0
while True:
    pessoa.clear()
    pessoa['nome'] = str(input('Nome: '))
    while True:
        pessoa['sexo'] = str(input('Sexo: [M/F] ')).upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        print('ERRO! Por favor, digite apenas M ou F.')
    pessoa['idade'] = int(input('Idade: '))
    soma += pessoa['idade']
    galera.append(pessoa.copy())
    while True:
        resp = str(input('Quer continuar? [S/N] ')).upper()[0]
        if resp in 'SN':
            break
        print('ERRO! Responda apenas S ou N.')
    if resp == 'S':
        break
print('-=' * 30)
print(f'A) Ao todo temos {len(galera)} pessoas cadastradas.')
média = soma / len(galera)
print(f'B) A média de idade é de {média:5.2f} anos.')
print('C) As mulheres cadastradas foram ', end='')
for p in galera:
    if p['sexo'] in 'Ff':
        print(f'{p["nome"]} ', end='')
print()
print('D) Lista das pessoas que estão acima da média: ')
for p in galera:
    if p['idade'] >= média:
        print('     ')
        for k, v in p.items():
            print(f'{k} = {v};', end='')
        print()
print('<< ENCERRADO >>')
