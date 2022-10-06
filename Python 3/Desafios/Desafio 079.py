"""Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. Caso o número já exista lá dentro, ele não será adicionado.
No final, serão exibidos todos os valores únicos digitados, em ordem crescente.
"""

valores = list()

while True:
    opcao = ' '

    valor = int(input("Digite um valor: "))

    if valor not in valores:
        valores.append(valor)
        print('Valor adicionado com sucesso...')
    else:
        print('Valor duplicado! Não vou adicionar...')

    while opcao not in 'SsNn':
        opcao = input('Quer continuar? [S/N] ')

    if opcao in 'Nn':
        break

valores.sort()

print('-=' * 35)
print(f'Você digitou os valores {valores}')


# Forma do Guanabara

números = list()
while True:
    n = int(input('Digite um valor: '))
    if n not in números:
        números.append(n)
        print('Valor adicionado com sucesso...')
    else:
        print('Valor duplicado! Não vou adicionar...')
    r = str(input('Quer continuar? [S/N] '))
    if r in 'Nn':
        break
print('-=' * 30)
números.sort()
print(f'Você digitou os valores {números}')
