"""Crie um programa que vai ler vários números e colocar em uma lista.
Depois disso, mostre:
A) Quantos números foram digitados.
B) A lista de valores, ordenado de forma decrescente.
C) Se o valor 5 foi digitado e está ou não na lista.
"""

lista = list()

while True:
    lista.append(int(input('Digite um valor: ')))

    continuar = input('Deseja continuar? [S/N] ').strip()[0]

    while continuar not in 'SsNn':
        continuar = input('Opção inválida. Deseja continuar? [S/N] ').strip()[0]

    if continuar in 'Nn':
        break

print(f'Foram digitados {len(lista)} números.')
print(f'Lista descrescente {sorted(lista, reverse=True)}')

if 5 in lista:
    print(f'O valor 5 foi digitado na posição {lista.index(5) + 1}.')
    print(f'Na lista decrescente está na {sorted(lista, reverse=True).index(5) + 1}º posição.')
else:
    print('O valor 5 não foi encontrado na lista.')


# Forma do Guanabara

valores = []
while True:
    valores.append(int('Digite um valor: '))
    resp = str(input('Quer continuar? [S/N] '))
    if resp in 'Nn':
        break
print('-=' * 30)
print(f'Você digitou {len(valores)} elementos.')
valores.sort(reverse=True)
print(f'Os valores em ordem decrescente são {valores}')
if 5 in valores:
    print('O valor 5 faz parte da lista!')
else:
    print('O valor 5 não foi encontrado na lista!')
