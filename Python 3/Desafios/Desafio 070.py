""" Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar.
No final, mostre:
A) Qual é o total gasto na compra.
B) Quantos produtos custam mais de R$ 1000.
C) Qual é o nome do produto mais barato.
"""

total_gasto = maior1000 = 0
lista_precos = []
lista_produtos = []
divisor = '-' * 30

print(divisor)
print("{:^30}".format("WK SUPERMERCADO"))
print(divisor)

while True:
    produto = str(input("Nome do Produto: "))
    preco = float(input("Preço: R$ "))
    
    lista_precos.append(preco)
    lista_produtos.append(produto)
    
    total_gasto += preco
    
    if preco > 1000:
        maior1000 += 1
    
    while True:
        continuar = str(input("Deseja Continuar? [S/N] ")).upper()[0]
        if continuar in 'SN':
            break
    
    print()
    
    if continuar == 'N':
        break

menor_preco = min(lista_precos)
produto_menor_preco = lista_produtos[lista_precos.index(menor_preco)]

print("{0} FIM DO PROGRAMA {0}".format('=' * 11))
print(f"O total gasto na compra foi de R$ {total_gasto:.2f}")
print(f"Da lista, {maior1000} produtos custam mais de R$ 1000.00")
print(f"O produto com menor preço foi: {produto_menor_preco}, custando R$ {menor_preco:.2f}")



"""   FORMA GUANABARA   """
total = totmil = menor = cont = 0
barato = ' '
while True:
    produto = str(input('Nome do Produto: '))
    preço = float(input('Preço: R$'))
    cont += 1
    total += preço
    if preço > 1000:
        totmil += 1
    if cont == 1 or preço < menor:
        menor = preço
        barato = produto
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp =='N':
        break
print('{:-^40}'.format(' FIM DO PROGRAMA '))
print(f'O total da compra foi R${total:.2f}')
print(f'Temos {totmil} produtos custando mais de R$1000.00')
print(f'O produto mais barato foi {barato} que custa R${menor:.2f}')
