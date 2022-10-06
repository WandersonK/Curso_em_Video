"""Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, já na posição correta de inserção (sem usar o sort()).
No final, mostre a lista ordenada na tela.
"""

lista = list()
posicao = 0

for i in range(0, 5):

    valor = int(input('Digite um valor: '))

    for item in range(0, len(lista)):

        if valor <= lista[item]:
            frase = f'Adicionado na posição {item} da lista...'
            posicao = item
            break

        elif valor > lista[item]:
            frase = 'Adicionado ao final da lista...'
            posicao = item + 1

    if len(lista) == 0:
        print('Adicionado ao final da lista...')
        lista.append(valor)

    else:
        print(frase)
        lista.insert(posicao, valor)

print('-=' * 40)
print(f'Os valores digitados em ordem foram {lista}')


# Forma do Guanabara

lista = []
for c in range(0, 5):
    n = int(input('Digite um valor: '))
    if c == 0 or n > lista[-1]:
        lista.append(n)
        print('Adicionado ao final da lista...')
    else:
        pos = 0
        while pos < len(lista):
            if n <= lista[pos]:
                lista.insert(pos, n)
                print(f'Adicionado na posição {pos} da lista...')
                break
            pos += 1
print('-=' * 30)
print(f'Os valores digitados em ordem foram {lista}')
