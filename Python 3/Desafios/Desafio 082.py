"""Crie um programa que vai ler vários números e colocar em uma lista.
Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores impares digitados, respectivamente.
Ao final, mostre o conteúdo das três listas geradas.
"""

lista_geral = list()
lista_impar = list()
lista_par = list()

while True:
    numero = int(input('Informe um número: '))

    lista_geral.append(numero)

    continuar = input('Deseja continuar? [S/N] ').strip()[0]

    while continuar not in 'NnSs':
        continuar = input('Opção inválida. Deseja continuar? [S/N] ').strip()[0]

    if continuar in 'Nn':
        break

for num in lista_geral:
    if num % 2 == 0:
        lista_par.append(num)
    else:
        lista_impar.append(num)

print('-=' * 40)
print(f'Lista total {lista_geral}')
print(f'Lista de pares {lista_par}')
print(f'Lista de impares {lista_impar}')


# Forma do Guanabara

num = list()
pares = list()
ímpares = list()
while True:
    num.append(int(input('Digite um número: ')))
    resp = str(input('Quer continuar? [S/N] '))
    if resp in 'Nn':
        break
for i, v in enumerate(num):
    if v % 2 == 0:
        pares.append(v)
    elif v % 2 == 1:
        ímpares.append(v)
print('-=' * 30)
print(f'A lista completa é {num}')
print(f'A lista de pares é {pares}')
print(f'A lista de ímpares é {ímpares}')
