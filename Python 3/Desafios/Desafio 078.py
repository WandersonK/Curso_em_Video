"""Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
No final, moste qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.
"""

lista_valores = list()

for i in range(0, 5):
    lista_valores.append(int(input(f'Digite um valor para a Posição {i}: ')))

maior_valor = max(lista_valores)
menor_valor = min(lista_valores)


def verifica_posicoes(tamanho):
    for pos, valor in enumerate(lista_valores):
        if valor == tamanho:
            print(f'{pos}...', end=' ')


print('=-' * 25)
print(f'Você digitou os valores {lista_valores}')

print(f'O \033[35mmaior\033[m valor digitado foi {maior_valor} nas posições ', end='')
verifica_posicoes(maior_valor)

print(f'\nO \033[35mmenor\033[m valor digitado foi {menor_valor} nas posições ', end='')
verifica_posicoes(menor_valor)
print()


#  Forma do Guanabara

listanum = []
mai = 0
men = 0
for c in range(0, 5):
    listanum.append(int(input(f'Digite um valor para a Posição {c}: ')))
    if c == 0:
        mai = men = listanum[c]
    else:
        if listanum[c] > mai:
            mai = listanum[c]
        if listanum[c] < men:
            men = listanum[c]
print('=-' * 30)
print(f'Você digitou os valores {listanum}')
print(f'O maior valor digitado foi {mai} nas posições ', end='')
for i, v in enumerate(listanum):
    if v == mai:
        print(f'{i}... ', end='')
print()
print(f'O menor valor digitado foi {men} nas posições ', end='')
for i, v in enumerate(listanum):
    if v == men:
        print(f'{i}... ', end='')
print()
