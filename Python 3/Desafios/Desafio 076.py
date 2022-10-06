"""Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência.
No final, mostre uma listagem de preços, organizando os dados em forma tabular.
"""

listagem = ('Lápis', 1.75, 'Borracha', 2, 'Caderno', 15.9, 'Estojo', 25, 'Transferidor', 4.2, 'Compasso', 9.99, 'Mochila', 120.32, 'Canetas', 22.3, 'Livro', 34.9)

divisor = '-' * 45

print(divisor)
print('{:^45}'.format("LISTAGEM DE PREÇOS"))
print(divisor)

for index_produto, produto_preco in enumerate(listagem):
    if index_produto % 2 == 0:
        print("{:.<36}R$".format(produto_preco), end=" ")
    else:
        print(f'{produto_preco:6.2f}')

print(divisor)


#  Forma do Guanabara

print('-' * 40)
print(f'{"LISTAGEM DE PREÇOS":^40}')
print('-' * 40)
for pos in range(0, len(listagem)):
    if pos % 2 == 0:
        print(f'{listagem[pos]:.<30}', end='')
    else:
        print(f'R${listagem[pos]:7.2f}')
print('-' * 40)
