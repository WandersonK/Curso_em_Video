""" Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
- À vista dinheiro/cheque: 10% de desconto
- À vista no cartão: 5% de desconto
- em até 2x no cartão: preço normal
- 3x ou mais no cartão: 20% de juros
"""
from time import sleep

print("\033[34m{0} WK SYSTEM PAGAMENTOS {0}\033[m".format('=' * 10))

preco_produto = float(input("Informe o preço do produto \033[32mR$\033[m "))

print("Indique a condição de pagamento abaixo:")

print("\033[33m>\033[m \033[1;35m1\033[m - À vista no dinheiro ou cheque.")
print("\033[33m>\033[m \033[1;35m2\033[m - À vista no cartão.")
print("\033[33m>\033[m \033[1;35m3\033[m - Em até 2x no cartão.")
print("\033[33m>\033[m \033[1;35m4\033[m - Em 3x ou mais no cartão.")

forma_pagamento = int(input('\033[32m>>\033[m '))

print("\nAnalisando...")
sleep(2)

if forma_pagamento == 1:
    print("\nVocê recebe \033[32m10% de desconto\033[m.")
    print("== Resumo ==")
    print("Valor do Produto: R${:.2f}.".format(preco_produto))
    print("Desconto: R${:.2f}.".format(preco_produto * 0.1))
    print("Preço com desconto: R${:.2f}.".format(preco_produto * (1 - 0.1)))

elif forma_pagamento == 2:
    print("\nVocê recebe \033[32m5% de desconto\033[m.")
    print("== Resumo ==")
    print("Valor do Produto: R${:.2f}.".format(preco_produto))
    print("Desconto: R${:.2f}.".format(preco_produto * 0.05))
    print("Preço com desconto: R${:.2f}.".format(preco_produto * (1 - 0.05)))

elif forma_pagamento == 3:
    print("\nInfelizmente não conseguimos te liberar um desconto.")
    print("Em até 2x no cartão o preço se mantem em R${:.2f}.".format(preco_produto))

elif forma_pagamento == 4:
    vezes_dividir = int(input("\nEm quantas vezes gostaria de dividir? "))
    print("Com essa opção você pagará \033[33m20% de juros\033[m.")
    print("== Resumo ==")
    print("Valor do Produto: R${:.2f}.".format(preco_produto))
    print("Juros: R${:.2f}.".format(preco_produto * 0.2))
    print("Preço com juros: R${:.2f}.".format(preco_produto * (1 + 0.2)))
    print("Valor das parcelas: {} vezes de R${:.2f}.".format(vezes_dividir, (preco_produto * (1 + 0.2)) / vezes_dividir))

else:
    print("\033[31mOpção inválida, tente novamente.\033[m")
