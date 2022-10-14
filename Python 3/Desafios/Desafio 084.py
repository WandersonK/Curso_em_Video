""" Faça um programa que leia nome e pesso de várias pessoas, guardando tudo em uma lista. No final, mostre:
A) Quantas pessoas foram cadastradas.
B) Uma listagem com as pessoas mais pesadas.
C) Uma listagem com as pessoas mais leves.
"""

list_pessoas = list()
dado = list()
pesos = list()

while True:
    dado.append(str(input('Nome: ')))
    dado.append(float(input('Peso: ')))
    list_pessoas.append(dado[:])
    pesos.append(dado[1])
    dado.clear()
    
    continuar = input('Deseja continuar? [S/N] ')[0].strip()
    
    while continuar not in 'NnSs':
        continuar = input('Opção inválida. Deseja continuar? [S/N] ')[0].strip()
    
    if continuar in 'Nn':
        break

print(f'Foram cadastradas {len(list_pessoas)} pessoas.')

maior_peso = max(pesos)
menor_peso = min(pesos)    

print(f'O maior peso foi de {maior_peso}Kg. Peso de ', end='')

for pessoa in list_pessoas:
    if pessoa[1] == maior_peso:
        print(f'[{pessoa[0]}]', end=' ')

print(f'\nO menor peso foi de {menor_peso}Kg. Peso de ', end='')

for pessoa in list_pessoas:
    if pessoa[1] == menor_peso:
        print(f'[{pessoa[0]}]', end=' ')


# Forma do Guanabara

temp = []
princ = []
mai = men = 0
while True:
    temp.append(str(input('Nome: ')))
    temp.append(float(input('Peso: ')))
    if len(princ) == 0:
        mai = men = temp[1]
    else:
        if temp[1] > mai:
            mai = temp[1]
        if temp[1] < men:
            men = temp[1]
    princ.append(temp[:])
    temp.clear()
    resp = str(input('Quer continuar? [S/N] '))
    if resp in 'Nn':
        break
print('-=' * 30)
print(f'Ao todo, você cadastrou {len(princ)} pessoas.')
print(f'O maior peso foi de {mai}Kg. Peso de ', end='')
for p in princ:
    if p[1] == mai:
        print(f'[{p[0]}] ', end='')
print()
print(f'O menor peso foi de {men}Kg. Peso de ', end='')
for p in princ:
    if p[1] == men:
        print(f'[{p[0]}] ', end='')
print()
